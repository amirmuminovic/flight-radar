class UnauthorizedError(Exception):
    """
    Raised when the API returns a 401 Unauthorized error.
    """
    pass


class NotFoundError(Exception):
    """
    Raised when the API returns a 404 Not Found error.
    """
    pass


class BadRequestError(Exception):
    """
    Raised when the API returns a 400 Bad Request error.
    """
    pass


class InsufficientCredits(Exception):
    """
    Raised when the API returns a 402 Payment Required error.
    """
    pass


class InternalServerError(Exception):
    """
    Raised when the API returns a 500 Internal Server Error.
    """
    pass


class InvalidResponseError(Exception):
    """
    Raised when the API returns an invalid response.
    """
    pass


class TooManyRequestsError(Exception):
    """
    Raised when the API returns a 429 Too Many Requests error.
    """
    pass
