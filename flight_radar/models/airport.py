from pydantic import BaseModel, Field

from flight_radar.dtos import (
    CountryDto,
    GetAirportLightResponseDto,
    GetAirportResponseDto,
    TimezoneDto,
    RunwayDto,
    SurfaceDto,
)


class Country(BaseModel):
    code: str = Field(description='ISO 3166-1 alpha-2 code of the country')
    name: str = Field(description='Name of the country')

    @staticmethod
    def from_dto(dto: CountryDto) -> 'Country':
        return Country(
            code=dto.code,
            name=dto.name,
        )


class Timezone(BaseModel):
    name: str = Field(description='Name of the timezone')
    offset: int = Field(description='Offset from UTC in seconds')

    @staticmethod
    def from_dto(dto: TimezoneDto) -> 'Timezone':
        return Timezone(
            name=dto.name,
            offset=dto.offset,
        )


class Surface(BaseModel):
    type: str = Field(
        description='Surface type code (e.g., ASPHH for asphalt).',
        examples=['ASPHH'],
    )
    description: str = Field(
        description='Human-readable surface description.',
        examples=['Asphalt'],
    )

    @staticmethod
    def from_dto(dto: SurfaceDto) -> 'Surface':
        return Surface(
            type=dto.type,
            description=dto.description,
        )


class Runway(BaseModel):
    designator: str = Field(description='Runway designator (e.g., 18R/36L).')
    heading: float = Field(description='Runway heading in decimal degrees.')
    length: int = Field(description='Runway length in feet.')
    width: int = Field(description='Runway width in feet.')
    elevation: int = Field(description='Runway elevation in feet.')
    thr_coordinates: tuple[float, float] = Field(
        description='Threshold coordinates (latitude, longitude) in decimal degrees.'
    )
    surface: Surface = Field(description='Surface type at the runway')

    @staticmethod
    def from_dto(dto: RunwayDto) -> 'Runway':
        return Runway(
            designator=dto.designator,
            heading=dto.heading,
            length=dto.length,
            width=dto.width,
            elevation=dto.elevation,
            thr_coordinates=(dto.thr_coordinates[0], dto.thr_coordinates[1]),
            surface=Surface.from_dto(dto.surface),
        )


class AirportLight(BaseModel):
    icao: str = Field(description='Airport ICAO code')
    name: str | None = Field(description='Airport name', default=None)
    iata: str | None = Field(description='Airport IATA code', default=None)

    @staticmethod
    def from_dto(dto: GetAirportLightResponseDto) -> 'AirportLight':
        return AirportLight(
            icao=dto.icao,
            name=dto.name,
            iata=dto.iata,
        )


class Airport(AirportLight):
    lon: float = Field(description='Longitude expressed in decimal degrees')
    lat: float = Field(description='Latitude expressed in decimal degrees')
    elevation: int = Field(description='Airport elevation in feet')
    city: str = Field(description='City of airport')
    country: Country = Field(description='Country')
    timezone: Timezone = Field(description='Timezone')
    state: str | None = Field(
        description='State where the airport is located. Only available for US, Canada, Brazil and Australia.',
        default=None,
    )
    runways: list[Runway] = Field(description='List of runways at the airport')

    @staticmethod
    def from_dto(dto: GetAirportResponseDto) -> 'Airport':
        return Airport(
            icao=dto.icao,
            name=dto.name,
            iata=dto.iata,
            lon=dto.lon,
            lat=dto.lat,
            elevation=dto.elevation,
            city=dto.city,
            country=Country.from_dto(dto.country),
            timezone=Timezone.from_dto(dto.timezone),
            state=dto.state,
            runways=[Runway.from_dto(runway) for runway in dto.runways],
        )
