from typing import NoReturn, Type, TypeVar

import requests
from pydantic import ValidationError

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

T = TypeVar('T')


class FlightRadarApiClient:
    def __init__(self, session: requests.Session, base_url: str = None, api_key: str = None):
        session.headers.update({'Authorization': f'Bearer {api_key}', 'Accept-Version': 'v1'})
        self.base_url = base_url
        self.session = session

    def _handle_non_success_case(self, response: requests.Response) -> NoReturn:
        match response.status_code:
            case HTTPStatus.BAD_REQUEST.value:
                raise BadRequestError(response.json())
            case HTTPStatus.UNAUTHORIZED.value:
                raise UnauthorizedError(response.json())
            case HTTPStatus.PAYMENT_REQUIRED.value:
                raise InsufficientCredits(response.json())
            case HTTPStatus.NOT_FOUND.value:
                raise NotFoundError(response.json())
            case HTTPStatus.TOO_MANY_REQUESTS.value:
                raise TooManyRequestsError(response.json())
            case HTTPStatus.INTERNAL_SERVER_ERROR.value | _:
                raise InternalServerError(response.json())

    def get(self, url: str, response_dto_class: Type[T], params: dict = None) -> T:
        with self.session.get(f'{self.base_url}{url}', params=params) as response:
            if response.status_code != 200:
                self._handle_non_success_case(response)

            try:
                dto = response_dto_class.model_validate(response.json())
                return dto
            except ValidationError as e:
                raise InvalidResponseError(e)

    def get_many(self, url: str, response_dto_class: Type[T], params: dict = None) -> T:
        with self.session.get(f'{self.base_url}{url}', params=params) as response:
            if response.status_code != 200:
                self._handle_non_success_case(response)

            try:
                dtos = [response_dto_class.model_validate(entry) for entry in response.json()]
                return dtos
            except ValidationError as e:
                raise InvalidResponseError(e)
