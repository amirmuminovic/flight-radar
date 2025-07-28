from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock

from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.models.common import AirportWithDirection, Route
from flight_radar.models.flight_summary import FlightSummaryRequest
from flight_radar.services.service import FlightRadarClient


def test_should_pass_flight_summary_params_correctly_with_flight_ids(
    mock_get_flight_summary_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_summary_response
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
    service.get_flight_summary(request)

    session.get.assert_called_once()
    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})
    assert url == 'https://api.flightradar24.com/flight-summary/full'
    assert params == {
        'flight_ids': '391fdd79',
        'painted_as': 'SAS',
        'operating_as': 'SAS',
        'airports': 'LHR',
        'routes': 'LHR-JFK',
        'aircraft': 'B738',
    }


def test_should_pass_flight_summary_params_correctly_with_flight_datetime_range(
    mock_get_flight_summary_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_summary_response
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
    service.get_flight_summary(request)

    session.get.assert_called_once()
    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})
    assert url == 'https://api.flightradar24.com/flight-summary/full'
    assert params == {
        'flight_datetime_from': flight_datetime_from.isoformat(),
        'flight_datetime_to': flight_datetime_to.isoformat(),
        'painted_as': 'SAS',
        'operating_as': 'SAS',
        'airports': 'LHR',
        'routes': 'LHR-JFK',
        'aircraft': 'B738',
    }


def test_should_parse_get_flight_summary_response_correctly(
    mock_get_flight_summary_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_summary_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = FlightSummaryRequest(
        flight_ids=['391fdd79'],
        painted_as=['SAS'],
    )
    response = service.get_flight_summary(request)

    assert len(response) != 0

    assert response[0].fr24_id == '391e1d99'
    assert response[0].flight == 'RR9407'
    assert response[0].callsign == 'RYS9407'
    assert response[0].operating_as == 'RYS'
    assert response[0].painted_as == 'RYS'
    assert response[0].type == 'B738'
    assert response[0].reg == 'SP-RSZ'
    assert response[0].orig_icao == 'LZIB'
    assert response[0].orig_iata == 'BTS'
    assert response[0].datetime_takeoff == datetime.fromisoformat('2025-02-13T21:23:39')
    assert response[0].runway_takeoff == '13'
    assert response[0].dest_icao == 'LGTS'
    assert response[0].dest_iata == 'SKG'
    assert response[0].dest_icao_actual == 'LGTS'
    assert response[0].dest_iata_actual == 'SKG'
    assert response[0].datetime_landed == datetime.fromisoformat('2025-02-13T22:39:56')
    assert response[0].runway_landed == '16'
    assert response[0].flight_time == 4577
    assert response[0].actual_distance == 983.342
    assert response[0].circle_distance == 965.913
    assert response[0].hex == '48C235'
    assert response[0].first_seen == datetime.fromisoformat('2025-02-13T20:54:19')
    assert response[0].last_seen == datetime.fromisoformat('2025-02-13T22:43:49')
    assert response[0].flight_ended is True
