from typing import Annotated, List, TypeAlias

from pydantic import BaseModel, Field

from flight_radar.enums.enums import Direction

MAX_LIST_LENGTH = 15


ConstrainedStringList: TypeAlias = Annotated[List[str], Field(max_length=MAX_LIST_LENGTH)]


class AirportWithDirection(BaseModel):
    airport: str = Field(description='Airport IATA or ICAO code.')
    direction: Direction | None = Field(
        description='Direction of the flight (inbound or outbound or both).',
        default=None,
    )

    def __str__(self):
        return f'{self.direction.value}:{self.airport}' if self.direction else self.airport


ConstrainedAirportWithDirectionList: TypeAlias = Annotated[
    List[AirportWithDirection], Field(max_length=MAX_LIST_LENGTH)
]


class Route(BaseModel):
    origin: str = Field(description='Origin airport IATA or ICAO code.')
    destination: str = Field(description='Destination airport IATA or ICAO code.')

    def __str__(self):
        return f'{self.origin}-{self.destination}'


ConstrainedRouteList: TypeAlias = Annotated[List[Route], Field(max_length=MAX_LIST_LENGTH)]
