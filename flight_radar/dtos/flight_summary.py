from pydantic import BaseModel

from flight_radar.dtos.flight_position import CountResponseDto


###### Common DTOs ######
class FlightSummaryBaseRequestDto(BaseModel):
    """
    Represents the base request for flight summary data.

    Attributes:
        flight_ids: A list of flight IDs.
        flight_datetime_from: The start of the flight datetime range.
        flight_datetime_to: The end of the flight datetime range.
        flights: A list of flight numbers.
        callsigns: A list of callsigns.
        registrations: A list of registrations.
        painted_as: The painted as airline.
        operating_as: The operating as airline.
        airports: A list of airport ICAO codes.
        routes: A list of routes.
        aircraft: A list of aircraft types.
    """
    flight_ids: str | None = None
    flight_datetime_from: str | None = None
    flight_datetime_to: str | None = None
    flights: str | None = None
    callsigns: str | None = None
    registrations: str | None = None
    painted_as: str | None = None
    operating_as: str | None = None
    airports: str | None = None
    routes: str | None = None
    aircraft: str | None = None


class FlightSummaryRequestDto(FlightSummaryBaseRequestDto):
    """
    Represents a request for flight summary data.

    Attributes:
        limit: The maximum number of records to return.
        sort: The field to sort by.
    """
    limit: int | None = None
    sort: str | None = None


class FlightSummaryCountRequestDto(FlightSummaryBaseRequestDto):
    """
    Represents a request for a count of flight summary data.
    """
    pass


class FlightSummaryLightDto(BaseModel):
    """
    Represents a light version of a flight summary.

    Attributes:
        fr24_id: The Flightradar24 ID.
        flight: The flight number.
        callsign: The callsign.
        operating_as: The operating as airline.
        painted_as: The painted as airline.
        type: The aircraft type.
        reg: The registration number.
        orig_icao: The ICAO code of the origin airport.
        datetime_takeoff: The takeoff datetime.
        dest_icao: The ICAO code of the destination airport.
        datetime_landed: The landed datetime.
        hex: The ICAO hex code.
        first_seen: The first seen datetime.
        last_seen: The last seen datetime.
        flight_ended: Whether the flight has ended.
    """
    fr24_id: str
    flight: str | None = None
    callsign: str | None = None
    operating_as: str | None = None
    painted_as: str | None = None
    type: str | None = None
    reg: str | None = None
    orig_icao: str | None = None
    datetime_takeoff: str | None = None
    dest_icao: str | None = None
    datetime_landed: str | None = None
    hex: str | None = None
    first_seen: str | None = None
    last_seen: str | None = None
    flight_ended: bool | None = None


class FlightSummaryDto(FlightSummaryLightDto):
    """
    Represents a flight summary.

    Attributes:
        orig_iata: The IATA code of the origin airport.
        runway_takeoff: The takeoff runway.
        dest_iata: The IATA code of the destination airport.
        dest_icao_actual: The actual ICAO code of the destination airport.
        dest_iata_actual: The actual IATA code of the destination airport.
        runway_landed: The landed runway.
        flight_time: The flight time in seconds.
        actual_distance: The actual distance in miles.
        circle_distance: The circle distance in miles.
    """
    orig_iata: str | None = None
    runway_takeoff: str | None = None
    dest_iata: str | None = None
    dest_icao_actual: str | None = None
    dest_iata_actual: str | None = None
    runway_landed: str | None = None
    flight_time: float | None = None
    actual_distance: float | None = None
    circle_distance: float | None = None


###### Request DTOs ######
class GetFlightSummaryLightRequestDto(FlightSummaryRequestDto):
    """
    Represents a request for a light version of flight summary data.
    """
    pass


class GetFlightSummaryRequestDto(FlightSummaryRequestDto):
    """
    Represents a request for flight summary data.
    """
    pass


class GetFlightSummaryCountRequestDto(FlightSummaryCountRequestDto):
    """
    Represents a request for a count of flight summary data.
    """
    pass


###### Response DTOs ######
class GetFlightSummaryLightResponseDto(BaseModel):
    """
    Represents the response for a light version of flight summary data.

    Attributes:
        data: A list of light flight summaries.
    """
    data: list[FlightSummaryLightDto]


class GetFlightSummaryResponseDto(BaseModel):
    """
    Represents the response for flight summary data.

    Attributes:
        data: A list of flight summaries.
    """
    data: list[FlightSummaryDto]


class GetFlightSummaryCountResponseDto(CountResponseDto):
    """
    Represents the response for a count of flight summary data.
    """
    pass
