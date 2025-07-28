from unittest.mock import MagicMock

import pytest

from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.enums.enums import TimePeriod
from flight_radar.models.api_usage import ApiUsageRequest
from flight_radar.services.service import FlightRadarClient


@pytest.mark.parametrize('period', [TimePeriod.DAY, TimePeriod.WEEK, TimePeriod.MONTH, TimePeriod.YEAR, None])
def test_should_pass_api_usage_params_correctly(mock_get_api_usage_response, period):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_api_usage_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    if period:
        request = ApiUsageRequest(period=period)
    else:
        request = ApiUsageRequest()
    service.get_api_usage(request)

    session.get.assert_called_once()
    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})

    assert url == 'https://api.flightradar24.com/usage'
    assert params == {'period': period.value if period else TimePeriod.DAY.value}


def test_should_parse_api_usage_correctly(mock_get_api_usage_response):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_api_usage_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = ApiUsageRequest()
    response = service.get_api_usage(request)

    assert len(response) != 0
    assert response[0].endpoint == 'live/flight-positions/full?{filters}'
    assert response[0].request_count == 1
    assert response[0].credits == 936
