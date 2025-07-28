from pydantic import BaseModel

from flight_radar.dtos.flight_position import (
    CountResponseDto,
    FlightPositionBaseRequestDto,
    FlightPositionLightDto,
    FlightPositionResponseDto,
)


###### Common DTOs ######
class GetHistoricFlightPositionBaseRequestDto(FlightPositionBaseRequestDto):
    timestamp: int


class GetHistoricFlightPositionWithLimitRequestDto(GetHistoricFlightPositionBaseRequestDto):
    limit: int | None = None


###### Request DTOs ######
class GetHistoricFlightPositionLightRequestDto(GetHistoricFlightPositionWithLimitRequestDto):
    pass


class GetHistoricFlightPositionRequestDto(GetHistoricFlightPositionWithLimitRequestDto):
    pass


class GetHistoricFlightPositionCountRequestDto(GetHistoricFlightPositionBaseRequestDto):
    pass


###### Response DTOs ######
class GetHistoricFlightPositionLightResponseDto(BaseModel):
    data: list[FlightPositionLightDto]


class GetHistoricFlightPositionResponseDto(BaseModel):
    data: list[FlightPositionResponseDto]


class GetHistoricFlightPositionCountResponseDto(CountResponseDto):
    pass
