.. _calculate_farthest_flight_arriving_at_airport_example:

*******************************************************************
Calculate the Farthest Flight Arriving at a Specific Airport
*******************************************************************

This guide demonstrates how to use the Flight Radar SDK to find the farthest flight currently en route to a specific airport (in this case, Stockholm Arlanda Airport, ESSA).

Prerequisites
=============

*   An API token from FlightRadar24.
*   The ``flight-radar`` and ``geopy`` libraries installed.

How It Works
============

The script is divided into three main steps:

1.  **Retrieve Arriving Flights**: It first queries the FlightRadar24 API to get a list of all flights that are currently inbound to the specified airport (``ESSA``).

2.  **Get Airport Coordinates**: It then fetches the geographical coordinates (latitude and longitude) of the destination airport.

3.  **Calculate and Compare Distances**: Finally, it iterates through each flight, calculates the great-circle distance from the flight's current position to the destination airport, and identifies which flight is the farthest away.

Step-by-Step Breakdown
======================

**Step 1: Retrieve Flights Arriving at ESSA**

The script sends a request to the API, filtering for flights with a destination of ``ESSA``.

.. code-block:: python

    request = LiveFlightPositionRequest(
        airports=[
            AirportWithDirection(
                airport='ESSA',
                direction=Direction.INBOUND,
            )
        ]
    )
    response = service.get_live_flight_positions(request)

**Step 2: Retrieve Airport Coordinates for ESSA**

To calculate the distance, we need the exact coordinates of the destination.

.. code-block:: python

    airport_response = service.get_airports('ESSA')
    destination_coords = (airport_response.lat, airport_response.lon)

**Step 3: Calculate the Farthest Flight**

The script uses the ``geopy`` library to calculate the distance and finds the flight with the maximum distance from ESSA.

.. code-block:: python

    farthest_flight = None
    max_distance = 0

    for flight in sorted_flights:
        origin_coords = (flight.lat, flight.lon)
        distance = calculate_distance(origin_coords, destination_coords)
        if distance > max_distance:
            max_distance = distance
            farthest_flight = flight

Complete Example
================

Here is the complete code for the example. You can run this script to see it in action.

.. literalinclude:: ../examples/calculate_farthest_flight_arriving_at_essa.py
   :language: python
