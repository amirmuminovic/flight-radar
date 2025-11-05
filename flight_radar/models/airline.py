from pydantic import BaseModel, Field

from flight_radar.dtos import GetAirlineLightResponseDto


class Airline(BaseModel):
    """
    Represents an airline.

    Attributes:
        icao: The ICAO code of the airline.
        name: The name of the airline.
        iata: The IATA code of the airline.
    """
    icao: str = Field(description='Airline ICAO code')
    name: str = Field(description='Name of the airline')
    iata: str | None = Field(description='Airline IATA code', default=None)

    @staticmethod
    def from_dto(dto: GetAirlineLightResponseDto) -> 'Airline':
        """
        Creates an Airline object from a GetAirlineLightResponseDto.

        Args:
            dto: The GetAirlineLightResponseDto object.

        Returns:
            An Airline object.
        """
        return Airline(
            icao=dto.icao,
            name=dto.name,
            iata=dto.iata,
        )
