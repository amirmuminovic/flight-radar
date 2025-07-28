from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock

from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.models.common import AirportWithDirection, Route
from flight_radar.models.flight_summary import FlightSummaryRequest
from flight_radar.services.service import FlightRadarClient


def test_should_pass_flight_summary_light_params_correctly_with_flight_ids(
    mock_get_flight_summary_light_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_summary_light_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = FlightSummaryRequest(
        flight_ids=['391fdd79'],
        painted_as=['SAS'],
        operating_as=['SAS'],
        airports=[
            AirportWithDirection(airport='LHR'),
        ],
        routes=[Route(origin='LHR', destination='JFK')],
        aircraft=['B738'],
    )
    service.get_flight_summary_light(request)

    session.get.assert_called_once()
    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})
    assert url == 'https://api.flightradar24.com/flight-summary/light'
    assert params == {
        'flight_ids': '391fdd79',
        'painted_as': 'SAS',
        'operating_as': 'SAS',
        'airports': 'LHR',
        'routes': 'LHR-JFK',
        'aircraft': 'B738',
    }


def test_should_pass_flight_summary_light_params_correctly_with_flight_datetime_range(
    mock_get_flight_summary_light_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_summary_light_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    flight_datetime_from = datetime.now(tz=timezone.utc) - timedelta(days=1)
    flight_datetime_to = datetime.now(tz=timezone.utc)

    request = FlightSummaryRequest(
        flight_datetime_from=flight_datetime_from,
        flight_datetime_to=flight_datetime_to,
        painted_as=['SAS'],
        operating_as=['SAS'],
        airports=[
            AirportWithDirection(airport='LHR'),
        ],
        routes=[Route(origin='LHR', destination='JFK')],
        aircraft=['B738'],
    )
    service.get_flight_summary_light(request)

    session.get.assert_called_once()
    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})
    assert url == 'https://api.flightradar24.com/flight-summary/light'
    assert params == {
        'flight_datetime_from': flight_datetime_from.isoformat(),
        'flight_datetime_to': flight_datetime_to.isoformat(),
        'painted_as': 'SAS',
        'operating_as': 'SAS',
        'airports': 'LHR',
        'routes': 'LHR-JFK',
        'aircraft': 'B738',
    }


def test_should_parse_get_flight_summary_light_response_correctly(
    mock_get_flight_summary_light_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_summary_light_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = FlightSummaryRequest(
        flight_ids=['391fdd79'],
        painted_as=['SAS'],
    )
    response = service.get_flight_summary_light(request)

    assert len(response) != 0

    assert response[0].fr24_id == '391fdd79'
    assert response[0].flight == 'D84529'
    assert response[0].callsign == 'NSZ4529'
    assert response[0].operating_as == 'NSZ'
    assert response[0].painted_as == 'NSZ'
    assert response[0].type == 'B38M'
    assert response[0].reg == 'SE-RTC'
    assert response[0].orig_icao == 'ESSA'
    assert response[0].datetime_takeoff is None
    assert response[0].dest_icao == 'GMAD'
    assert response[0].datetime_landed is None
    assert response[0].hex == '4ACA83'
    assert response[0].first_seen == datetime.fromisoformat('2025-02-14T11:47:06Z')
    assert response[0].last_seen == datetime.fromisoformat('2025-02-14T13:11:49Z')
    assert response[0].flight_ended is True
