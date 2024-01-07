def get_success_response(data=None):
    if data is None:
        data = dict()
    return {"result": "success", "data": data, "error": None}


def get_failed_response(exec="Api failed!"):
    return {"result": "failed", "data": None, "error": exec}
