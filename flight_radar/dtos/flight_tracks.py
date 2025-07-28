from pydantic import BaseModel


###### Common DTOs ######
class FlightTrackDto(BaseModel):
    timestamp: str
    lat: float
    lon: float
    alt: int
    gspeed: int
    vspeed: int
    track: int
    squawk: str
    source: str
    callsign: str | None = None


###### Request DTOs ######
class GetFlightTracksBaseRequestDto(BaseModel):
    flight_id: str


###### Response DTOs ######
class GetFlightTracksResponseDto(BaseModel):
    tracks: list[FlightTrackDto]
    fr24_id: str
