class UnauthorizedError(Exception):
    pass


class NotFoundError(Exception):
    pass


class BadRequestError(Exception):
    pass


class InsufficientCredits(Exception):
    pass


class InternalServerError(Exception):
    pass


class InvalidResponseError(Exception):
    pass


class TooManyRequestsError(Exception):
    pass
