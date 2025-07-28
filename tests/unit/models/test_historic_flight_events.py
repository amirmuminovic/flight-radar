import pytest
from pydantic import ValidationError

from flight_radar.dtos.historic_flight_event import HistoricFlightEventRequestDto
from flight_radar.enums.enums import HistoricFlightEventTypes
from flight_radar.models.historic_flight_event import HistoricFlightEventRequest


def test_should_serialize_historic_flight_event_request():
    request = HistoricFlightEventRequest(
        flight_ids=['BA123', 'BA456'],
        event_types=[HistoricFlightEventTypes.GATE_DEPARTURE],
    )
    assert request.to_dto() == HistoricFlightEventRequestDto(
        flight_ids='BA123,BA456',
        event_types='gate_departure',
    )


def test_should_serialize_historic_flight_event_request_with_all_event_types():
    request = HistoricFlightEventRequest(
        flight_ids=['BA123', 'BA456'],
        event_types=None,
    )
    assert request.to_dto() == HistoricFlightEventRequestDto(
        flight_ids='BA123,BA456',
        event_types='all',
    )


def test_should_raise_validation_error_if_too_many_flight_ids():
    with pytest.raises(ValidationError, match='List should have at most 15 items after validation'):
        HistoricFlightEventRequest(
            flight_ids=['BA123'] * 16,
        )
