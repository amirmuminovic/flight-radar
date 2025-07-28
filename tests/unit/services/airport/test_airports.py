from unittest.mock import MagicMock

from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.services.service import FlightRadarClient


def test_should_pass_iata_code_correctly_get_airports(mock_get_airport_response):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_airport_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    service.get_airports('ARN')

    session.get.assert_called_once()
    call_args = session.get.call_args
    url = call_args[0][0]
    assert url == 'https://api.flightradar24.com/static/airports/ARN/full'


def test_should_parse_get_airports_light_response_correctly(
    mock_get_airports_light_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_airports_light_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    response = service.get_airports_light('ARN')

    assert response.iata == 'ARN'
    assert response.icao == 'ESSA'
    assert response.name == 'Stockholm Arlanda Airport'
