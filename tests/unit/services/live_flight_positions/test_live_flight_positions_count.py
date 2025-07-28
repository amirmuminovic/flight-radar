from unittest.mock import MagicMock

from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.enums.enums import DataSources, Direction, FlightCategory
from flight_radar.models.common import AirportWithDirection, Route
from flight_radar.models.flight_position import LiveFlightPositionCountRequest
from flight_radar.services.service import FlightRadarClient


def test_should_serialize_get_flight_positions_count_request_correctly(
    mock_get_flight_positions_count_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_positions_count_response
    session.get.return_value.__enter__.return_value = mock_response
    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = LiveFlightPositionCountRequest(
        bounds=(42.4734, 37.3315, -10.0142, -4.1151),
        flights=['CA4515', 'UA1742'],
        callsigns=['WJA329', 'WSW102'],
        registrations=['D-AFAM', 'EC-MQM'],
        painted_as=['SAS', 'ART'],
        operating_as=['SAS', 'ART'],
        airports=[
            AirportWithDirection(airport='LHR'),
            AirportWithDirection(airport='SE'),
            AirportWithDirection(airport='WAW', direction=Direction.INBOUND),
            AirportWithDirection(airport='US'),
            AirportWithDirection(airport='JFK', direction=Direction.OUTBOUND),
            AirportWithDirection(airport='ESSA', direction=Direction.BOTH),
        ],
        routes=[
            Route(origin='SE', destination='US'),
            Route(origin='ESSA', destination='JFK'),
        ],
        aircraft=['B38M', 'B738'],
        altitude_ranges=[(0, 3000), (5000, 7000)],
        squawks=['6135', '7070'],
        categories=[FlightCategory.PASSENGER, FlightCategory.CARGO],
        data_sources=[DataSources.ADSB, DataSources.MLAT, DataSources.ESTIMATED],
        airspaces=['ESAA', 'LFFF'],
        gspeed=(0, 40),
    )
    service.get_live_flight_position_count(request)

    session.get.assert_called_once()

    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})

    assert url == 'https://api.flightradar24.com/live/flight-positions/count'
    assert params['bounds'] == '42.473,37.332,-10.014,-4.115'
    assert params['flights'] == 'CA4515,UA1742'
    assert params['callsigns'] == 'WJA329,WSW102'
    assert params['registrations'] == 'D-AFAM,EC-MQM'
    assert params['painted_as'] == 'SAS,ART'
    assert params['operating_as'] == 'SAS,ART'
    assert params['airports'] == 'LHR,SE,inbound:WAW,US,outbound:JFK,both:ESSA'
    assert params['routes'] == 'SE-US,ESSA-JFK'
    assert params['aircraft'] == 'B38M,B738'
    assert params['altitude_ranges'] == '0-3000,5000-7000'
    assert params['squawks'] == '6135,7070'
    assert params['categories'] == 'P,C'
    assert params['data_sources'] == 'ADSB,MLAT,ESTIMATED'
    assert params['airspaces'] == 'ESAA,LFFF'
    assert params['gspeed'] == '0-40'


def test_should_parse_get_flight_positions_count_correctly(
    mock_get_flight_positions_count_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_positions_count_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = LiveFlightPositionCountRequest(bounds=(42.4734, 37.3315, -10.0142, -4.1151))
    response = service.get_live_flight_position_count(request)

    assert response.record_count == 1233
