from pydantic import BaseModel

from flight_radar.dtos.flight_position import CountResponseDto


###### Common DTOs ######
class FlightSummaryBaseRequestDto(BaseModel):
    flight_ids: str | None = None
    flight_datetime_from: str | None = None
    flight_datetime_to: str | None = None
    flights: str | None = None
    callsigns: str | None = None
    registrations: str | None = None
    painted_as: str | None = None
    operating_as: str | None = None
    airports: str | None = None
    routes: str | None = None
    aircraft: str | None = None


class FlightSummaryRequestDto(FlightSummaryBaseRequestDto):
    limit: int | None = None
    sort: str | None = None


class FlightSummaryCountRequestDto(FlightSummaryBaseRequestDto):
    pass


class FlightSummaryLightDto(BaseModel):
    fr24_id: str
    flight: str | None = None
    callsign: str | None = None
    operating_as: str | None = None
    painted_as: str | None = None
    type: str | None = None
    reg: str | None = None
    orig_icao: str | None = None
    datetime_takeoff: str | None = None
    dest_icao: str | None = None
    datetime_landed: str | None = None
    hex: str | None = None
    first_seen: str | None = None
    last_seen: str | None = None
    flight_ended: bool | None = None


class FlightSummaryDto(FlightSummaryLightDto):
    orig_iata: str | None = None
    runway_takeoff: str | None = None
    dest_iata: str | None = None
    dest_icao_actual: str | None = None
    dest_iata_actual: str | None = None
    runway_landed: str | None = None
    flight_time: float | None = None
    actual_distance: float | None = None
    circle_distance: float | None = None


###### Request DTOs ######
class GetFlightSummaryLightRequestDto(FlightSummaryRequestDto):
    pass


class GetFlightSummaryRequestDto(FlightSummaryRequestDto):
    pass


class GetFlightSummaryCountRequestDto(FlightSummaryCountRequestDto):
    pass


###### Response DTOs ######
class GetFlightSummaryLightResponseDto(BaseModel):
    data: list[FlightSummaryLightDto]


class GetFlightSummaryResponseDto(BaseModel):
    data: list[FlightSummaryDto]


class GetFlightSummaryCountResponseDto(CountResponseDto):
    pass
