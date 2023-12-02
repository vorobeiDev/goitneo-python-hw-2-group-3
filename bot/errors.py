class ContactExistsError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class IncorrectArgumentsQuantityError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class ContactNotFoundError(Exception):
    pass


class ContactsAreEmptyError(Exception):
    pass
