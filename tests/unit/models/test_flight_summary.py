from datetime import timedelta, datetime, timezone
import pytest
from pydantic import ValidationError

from flight_radar.enums.enums import Direction
from flight_radar.models.common import AirportWithDirection, Route
from flight_radar.models.flight_summary import FlightSummaryBaseRequest


def test_should_raise_validation_error_if_no_flight_id_or_datetime_range_provided():
    with pytest.raises(
        ValidationError,
        match='Either flight_datetime_from and flight_datetime_to or flight_ids must be provided',
    ):
        FlightSummaryBaseRequest()


@pytest.mark.parametrize(
    'key_filters',
    [
        {'flight_ids': ['123']},
        {
            'flight_datetime_from': datetime.now(tz=timezone.utc) - timedelta(days=1),
            'flight_datetime_to': datetime.now(tz=timezone.utc),
        },
    ],
)
def test_should_raise_validation_error_if_no_filters_provided(key_filters):
    with pytest.raises(ValidationError, match='At least one filter parameter must be provided'):
        FlightSummaryBaseRequest(**key_filters)


@pytest.mark.parametrize(
    'flight_datetime_from, flight_datetime_to, message',
    [
        (
            datetime.now(tz=timezone.utc) - timedelta(days=15),
            datetime.now(tz=timezone.utc) - timedelta(days=20),
            'flight_datetime_from must be within the last 14 days',
        ),
        (
            datetime.now(tz=timezone.utc) - timedelta(days=1),
            datetime.now(tz=timezone.utc) - timedelta(days=2),
            'flight_datetime_from must be before flight_datetime_to',
        ),
    ],
)
def test_should_raise_validation_error_if_flight_datetime_range_is_invalid(
    flight_datetime_from, flight_datetime_to, message
):
    with pytest.raises(ValidationError, match=message):
        FlightSummaryBaseRequest(
            flight_datetime_from=flight_datetime_from,
            flight_datetime_to=flight_datetime_to,
            callsigns=['BAW123'],
        )


@pytest.mark.parametrize(
    'field',
    [
        'callsigns',
        'flight_ids',
        'registrations',
        'painted_as',
        'operating_as',
        'aircraft',
    ],
)
def test_should_raise_validation_error_if_too_many_values_in_list_filters_provided(
    field,
):
    filters = ['BAW123'] * 16
    message = 'List should have at most 15 items after validation'
    with pytest.raises(ValidationError, match=message):
        FlightSummaryBaseRequest(
            **{field: filters},
        )


def test_should_raise_validation_error_if_too_many_values_in_airport_filters_provided():
    filters = [AirportWithDirection(airport='LHR', direction=Direction.BOTH)] * 16
    message = 'List should have at most 15 items after validation'
    with pytest.raises(ValidationError, match=message):
        FlightSummaryBaseRequest(
            airports=filters,
        )


def test_should_raise_validation_error_if_too_many_values_in_route_filters_provided():
    filters = [Route(origin='LHR', destination='BKK')] * 16
    message = 'List should have at most 15 items after validation'
    with pytest.raises(ValidationError, match=message):
        FlightSummaryBaseRequest(
            routes=filters,
        )
