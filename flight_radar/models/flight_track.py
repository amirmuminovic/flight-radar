from datetime import datetime
from pydantic import BaseModel, Field

from flight_radar.dtos import FlightTrackDto, GetFlightTracksBaseRequestDto


class FlightTrackRequest(BaseModel):
    flight_id: str = Field(description='Unique identifier assigned by Flightradar24 to the flight leg.')

    def to_dto(self) -> GetFlightTracksBaseRequestDto:
        return GetFlightTracksBaseRequestDto(
            flight_id=self.flight_id,
        )


class FlightTrack(BaseModel):
    timestamp: datetime = Field(description='Timestamp of the flight position expressed in UTC (ISO 8601 date format).')
    latitude: float = Field(description='Latest latitude expressed in decimal degrees')
    longitude: float = Field(description='Latest longitude expressed in decimal degrees')
    altitude: int = Field(
        description="""Barometric pressure altitude above mean sea level (AMSL)
        reported at a standard atmospheric pressure (1013.25 hPa / 29.92 in. Hg.)
        expressed in feet."""
    )
    gspeed: int = Field(description='Speed relative to the ground expressed in knots.')
    vspeed: int = Field(
        description="""The rate at which the aircraft is ascending or
        descending in feet per minute."""
    )
    track: int = Field(
        description="""True track (over ground) expressed in integer degrees as 0-360.
        Please note that 0 can in some cases mean unknown."""
    )
    squawk: str = Field(description='4 digit unique identifying code for ATC expressed in octal format.')
    callsign: str = Field(
        description="""The last known callsign used by Air Traffic Control to denote a
        specific flight, as sent by the aircraft transponder. This callsign is
        consistent across all reported positions."""
    )
    source: str = Field(description='Data source of the provided flight position.')

    @staticmethod
    def from_dto(dto: FlightTrackDto) -> 'FlightTrack':
        return FlightTrack(
            timestamp=datetime.fromisoformat(dto.timestamp),
            latitude=dto.lat,
            longitude=dto.lon,
            altitude=dto.alt,
            gspeed=dto.gspeed,
            vspeed=dto.vspeed,
            track=dto.track,
            squawk=dto.squawk,
            callsign=dto.callsign if dto.callsign else '',
            source=dto.source,
        )
