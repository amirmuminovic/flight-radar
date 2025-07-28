from datetime import datetime
from unittest.mock import MagicMock

from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.enums.enums import DataSources, Direction, FlightCategory
from flight_radar.models.common import AirportWithDirection, Route
from flight_radar.models.flight_position import (
    LiveFlightPositionRequest,
)
from flight_radar.services.service import FlightRadarClient


def test_should_serialize_get_flight_positions_light_request_correctly(
    mock_get_flight_positions_light_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_positions_light_response
    session.get.return_value.__enter__.return_value = mock_response
    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = LiveFlightPositionRequest(
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
        limit=100,
    )
    service.get_live_flight_positions_light(request)

    session.get.assert_called_once()

    call_args = session.get.call_args
    url = call_args[0][0]
    params = call_args[1].get('params', {})

    assert url == 'https://api.flightradar24.com/live/flight-positions/light'
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
    assert params['limit'] == 100


def test_should_parse_get_flight_positions_light_response_correctly(
    mock_get_flight_positions_light_response,
):
    session = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_get_flight_positions_light_response
    session.get.return_value.__enter__.return_value = mock_response

    api_client = FlightRadarApiClient(session, 'https://api.flightradar24.com', 'test')
    service = FlightRadarClient(api_client)

    request = LiveFlightPositionRequest(bounds=(42.4734, 37.3315, -10.0142, -4.1151))
    response = service.get_live_flight_positions_light(request)

    assert len(response) != 0

    assert response[0].fr24_id == '321a0cc3'
    assert response[0].hex == '394C19'
    assert response[0].callsign == 'AFR1463'
    assert response[0].lat == -0.08806
    assert response[0].lon == -168.07118
    assert response[0].track == 219
    assert response[0].alt == 38000
    assert response[0].gspeed == 500
    assert response[0].vspeed == 340
    assert response[0].squawk == '6135'
    assert response[0].timestamp == datetime.fromisoformat('2023-11-08T10:10:00Z')
    assert response[0].source == 'ADSB'
