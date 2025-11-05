from pydantic import BaseModel


###### Common DTOs ######
class CountryDto(BaseModel):
    """
    Represents a country.

    Attributes:
        code: The country code.
        name: The name of the country.
    """
    code: str
    name: str


class TimezoneDto(BaseModel):
    """
    Represents a timezone.

    Attributes:
        name: The name of the timezone.
        offset: The timezone offset.
    """
    name: str
    offset: int


class SurfaceDto(BaseModel):
    """
    Represents a runway surface.

    Attributes:
        type: The type of the surface.
        description: The description of the surface.
    """
    type: str
    description: str


class RunwayDto(BaseModel):
    """
    Represents a runway.

    Attributes:
        designator: The designator of the runway.
        heading: The heading of the runway.
        length: The length of the runway.
        width: The width of the runway.
        elevation: The elevation of the runway.
        thr_coordinates: The coordinates of the runway threshold.
        surface: The surface of the runway.
    """
    designator: str
    heading: float
    length: int
    width: int
    elevation: int
    thr_coordinates: list[float]
    surface: SurfaceDto


###### Response DTOs ######
class GetAirportLightResponseDto(BaseModel):
    """
    Represents a light version of an airport.

    Attributes:
        icao: The ICAO code of the airport.
        name: The name of the airport.
        iata: The IATA code of the airport.
    """
    icao: str
    name: str | None = None
    iata: str | None = None


class GetAirportResponseDto(GetAirportLightResponseDto):
    """
    Represents an airport.

    Attributes:
        lon: The longitude of the airport.
        lat: The latitude of the airport.
        elevation: The elevation of the airport.
        city: The city of the airport.
        country: The country of the airport.
        timezone: The timezone of the airport.
        state: The state of the airport.
        runways: The runways of the airport.
    """
    lon: float
    lat: float
    elevation: int
    city: str
    country: CountryDto
    timezone: TimezoneDto
    state: str | None = None
    runways: list[RunwayDto]
