from pydantic import BaseModel


class GetAirlineLightResponseDto(BaseModel):
    icao: str
    name: str
    iata: str | None = None
