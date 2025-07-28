from unittest.mock import MagicMock

import pytest
from pydantic import BaseModel

from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.enums.enums import HTTPStatus
from flight_radar.errors import (
    BadRequestError,
    InsufficientCredits,
    InternalServerError,
    InvalidResponseError,
    NotFoundError,
    TooManyRequestsError,
    UnauthorizedError,
)


@pytest.mark.parametrize(
    'status_code, error_class',
    [
        (HTTPStatus.BAD_REQUEST, BadRequestError),
        (HTTPStatus.UNAUTHORIZED, UnauthorizedError),
        (HTTPStatus.PAYMENT_REQUIRED, InsufficientCredits),
        (HTTPStatus.NOT_FOUND, NotFoundError),
        (HTTPStatus.TOO_MANY_REQUESTS, TooManyRequestsError),
        (HTTPStatus.INTERNAL_SERVER_ERROR, InternalServerError),
    ],
)
def test_should_handle_non_success_get_case(status_code, error_class):
    session = MagicMock()
    session.get.return_value.__enter__.return_value.status_code = status_code.value

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')

    class DummyResponse(BaseModel):
        pass

    with pytest.raises(error_class):
        api_client.get('test-path', DummyResponse)


def test_should_handle_unparsable_get_response():
    session = MagicMock()

    class TestResponse(BaseModel):
        name: str

    session.get.return_value.__enter__.return_value.status_code = 200
    session.get.return_value.__enter__.return_value.json.return_value = 'invalid'

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')

    with pytest.raises(InvalidResponseError):
        api_client.get('test-path', TestResponse)


@pytest.mark.parametrize(
    'status_code, error_class',
    [
        (HTTPStatus.BAD_REQUEST, BadRequestError),
        (HTTPStatus.UNAUTHORIZED, UnauthorizedError),
        (HTTPStatus.PAYMENT_REQUIRED, InsufficientCredits),
        (HTTPStatus.NOT_FOUND, NotFoundError),
        (HTTPStatus.TOO_MANY_REQUESTS, TooManyRequestsError),
        (HTTPStatus.INTERNAL_SERVER_ERROR, InternalServerError),
    ],
)
def test_should_handle_non_success_get_many_case(status_code, error_class):
    session = MagicMock()
    session.get.return_value.__enter__.return_value.status_code = status_code.value

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')

    class DummyResponse(BaseModel):
        pass

    with pytest.raises(error_class):
        api_client.get_many('test-path', DummyResponse)


def test_should_handle_unparsable_get_many_response():
    session = MagicMock()

    class TestResponse(BaseModel):
        name: str

    session.get.return_value.__enter__.return_value.status_code = 200
    session.get.return_value.__enter__.return_value.json.return_value = 'invalid'

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')

    with pytest.raises(InvalidResponseError):
        api_client.get_many('test-path', TestResponse)
