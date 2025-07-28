from unittest.mock import MagicMock

from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.services.service import FlightRadarClient


def test_should_pass_icao_code_correctly(mock_get_airlines_light_response):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_airlines_light_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    service.get_airlines_light('AAL')

    session.get.assert_called_once()

    call_args = session.get.call_args
    url = call_args[0][0]
    assert url == 'https://api.flightradar24.com/static/airlines/AAL/light'


def test_should_parse_get_airlines_light_response_correctly(
    mock_get_airlines_light_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_airlines_light_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    response = service.get_airlines_light('AAL')

    assert response.iata == 'AA'
    assert response.icao == 'AAL'
    assert response.name == 'American Airlines'
