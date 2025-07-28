from pydantic import BaseModel


###### Common DTOs ######
class CountryDto(BaseModel):
    code: str
    name: str


class TimezoneDto(BaseModel):
    name: str
    offset: int


class SurfaceDto(BaseModel):
    type: str
    description: str


class RunwayDto(BaseModel):
    designator: str
    heading: float
    length: int
    width: int
    elevation: int
    thr_coordinates: list[float]
    surface: SurfaceDto


###### Response DTOs ######
class GetAirportLightResponseDto(BaseModel):
    icao: str
    name: str | None = None
    iata: str | None = None


class GetAirportResponseDto(GetAirportLightResponseDto):
    lon: float
    lat: float
    elevation: int
    city: str
    country: CountryDto
    timezone: TimezoneDto
    state: str | None = None
    runways: list[RunwayDto]
