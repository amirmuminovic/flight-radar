from pydantic import BaseModel

from flight_radar.dtos.flight_position import (
    CountResponseDto,
    FlightPositionBaseRequestDto,
    FlightPositionLightDto,
    FlightPositionResponseDto,
)


###### Common DTOs ######
class LiveFlightPositionWithLimitRequestDto(FlightPositionBaseRequestDto):
    limit: int | None = None


###### Request DTOs ######
class GetLiveFlightPositionCountRequestDto(FlightPositionBaseRequestDto):
    pass


class GetLiveFlightPositionRequestDto(LiveFlightPositionWithLimitRequestDto):
    pass


###### Response DTOs ######
class GetLiveFlightPositionLightResponseDto(BaseModel):
    data: list[FlightPositionLightDto]


class GetLiveFlightPositionResponseDto(BaseModel):
    data: list[FlightPositionResponseDto]


class GetLiveFlightPositionCountResponseDto(CountResponseDto):
    pass
