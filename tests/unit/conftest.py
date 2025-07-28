import json

import pytest


@pytest.fixture
def mock_get_airports_light_response():
    with open('tests/fixtures/get_airports_light.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_airlines_light_response():
    with open('tests/fixtures/get_airlines_light.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_airport_response():
    with open('tests/fixtures/get_airports.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_api_usage_response():
    with open('tests/fixtures/get_api_usage.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_flight_positions_count_response():
    with open('tests/fixtures/get_flight_positions_count.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_flight_positions_light_response():
    with open('tests/fixtures/get_flight_positions_light.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_flight_positions_response():
    with open('tests/fixtures/get_flight_positions.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_flight_summary_count_response():
    with open('tests/fixtures/get_flight_summary_count.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_flight_summary_light_response():
    with open('tests/fixtures/get_flight_summary_light.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_flight_summary_response():
    with open('tests/fixtures/get_flight_summary.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_flight_tracks_response():
    with open('tests/fixtures/get_flight_tracks.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_historic_flight_positions_count_response():
    with open('tests/fixtures/get_historic_flight_positions_count.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_historic_flight_positions_light_response():
    with open('tests/fixtures/get_historic_flight_positions_light.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_historic_flight_positions_response():
    with open('tests/fixtures/get_historic_flight_positions.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_historic_flight_events_light_response():
    with open('tests/fixtures/get_historic_flight_events_light.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def mock_get_historic_flight_events_response():
    with open('tests/fixtures/get_historic_flight_events.json', 'r') as f:
        return json.load(f)
