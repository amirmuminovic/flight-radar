from pydantic import BaseModel

from flight_radar.dtos.flight_position import (
    CountResponseDto,
    FlightPositionBaseRequestDto,
    FlightPositionLightDto,
    FlightPositionResponseDto,
)


###### Common DTOs ######
class LiveFlightPositionWithLimitRequestDto(FlightPositionBaseRequestDto):
    """
    Represents a request for live flight position data with a limit.

    Attributes:
        limit: The maximum number of records to return.
    """
    limit: int | None = None


###### Request DTOs ######
class GetLiveFlightPositionCountRequestDto(FlightPositionBaseRequestDto):
    """
    Represents a request for a count of live flight position data.
    """
    pass


class GetLiveFlightPositionRequestDto(LiveFlightPositionWithLimitRequestDto):
    """
    Represents a request for live flight position data.
    """
    pass


###### Response DTOs ######
class GetLiveFlightPositionLightResponseDto(BaseModel):
    """
    Represents the response for a light version of live flight position data.

    Attributes:
        data: A list of light flight positions.
    """
    data: list[FlightPositionLightDto]


class GetLiveFlightPositionResponseDto(BaseModel):
    """
    Represents the response for live flight position data.

    Attributes:
        data: A list of flight positions.
    """
    data: list[FlightPositionResponseDto]


class GetLiveFlightPositionCountResponseDto(CountResponseDto):
    """
    Represents the response for a count of live flight position data.
    """
    pass
