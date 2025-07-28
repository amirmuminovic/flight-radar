from typing import Union

from pydantic import BaseModel


### Request DTOs
class FlightPositionBaseRequestDto(BaseModel):
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
    record_count: int
