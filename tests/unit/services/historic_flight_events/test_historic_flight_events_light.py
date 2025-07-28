from datetime import datetime
from unittest.mock import MagicMock

from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.enums.enums import HistoricFlightEventTypes
from flight_radar.models.historic_flight_event import HistoricFlightEventRequest
from flight_radar.services.service import FlightRadarClient


def test_should_serialize_get_historic_flight_event_request(
    mock_get_historic_flight_events_light_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_historic_flight_events_light_response
    session.get.return_value.__enter__.return_value = mock_response
    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = HistoricFlightEventRequest(
        flight_ids=['CA4515', 'UA1742'],
        event_types=[HistoricFlightEventTypes.CRUISING],
    )
    service.get_historic_flight_events_light(request)

    session.get.assert_called_once()

    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})

    assert url == 'https://api.flightradar24.com/historic/flight-events/light'
    assert params['flight_ids'] == 'CA4515,UA1742'
    assert params['event_types'] == 'cruising'


def test_should_parse_get_historical_flight_events_light_response_correctly(
    mock_get_historic_flight_events_light_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_historic_flight_events_light_response
    session.get.return_value.__enter__.return_value = mock_response
    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = HistoricFlightEventRequest(
        flight_ids=['CA4515', 'UA1742'],
        event_types=[HistoricFlightEventTypes.AIRSPACE_TRANSITION],
    )
    response = service.get_historic_flight_events_light(request)

    assert len(response) != 0

    assert response[0].fr24_id == '2efc4160'
    assert response[0].callsign == 'SAS1415'
    assert response[0].hex == '4AC9F5'

    assert len(response[0].events) != 0
    assert response[0].events[0].type == HistoricFlightEventTypes.AIRSPACE_TRANSITION
    assert response[0].events[0].timestamp == datetime.fromisoformat('2023-01-27T06:02:43Z')
    assert response[0].events[0].lat == 55.98839
    assert response[0].events[0].lon == 12.64427
    assert response[0].events[0].alt == 8700
    assert response[0].events[0].gspeed == 301
    assert response[0].events[0].details is not None
    assert response[0].events[0].details.exited_airspace == 'SWEDEN'
    assert response[0].events[0].details.exited_airspace_id == 'ESAA'
    assert response[0].events[0].details.entered_airspace == 'KOBENHAVN'
    assert response[0].events[0].details.entered_airspace_id == 'EKDK'
