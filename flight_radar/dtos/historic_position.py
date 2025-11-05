from pydantic import BaseModel

from flight_radar.dtos.flight_position import (
    CountResponseDto,
    FlightPositionBaseRequestDto,
    FlightPositionLightDto,
    FlightPositionResponseDto,
)


###### Common DTOs ######
class GetHistoricFlightPositionBaseRequestDto(FlightPositionBaseRequestDto):
    """
    Represents the base request for historic flight position data.

    Attributes:
        timestamp: The timestamp for which to retrieve data.
    """
    timestamp: int


class GetHistoricFlightPositionWithLimitRequestDto(GetHistoricFlightPositionBaseRequestDto):
    """
    Represents a request for historic flight position data with a limit.

    Attributes:
        limit: The maximum number of records to return.
    """
    limit: int | None = None


###### Request DTOs ######
class GetHistoricFlightPositionLightRequestDto(GetHistoricFlightPositionWithLimitRequestDto):
    """
    Represents a request for a light version of historic flight position data.
    """
    pass


class GetHistoricFlightPositionRequestDto(GetHistoricFlightPositionWithLimitRequestDto):
    """
    Represents a request for historic flight position data.
    """
    pass


class GetHistoricFlightPositionCountRequestDto(GetHistoricFlightPositionBaseRequestDto):
    """
    Represents a request for a count of historic flight position data.
    """
    pass


###### Response DTOs ######
class GetHistoricFlightPositionLightResponseDto(BaseModel):
    """
    Represents the response for a light version of historic flight position data.

    Attributes:
        data: A list of light flight positions.
    """
    data: list[FlightPositionLightDto]


class GetHistoricFlightPositionResponseDto(BaseModel):
    """
    Represents the response for historic flight position data.

    Attributes:
        data: A list of flight positions.
    """
    data: list[FlightPositionResponseDto]


class GetHistoricFlightPositionCountResponseDto(CountResponseDto):
    """
    Represents the response for a count of historic flight position data.
    """
    pass
