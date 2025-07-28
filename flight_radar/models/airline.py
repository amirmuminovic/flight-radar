from pydantic import BaseModel, Field

from flight_radar.dtos import GetAirlineLightResponseDto


class Airline(BaseModel):
    icao: str = Field(description='Airline ICAO code')
    name: str = Field(description='Name of the airline')
    iata: str | None = Field(description='Airline IATA code', default=None)

    @staticmethod
    def from_dto(dto: GetAirlineLightResponseDto) -> 'Airline':
        return Airline(
            icao=dto.icao,
            name=dto.name,
            iata=dto.iata,
        )
