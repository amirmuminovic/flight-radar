.. _flight_position_light_example:

****************************************
Live Flight Positions Example
****************************************

This guide demonstrates how to retrieve live flight positions within a specified geographical area using the Flight Radar SDK.

Prerequisites
=============

Before you begin, ensure you have the following:

*   An API token from FlightRadar24.
*   The ``flight-radar`` library installed.

Step-by-Step Guide
==================

1.  **Import necessary modules**:

    .. code-block:: python

        from flight_radar.factory import get_flight_radar_client
        from flight_radar.models import LiveFlightPositionRequest

2.  **Set up your credentials**:

    Replace ``'your_api_token_here'`` with your actual FlightRadar24 API token.

    .. code-block:: python

        API_TOKEN = 'your_api_token_here'
        BASE_URL = 'https://fr24api.flightradar24.com/api'

3.  **Initialize the client**:

    Create an instance of the Flight Radar client.

    .. code-block:: python

        service = get_flight_radar_client(
            base_url=BASE_URL,
            api_key=API_TOKEN,
        )

4.  **Define the request parameters**:

    Specify the geographical boundaries for which you want to retrieve flight data. The ``bounds`` parameter is a tuple of four floats representing ``(latitude_north, latitude_south, longitude_west, longitude_east)``.

    .. code-block:: python

        request = LiveFlightPositionRequest(bounds=(50.682, 46.218, 14.422, 22.243))

5.  **Fetch and print the data**:

    Call the ``get_live_flight_positions`` method with your request object. It's good practice to wrap the call in a ``try...except`` block to handle potential errors.

    .. code-block:: python

        try:
            response = service.get_live_flight_positions(request)
            print('Live Flight Positions:')
            print(response)
        except Exception as e:
            print(f'Error: {e}')

Complete Example
================

Here is the complete code example:

.. literalinclude:: ../examples/flight_position_light_example.py
   :language: python
