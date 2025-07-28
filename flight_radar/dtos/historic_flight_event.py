from pydantic import BaseModel


class HistoricFlightEventRequestDto(BaseModel):
    flight_ids: str
    event_types: str | None = None


class HistoricFlightEventDetailsDto(BaseModel):
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
    type: str
    timestamp: str
    lat: float | None = None
    lon: float | None = None
    alt: int | None = None
    gspeed: int | None = None
    details: HistoricFlightEventDetailsDto | None = None


class HistoricFlightEventBaseResponseDto(BaseModel):
    fr24_id: str
    callsign: str
    hex: str
    events: list[HistoricFlightEventDto]


class HistoricFlightEventLightResponseDto(BaseModel):
    data: list[HistoricFlightEventBaseResponseDto]


class HistoricFlightEventResponseEntryDto(HistoricFlightEventBaseResponseDto):
    painted_as: str
    operating_as: str
    orig_icao: str
    orig_iata: str
    dest_iata: str
    dest_icao: str


class HistoricFlightEventResponseDto(BaseModel):
    data: list[HistoricFlightEventResponseEntryDto]
