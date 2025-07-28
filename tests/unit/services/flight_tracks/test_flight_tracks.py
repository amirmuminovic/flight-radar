from datetime import datetime
from unittest.mock import MagicMock


from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.models.flight_track import FlightTrackRequest
from flight_radar.services.service import FlightRadarClient


def test_should_pass_flight_tracks_params_correctly(mock_get_flight_tracks_response):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_tracks_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = FlightTrackRequest(
        flight_id='391e1d99',
    )
    service.get_flight_tracks(request)

    session.get.assert_called_once()
    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})
    assert url == 'https://api.flightradar24.com/flight-tracks'
    assert params == {'flight_id': '391e1d99'}


def test_should_parse_get_flight_tracks_response_correctly(
    mock_get_flight_tracks_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_tracks_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = FlightTrackRequest(
        flight_id='391e1d99',
    )
    fr24_id, tracks = service.get_flight_tracks(request)

    assert len(tracks) != 0

    assert fr24_id == '35f2ffd9'
    assert tracks[0].timestamp == datetime.fromisoformat('2024-07-02T11:22:43Z')
    assert tracks[0].latitude == 62.97148
    assert tracks[0].longitude == -26.25193
    assert tracks[0].altitude == 33000
    assert tracks[0].gspeed == 505
    assert tracks[0].vspeed == 0
    assert tracks[0].track == 105
    assert tracks[0].squawk == '2566'
    assert tracks[0].callsign == 'THY10'
    assert tracks[0].source == 'ADSB'
