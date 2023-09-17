class DBError(Exception):
    pass


class NoRowsFoundError(Exception):
    pass


class MultipleRowsFoundError(Exception):
    pass


class AlreadyExistError(Exception):
    pass


class TokenError(Exception):
    pass
