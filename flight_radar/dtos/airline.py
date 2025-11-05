from pydantic import BaseModel


class GetAirlineLightResponseDto(BaseModel):
    """
    Represents a light version of an airline.

    Attributes:
        icao: The ICAO code of the airline.
        name: The name of the airline.
        iata: The IATA code of the airline.
    """
    icao: str
    name: str
    iata: str | None = None
