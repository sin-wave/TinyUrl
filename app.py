from flask import Flask, json, request, jsonify, redirect, render_template
from werkzeug.utils import redirect
from werkzeug.wrappers import response
from db import Database
from dotenv import dotenv_values
from tiny_id import UniqueString
from Schema import Create, Find, FindId
import os

client = Database.Connect()
app = Flask(__name__, static_folder="./static")
config = dotenv_values(".env")
# app.config["CACHE_TYPE"] = "null"


@app.route("/", methods=["GET", "POST"])
def Home():
    try:
        if request.method == "POST":
            long_url = request.form["url"]
            id = UniqueString()
            d_b = client["myFirstDatabase"]
            collection = d_b["url"]
            flag, code, lu = Find(collection, long_url)
            if flag == False:
                short_url = "https://sbbi.herokuapp.com/" + id
                data = {"code": id, "long_url": long_url, "short_url": short_url}
                response = {"long_url": long_url, "short_url": short_url}
                Create(collection, data)
                return jsonify(response), 201
            elif code != None and lu != None:
                short_url = "https://sbbi.herokuapp.com/" + code
                response = {"long_url": lu, "short_url": short_url}
                return jsonify(response), 200

        elif request.method == "GET":
            return render_template("index.html", title="TinyUrl")

    except Exception as e:
        response = {"messsage": "Server Error!"}
        return jsonify(response), 500


@app.route("/<id>", methods=["GET"])
def redirect_url(id):
    d_b = client["myFirstDatabase"]
    collection = d_b["url"]
    lu = FindId(collection, id)
    print(lu)
    if lu == None:
        response = {"message": "Url may be expired"}
        return jsonify(response), 404
    else:
        return redirect(lu)


if __name__ == "__main__":
    # port = dict(config)["PORT"]
    # host = dict(config)["HOST"]
    port = int(os.environ.get("PORT"))
    app.run(host="0.0.0.0", port=port)
