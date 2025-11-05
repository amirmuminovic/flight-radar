from pydantic import BaseModel


class HistoricFlightEventRequestDto(BaseModel):
    """
    Represents a request for historic flight events.

    Attributes:
        flight_ids: A list of flight IDs.
        event_types: The types of events to retrieve.
    """
    flight_ids: str
    event_types: str | None = None


class HistoricFlightEventDetailsDto(BaseModel):
    """
    Represents the details of a historic flight event.

    Attributes:
        gate_ident: The gate identifier.
        gate_lat: The latitude of the gate.
        gate_lon: The longitude of the gate.
        takeoff_runway: The takeoff runway.
        landed_icao: The ICAO code of the landed airport.
        landed_runway: The landed runway.
        exited_airspace: The exited airspace.
        exited_airspace_id: The ID of the exited airspace.
        entered_airspace: The entered airspace.
        entered_airspace_id: The ID of the entered airspace.
    """
    gate_ident: str | None = None
    gate_lat: float | None = None
    gate_lon: float | None = None
    takeoff_runway: str | None = None
    landed_icao: str | None = None
    landed_runway: str | None = None
    exited_airspace: str | None = None
    exited_airspace_id: str | None = None
    entered_airspace: str | None = None
    entered_airspace_id: str | None = None


class HistoricFlightEventDto(BaseModel):
    """
    Represents a historic flight event.

    Attributes:
        type: The type of the event.
        timestamp: The timestamp of the event.
        lat: The latitude of the event.
        lon: The longitude of the event.
        alt: The altitude of the event in feet.
        gspeed: The ground speed of the event in knots.
        details: The details of the event.
    """
    type: str
    timestamp: str
    lat: float | None = None
    lon: float | None = None
    alt: int | None = None
    gspeed: int | None = None
    details: HistoricFlightEventDetailsDto | None = None


class HistoricFlightEventBaseResponseDto(BaseModel):
    """
    Represents the base response for historic flight events.

    Attributes:
        fr24_id: The Flightradar24 ID of the flight.
        callsign: The callsign of the flight.
        hex: The ICAO hex code of the flight.
        events: A list of historic flight events.
    """
    fr24_id: str
    callsign: str
    hex: str
    events: list[HistoricFlightEventDto]


class HistoricFlightEventLightResponseDto(BaseModel):
    """
    Represents the light response for historic flight events.

    Attributes:
        data: A list of historic flight event base responses.
    """
    data: list[HistoricFlightEventBaseResponseDto]


class HistoricFlightEventResponseEntryDto(HistoricFlightEventBaseResponseDto):
    """
    Represents an entry in the response for historic flight events.

    Attributes:
        painted_as: The painted as airline.
        operating_as: The operating as airline.
        orig_icao: The ICAO code of the origin airport.
        orig_iata: The IATA code of the origin airport.
        dest_iata: The IATA code of the destination airport.
        dest_icao: The ICAO code of the destination airport.
    """
    painted_as: str
    operating_as: str
    orig_icao: str
    orig_iata: str
    dest_iata: str
    dest_icao: str


class HistoricFlightEventResponseDto(BaseModel):
    """
    Represents the response for historic flight events.

    Attributes:
        data: A list of historic flight event response entries.
    """
    data: list[HistoricFlightEventResponseEntryDto]
