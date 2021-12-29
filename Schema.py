from logging import exception


def Create(collection, data):
    collection.insert_one(data)


def Find(collection, data):
    try:
        record = collection.find()
        for val in record:
            if val == None:
                return False, None, None
            else:
                val = dict(val)
                long_url = val["long_url"]
                if long_url == data:
                    code = val["code"]
                    return True, code, long_url
        return False, None, None

    except Exception as e:
        return False


def FindId(collection, id):
    try:
        record = collection.find()
        for val in record:
            val = dict(val)
            if val["code"] == id:
                return val["long_url"]
        return None

    except exception as e:
        return None
