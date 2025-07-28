# Flight Radar API Client

This project provides a Python client for interacting with the Flight Radar API. It simplifies the process of fetching flight-related data, such as live and historic flight positions, flight summaries, and airline and airport information.

## Features

- **Live Flight Data:** Get real-time flight positions for aircraft around the world.
- **Historic Flight Data:** Access historical flight data, including positions, summaries, and events.
- **Flight Details:** Retrieve detailed information about specific flights, including their tracks.
- **Airline & Airport Information:** Look up details about airlines and airports.
- **API Usage Monitoring:** Check your API usage statistics.

## Installation

To install the Flight Radar API Client, you can use pip:

```bash
pip install flight-radar
```

## Quickstart

Here's a simple example of how to use the client to get live flight positions:

```python
from flight_radar.factory import get_flight_radar_client
from flight_radar.models import LiveFlightPositionRequest

# Create a flight radar client
client = get_flight_radar_client()

# Create a request to get the live flight positions
request = LiveFlightPositionRequest(
    limit=10,
    # Add any other parameters you might need
)

# Get the live flight positions
positions = client.get_live_flight_positions(request)

# Print the positions
for position in positions:
    print(position)
```

This will output a list of `FlightPosition` objects, each containing information about a live flight.

## Documentation

For more detailed information about the available methods and models, please refer to the [official documentation](https://amirmuminovic.github.io/flight-radar/).

## Contributing

Contributions are welcome! If you'd like to contribute, please check out the [CONTRIBUTING.md](CONTRIBUTING.md).

## Local Development

To set up the project for local development, follow these steps. This project uses `uv` for package management.

1.  **Install uv:**

    Follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/) to install `uv`.

2. **Create and activate a virtual environment:**

    To run the examples, you first need to create and activate a virtual environment:

    ```bash
    uv venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**

    Install the project dependencies, including the development dependencies:
    ```bash
    uv sync --extra dev
    ```

4.  **Set up pre-commit hooks:**

    This project uses pre-commit hooks to ensure code quality. Install them by running:
    ```bash
    uv run pre-commit install
    ```

5.  **Run an example:**

    Then, you can run any of the example scripts:

    ```bash
    python examples/alert_when_flight_enters_circular_area.py
    ```

Now you are all set up to run the project locally and contribute to its development.
