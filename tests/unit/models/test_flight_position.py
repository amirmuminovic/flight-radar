import pytest
from pydantic import ValidationError

from flight_radar.enums.enums import DataSources, Direction, FlightCategory
from flight_radar.models.common import AirportWithDirection, Route
from flight_radar.models.flight_position import FlightPositionBaseRequest


def test_should_raise_validation_error_if_no_filters_provided():
    with pytest.raises(ValidationError):
        FlightPositionBaseRequest()


@pytest.mark.parametrize(
    'altitude_ranges, message',
    [
        [[(-10, 1000)], 'Altitude range must be greater than 0'],
        [[(1000, 0)], 'Altitude range must be in ascending order'],
        [[(1000, 0, 1000)], 'Tuple should have at most 2 items after validation'],
    ],
)
def test_should_raise_validation_error_if_altitude_range_is_invalid(altitude_ranges, message):
    with pytest.raises(ValidationError, match=message):
        FlightPositionBaseRequest(altitude_ranges=altitude_ranges)


@pytest.mark.parametrize(
    'gspeed, message',
    [
        [(-10, 1000), 'Ground speed must be greater than 0'],
        [-5, 'Ground speed must be greater than 0'],
        [(1000, 0), 'Ground speed must be in ascending order'],
        [(1000, 0, 1000), 'Tuple should have at most 2 items after validation'],
    ],
)
def test_should_raise_validation_error_if_gspeed_is_invalid(gspeed, message):
    with pytest.raises(ValidationError, match=message):
        FlightPositionBaseRequest(gspeed=gspeed)


@pytest.mark.parametrize(
    'field',
    [
        'flights',
        'callsigns',
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
        FlightPositionBaseRequest(
            **{field: filters},
        )


def test_should_raise_validation_error_if_too_many_values_in_airport_filters_provided():
    filters = [AirportWithDirection(airport='LHR', direction=Direction.BOTH)] * 16
    message = 'List should have at most 15 items after validation'
    with pytest.raises(ValidationError, match=message):
        FlightPositionBaseRequest(
            airports=filters,
        )


def test_should_raise_validation_error_if_too_many_values_in_route_filters_provided():
    filters = [Route(origin='LHR', destination='BKK')] * 16
    message = 'List should have at most 15 items after validation'
    with pytest.raises(ValidationError, match=message):
        FlightPositionBaseRequest(
            routes=filters,
        )


def test_should_serialize_flight_position_base_request_to_dto():
    request = FlightPositionBaseRequest(
        flights=['BAW123'],
        callsigns=['BAW123'],
        registrations=['BAW123'],
        painted_as=['BAW123'],
        operating_as=['BAW123'],
        airports=[AirportWithDirection(airport='LHR', direction=Direction.BOTH)],
        routes=[Route(origin='LHR', destination='BKK')],
        aircraft=['BAW123'],
        altitude_ranges=[(1000, 2000)],
        gspeed=(100, 200),
        squawks=['1234'],
        categories=[FlightCategory.PASSENGER],
        data_sources=[DataSources.ADSB],
        airspaces=['1234'],
        bounds=(51.5074, -0.1278, 51.5074, -0.1278),
    )
    dto = request.to_dto()
    assert dto.flights == 'BAW123'
    assert dto.callsigns == 'BAW123'
    assert dto.registrations == 'BAW123'
    assert dto.painted_as == 'BAW123'
    assert dto.operating_as == 'BAW123'
    assert dto.airports == 'both:LHR'
    assert dto.routes == 'LHR-BKK'
    assert dto.aircraft == 'BAW123'
    assert dto.altitude_ranges == '1000-2000'
    assert dto.gspeed == '100-200'
    assert dto.squawks == '1234'
    assert dto.categories == FlightCategory.PASSENGER.value
    assert dto.data_sources == DataSources.ADSB.value
    assert dto.airspaces == '1234'
    assert dto.bounds == '51.507,-0.128,51.507,-0.128'


def test_should_serialize_flight_position_base_request_to_dto_with_none_values():
    request = FlightPositionBaseRequest(
        gspeed=6,
    )
    dto = request.to_dto()
    assert dto.bounds is None
    assert dto.flights is None
    assert dto.callsigns is None
    assert dto.registrations is None
    assert dto.painted_as is None
    assert dto.operating_as is None
    assert dto.airports is None
    assert dto.routes is None
    assert dto.aircraft is None
    assert dto.altitude_ranges is None
    assert dto.squawks is None
    assert dto.categories is None
    assert dto.data_sources is None
    assert dto.airspaces is None
    assert dto.gspeed == '6'
