.. _alert_when_flight_enters_circular_area_example:

***************************************************
Alert When a Flight Enters a Circular Area
***************************************************

This guide explains how to use the Flight Radar SDK to monitor flights and receive alerts when they enter a predefined circular geographical area.

Prerequisites
=============

*   An API token from FlightRadar24.
*   The ``flight-radar`` library installed.

Configuration
=============

Before running the script, you need to configure several parameters:

*   ``API_TOKEN``: Your personal FlightRadar24 API token.
*   ``CENTER_LAT`` & ``CENTER_LON``: The latitude and longitude for the center of your monitoring circle (e.g., a city or a specific point of interest).
*   ``RADIUS_KM``: The radius of the circular area in kilometers.
*   ``POLLING_INTERVAL``: The time in seconds between each check for new flight data.

.. code-block:: python

    # Configuration Parameters
    API_TOKEN = 'your_api_token_here'  # Replace with your actual FR24 API token
    BASE_URL = 'https://fr24api.flightradar24.com/api'
    CENTER_LAT = 52.5200  # Latitude for Berlin
    CENTER_LON = 13.4050  # Longitude for Berlin
    RADIUS_KM = 50  # Radius in kilometers
    POLLING_INTERVAL = 5  # Time between API calls in seconds

How It Works
============

The script performs the following steps in a continuous loop:

1.  **Fetches Flight Data**: It calls the FlightRadar24 API to get live flight positions within a broad geographical area defined around your center point.
2.  **Calculates Distance**: For each flight, it calculates the distance from the center of your defined circle using the Haversine formula.
3.  **Checks Location**: It checks if the calculated distance is within the specified radius.
4.  **Sends Alerts**: If a flight is inside the circle and has not been alerted before, it triggers an alert and adds the flight to a set of alerted flights to avoid duplicate notifications.
5.  **Waits**: It waits for the duration of ``POLLING_INTERVAL`` before repeating the process.

Complete Example
================

Here is the complete code for the example. You can run this script directly to start monitoring flights.

.. literalinclude:: ../examples/alert_when_flight_enters_circular_area.py
   :language: python
