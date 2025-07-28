.. FlightRadar24 Python SDK documentation master file, created by
   sphinx-quickstart on Fri Jul 11 07:23:17 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

##################################
FlightRadar24 Python SDK
##################################

Welcome to the official documentation for the FlightRadar24 Python SDK, an unofficial wrapper for the FlightRadar24 API.

This SDK provides a streamlined, developer-friendly interface to access the vast amount of flight data from FlightRadar24. Whether you're a hobbyist building a flight tracking application, a data scientist analyzing air traffic patterns, or a developer integrating flight data into your services, this SDK is designed to simplify your interaction with the API.

Features
========

- **Live Flight Tracking**: Retrieve real-time positions of flights globally or within specific geographical bounds.
- **Airport Data**: Find all flights currently inbound or outbound for a particular airport.
- **Detailed Flight Information**: Access comprehensive details for a specific flight, including its track, speed, altitude, and estimated time of arrival.
- **Aircraft and Airline Information**: Look up details about airports (like coordinates) and airlines.
- **API Usage Monitoring**: Track your API consumption to manage usage effectively.
- **Historical Data**: Query past flight events and positional data.

Prerequisites
=============

- Python 3.10 or higher
- A FlightRadar24 API key

Installation
============

To install the SDK, run the following command:

.. code-block:: bash

   pip install flight-radar

Quickstart
==========

Here's a simple example of how to get started:

.. code-block:: python

   from flight_radar.models import LiveFlightPositionRequest
   from flight_radar import get_flight_radar_client

   # Initialize the client with your API key
   client = get_flight_radar_client(
      api_key="your_api_key",
      base_url="https://api.flightradar24.com/api/v1",
   )

   # Define the geographical bounds for the flight search
   request = LiveFlightPositionRequest(
       bounds=(40.7128, -74.0060, 40.7000, -74.0200)
   )

   # Retrieve live flight positions
   positions = client.get_live_flight_positions(request)

   for position in positions:
       print(f"Flight {position.callsign} is at {position.latitude}, {position.longitude}")

Guides
======

This section provides practical guides for common use cases.

.. toctree::
   :maxdepth: 1
   :caption: Guides

   flight_position_light_example
   alert_when_flight_enters_circular_area_example
   calculate_fartherst_flight_arriving_at_airport_example

.. _api-reference:

API Reference
=============

The API reference provides detailed information on all the available modules, classes, and methods.

.. toctree::
   :maxdepth: 3
   :caption: Client

   flight_radar_client

.. toctree::
   :maxdepth: 1
   :caption: Data Models

   models_airline
   models_airport
   models_api_usage
   models_common
   models_flight_position
   models_flight_summary
   models_flight_track
   models_historic_flight_event
