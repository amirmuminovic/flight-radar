from typing import Union

from pydantic import BaseModel


### Request DTOs
class FlightPositionBaseRequestDto(BaseModel):
    """
    Represents the base request for flight position data.

    Attributes:
        bounds: The geographical bounds.
        flights: A list of flight IDs.
        callsigns: A list of callsigns.
        registrations: A list of registrations.
        painted_as: The painted as airline.
        operating_as: The operating as airline.
        airports: A list of airport ICAO codes.
        routes: A list of routes.
        aircraft: A list of aircraft types.
        altitude_ranges: The altitude ranges.
        squawks: A list of squawk codes.
        categories: A list of aircraft categories.
        data_sources: A list of data sources.
        airspaces: A list of airspaces.
        gspeed: The ground speed range.
    """
    bounds: str | None = None
    flights: str | None = None
    callsigns: str | None = None
    registrations: str | None = None
    painted_as: str | None = None
    operating_as: str | None = None
    airports: str | None = None
    routes: str | None = None
    aircraft: str | None = None
    altitude_ranges: str | None = None
    squawks: str | None = None
    categories: str | None = None
    data_sources: str | None = None
    airspaces: str | None = None
    gspeed: str | None = None


### Response DTOs
class FlightPositionLightDto(BaseModel):
    """
    Represents a light version of a flight's position.

    Attributes:
        fr24_id: The Flightradar24 ID.
        hex: The ICAO hex code.
        callsign: The callsign.
        lat: The latitude.
        lon: The longitude.
        track: The track in degrees.
        alt: The altitude in feet.
        gspeed: The ground speed in knots.
        vspeed: The vertical speed in feet per minute.
        squawk: The squawk code.
        timestamp: The timestamp of the position.
        source: The data source.
    """
    fr24_id: str
    hex: str | None = None
    callsign: str | None = None
    lat: float
    lon: float
    track: int
    alt: int
    gspeed: int
    vspeed: int
    squawk: Union[str, int]
    timestamp: str
    source: str


class FlightPositionResponseDto(FlightPositionLightDto):
    """
    Represents a flight's position.

    Attributes:
        flight: The flight number.
        painted_as: The painted as airline.
        operating_as: The operating as airline.
        orig_iata: The IATA code of the origin airport.
        orig_icao: The ICAO code of the origin airport.
        dest_iata: The IATA code of the destination airport.
        dest_icao: The ICAO code of the destination airport.
        eta: The estimated time of arrival.
        type: The aircraft type.
        reg: The registration number.
    """
    flight: str | None = None
    painted_as: str | None = None
    operating_as: str | None = None
    orig_iata: str | None = None
    orig_icao: str | None = None
    dest_iata: str | None = None
    dest_icao: str | None = None
    eta: str | None = None
    type: str | None = None
    reg: str | None = None


class CountResponseDto(BaseModel):
    """
    Represents a count of records.

    Attributes:
        record_count: The number of records.
    """
    record_count: int
