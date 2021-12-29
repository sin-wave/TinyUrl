import uuid


def UniqueString():
    str_ = str(uuid.uuid4())[:8]
    return str_


# print(UniqueString())
