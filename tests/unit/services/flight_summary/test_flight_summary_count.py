from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock


from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.models.common import AirportWithDirection, Route
from flight_radar.models.flight_summary import FlightSummaryCountRequest
from flight_radar.services.service import FlightRadarClient


def test_should_pass_flight_summary_count_params_correctly_with_flight_ids(
    mock_get_flight_summary_count_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_summary_count_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = FlightSummaryCountRequest(
        flight_ids=['391fdd79'],
        painted_as=['SAS'],
        operating_as=['SAS'],
        airports=[
            AirportWithDirection(airport='LHR'),
        ],
        routes=[Route(origin='LHR', destination='JFK')],
        aircraft=['B738'],
    )
    service.get_flight_summary_count(request)

    session.get.assert_called_once()
    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})
    assert url == 'https://api.flightradar24.com/flight-summary/count'
    assert params == {
        'flight_ids': '391fdd79',
        'painted_as': 'SAS',
        'operating_as': 'SAS',
        'airports': 'LHR',
        'routes': 'LHR-JFK',
        'aircraft': 'B738',
    }


def test_should_pass_flight_summary_count_params_correctly_with_flight_datetime_range(
    mock_get_flight_summary_count_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_summary_count_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    flight_datetime_from = datetime.now(tz=timezone.utc) - timedelta(days=1)
    flight_datetime_to = datetime.now(tz=timezone.utc)

    request = FlightSummaryCountRequest(
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
    service.get_flight_summary_count(request)

    session.get.assert_called_once()
    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})
    assert url == 'https://api.flightradar24.com/flight-summary/count'
    assert params == {
        'flight_datetime_from': flight_datetime_from.isoformat(),
        'flight_datetime_to': flight_datetime_to.isoformat(),
        'painted_as': 'SAS',
        'operating_as': 'SAS',
        'airports': 'LHR',
        'routes': 'LHR-JFK',
        'aircraft': 'B738',
    }


def test_should_parse_get_flight_summary_count_correctly(
    mock_get_flight_summary_count_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_summary_count_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = FlightSummaryCountRequest(
        flight_ids=['391fdd79'],
        painted_as=['SAS'],
    )
    response = service.get_flight_summary_count(request)

    assert response.record_count == 1233
