class ExpectedError(object):
    def __init__(self, code=None, message=None, key=None):
        self.code = code
        self.message = message
        self.key = key

    def __repr__(self):
        return str({
            "code": self.code,
            "message": self.message,
            "key": self.key
        })


class TestCaseData(object):
    def __init__(self, description, status_code, data, general_error=None, errors=None):
        self.description = description
        self.status_code = status_code
        self.general_error = general_error
        self.errors = errors
        self.data = data


