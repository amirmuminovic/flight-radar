from pydantic import BaseModel


###### Common DTOs ######
class FlightTrackDto(BaseModel):
    """
    Represents a flight track point.

    Attributes:
        timestamp: The timestamp of the track point.
        lat: The latitude of the track point.
        lon: The longitude of the track point.
        alt: The altitude of the track point in feet.
        gspeed: The ground speed of the track point in knots.
        vspeed: The vertical speed of the track point in feet per minute.
        track: The track of the track point in degrees.
        squawk: The squawk code of the track point.
        source: The source of the track point.
        callsign: The callsign of the track point.
    """
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
    """
    Represents the base request for flight tracks.

    Attributes:
        flight_id: The ID of the flight.
    """
    flight_id: str


###### Response DTOs ######
class GetFlightTracksResponseDto(BaseModel):
    """
    Represents the response for flight tracks.

    Attributes:
        tracks: A list of flight track points.
        fr24_id: The Flightradar24 ID of the flight.
    """
    tracks: list[FlightTrackDto]
    fr24_id: str
