from datetime import datetime
from decimal import ROUND_HALF_UP, Decimal
from typing import Annotated, List

from pydantic import BaseModel, Field, model_validator

from flight_radar.dtos import (
    CountResponseDto,
    FlightPositionBaseRequestDto,
    FlightPositionLightDto,
    FlightPositionResponseDto,
    GetHistoricFlightPositionCountRequestDto,
    GetHistoricFlightPositionRequestDto,
    GetLiveFlightPositionRequestDto,
)
from flight_radar.enums.enums import DataSources, FlightCategory
from flight_radar.models.common import (
    ConstrainedAirportWithDirectionList,
    ConstrainedRouteList,
    ConstrainedStringList,
)


class FlightPositionBaseRequest(BaseModel):
    """
    Represents the base request for flight position data.
    """
    bounds: tuple[float, float, float, float] | None = None
    flights: ConstrainedStringList | None = None
    callsigns: ConstrainedStringList | None = None
    registrations: ConstrainedStringList | None = None
    painted_as: ConstrainedStringList | None = None
    operating_as: ConstrainedStringList | None = None
    airports: ConstrainedAirportWithDirectionList | None = None
    routes: ConstrainedRouteList | None = None
    aircraft: ConstrainedStringList | None = None
    altitude_ranges: List[tuple[int, int]] | None = None
    squawks: List[str] | None = None
    categories: List[FlightCategory] | None = None
    data_sources: List[DataSources] | None = None
    airspaces: List[str] | None = None
    gspeed: int | tuple[int, int] | None = None

    @model_validator(mode='after')
    def validate(self):
        """
        Validate that at least one filter parameter is provided.
        """
        field_names = list(FlightPositionBaseRequest.model_fields.keys())

        if all(getattr(self, field_name) is None for field_name in field_names):
            raise ValueError('At least one filter parameter must be provided')

        if self.altitude_ranges:
            for altitude_range in self.altitude_ranges:
                if altitude_range[0] < 0:
                    raise ValueError('Altitude range must be greater than 0')
                if altitude_range[0] > altitude_range[1]:
                    raise ValueError('Altitude range must be in ascending order')

        if self.gspeed:
            if isinstance(self.gspeed, tuple):
                if self.gspeed[0] < 0:
                    raise ValueError('Ground speed must be greater than 0')
                if self.gspeed[0] > self.gspeed[1]:
                    raise ValueError('Ground speed must be in ascending order')
            else:
                if self.gspeed < 0:
                    raise ValueError('Ground speed must be greater than 0')

        return self

    def _map_bounds(self):
        if not self.bounds:
            return None

        result = []
        for bound in self.bounds:
            decimal_value = Decimal(str(bound))
            rounded_bound = decimal_value.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
            result.append(str(rounded_bound))

        return ','.join(result)

    def _map_categories(self):
        if not self.categories:
            return None

        categories = [c.value for c in self.categories]
        return ','.join(categories)

    def _map_altitude_ranges(self):
        if not self.altitude_ranges:
            return None

        result = []
        for altitude_range in self.altitude_ranges:
            result.append('-'.join(map(str, altitude_range)))
        return ','.join(result)

    def _map_gspeed(self):
        if not self.gspeed:
            return None

        if isinstance(self.gspeed, tuple):
            return f'{self.gspeed[0]}-{self.gspeed[1]}'

        return str(self.gspeed)

    def _map_data_sources(self):
        if not self.data_sources:
            return None

        data_sources = [ds.value for ds in self.data_sources if ds.value is not None]
        return ','.join(data_sources)

    def to_dto(self) -> FlightPositionBaseRequestDto:
        """
        Converts the request to a DTO.

        Returns:
            A FlightPositionBaseRequestDto object.
        """
        return FlightPositionBaseRequestDto(
            bounds=self._map_bounds(),
            flights=','.join(self.flights) if self.flights else None,
            callsigns=','.join(self.callsigns) if self.callsigns else None,
            registrations=','.join(self.registrations) if self.registrations else None,
            painted_as=','.join(self.painted_as) if self.painted_as else None,
            operating_as=','.join(self.operating_as) if self.operating_as else None,
            airports=','.join(map(str, self.airports)) if self.airports else None,
            routes=','.join(map(str, self.routes)) if self.routes else None,
            aircraft=','.join(self.aircraft) if self.aircraft else None,
            altitude_ranges=self._map_altitude_ranges(),
            squawks=','.join(self.squawks) if self.squawks else None,
            categories=self._map_categories(),
            data_sources=self._map_data_sources(),
            airspaces=','.join(self.airspaces) if self.airspaces else None,
            gspeed=self._map_gspeed(),
        )


class LiveFlightPositionCountRequest(FlightPositionBaseRequest):
    """
    Represents a request for a count of live flight positions.
    """
    pass


MAX_LIMIT = 30000


class LiveFlightPositionRequest(FlightPositionBaseRequest):
    """
    Represents a request for live flight position data.
    """
    limit: Annotated[int, Field(ge=1, le=MAX_LIMIT)] | None = None

    def to_dto(self) -> GetLiveFlightPositionRequestDto:
        """
        Converts the request to a DTO.

        Returns:
            A GetLiveFlightPositionRequestDto object.
        """
        dto = super().to_dto()
        return GetLiveFlightPositionRequestDto(
            **dto.model_dump(),
            limit=self.limit,
        )


class HistoricFlightPositionRequest(FlightPositionBaseRequest):
    """
    Represents a request for historic flight position data.
    """
    timestamp: datetime
    limit: Annotated[int, Field(ge=1, le=MAX_LIMIT)] | None = None

    def to_dto(self) -> GetHistoricFlightPositionRequestDto:
        """
        Converts the request to a DTO.

        Returns:
            A GetHistoricFlightPositionRequestDto object.
        """
        dto = super().to_dto()
        return GetHistoricFlightPositionRequestDto(
            **dto.model_dump(),
            timestamp=int(self.timestamp.timestamp()),
            limit=self.limit,
        )


class HistoricFlightPositionCountRequest(FlightPositionBaseRequest):
    """
    Represents a request for a count of historic flight positions.
    """
    timestamp: datetime = Field(
        description="""Unix timestamp representing the exact point in time for which you want to fetch flight positions.
        The timestamp must be later than May 11, 2016, subject to your subscription plan's limitations.
        Only one timestamp value is accepted; time ranges not supported""",
    )

    def to_dto(self) -> GetHistoricFlightPositionCountRequestDto:
        """
        Converts the request to a DTO.

        Returns:
            A GetHistoricFlightPositionCountRequestDto object.
        """
        dto = super().to_dto()
        return GetHistoricFlightPositionCountRequestDto(
            **dto.model_dump(),
            timestamp=int(self.timestamp.timestamp()),
        )


class FlightPositionLight(BaseModel):
    """
    Represents a light version of a flight's position.
    """
    fr24_id: str = Field(description='Unique identifier assigned by Flightradar24 to the flight leg.')
    hex: str | None = Field(
        description='24 bit Mode-S identifier expressed in hexadecimal format.',
        default=None,
    )
    callsign: str | None = Field(
        description="""Callsign used by Air Traffic Control to denote
        a specific flight (as sent by aircraft transponder).""",
        default=None,
    )
    lat: float = Field(description='Latest latitude expressed in decimal degrees.')
    lon: float = Field(description='Latest longitude expressed in decimal degrees.')
    track: int = Field(
        description="""True track (over ground) expressed in integer degrees as 0-360.
        Please note that 0 can in some cases mean unknown."""
    )
    alt: int = Field(
        description="""Barometric pressure altitude above mean sea level (AMSL)
        reported at a standard atmospheric pressure (1013.25 hPa / 29.92 in. Hg.)
        expressed in feet."""
    )
    gspeed: int = Field(description='Speed relative to the ground expressed in knots.')
    vspeed: int = Field(description='The rate at which the aircraft is ascending or descending in feet per minute.')
    squawk: str = Field(description='4 digit unique identifying code for ATC expressed in octal format.')
    timestamp: datetime = Field(description='Timestamp of the flight position in UTC.')
    source: str = Field(description='Data source of the provided flight position.')

    @staticmethod
    def from_dto(dto: FlightPositionLightDto) -> 'FlightPositionLight':
        """
        Creates a FlightPositionLight object from a FlightPositionLightDto.

        Args:
            dto: The FlightPositionLightDto object.

        Returns:
            A FlightPositionLight object.
        """
        return FlightPositionLight(
            fr24_id=dto.fr24_id,
            hex=dto.hex,
            callsign=dto.callsign,
            lat=dto.lat,
            lon=dto.lon,
            track=dto.track,
            alt=dto.alt,
            gspeed=dto.gspeed,
            vspeed=dto.vspeed,
            squawk=str(dto.squawk),
            timestamp=datetime.fromisoformat(dto.timestamp),
            source=dto.source,
        )


class FlightPosition(FlightPositionLight):
    """
    Represents a flight's position.
    """
    flight: str | None = Field(
        description='Commercial flight number.',
        default=None,
    )
    painted_as: str | None = Field(
        description="ICAO code of the carrier mapped from FR24's internal database.",
        default=None,
    )
    operating_as: str | None = Field(
        description='ICAO code of the airline carrier as derived from flight callsign.',
        default=None,
    )
    orig_iata: str | None = Field(
        description='IATA code for the origin airport.',
        default=None,
    )
    orig_icao: str | None = Field(
        description='ICAO code for the origin airport.',
        default=None,
    )
    dest_iata: str | None = Field(
        description='IATA code for the destination airport.',
        default=None,
    )
    dest_icao: str | None = Field(
        description='ICAO code for the destination airport.',
        default=None,
    )
    eta: datetime | None = Field(
        description='Estimated time of arrival',
        default=None,
    )
    type: str | None = Field(
        description='Aircraft ICAO type code.',
        default=None,
    )
    reg: str | None = Field(
        description='Aircraft registration as matched from Mode-S identifier.',
        default=None,
    )

    @staticmethod
    def from_dto(dto: FlightPositionResponseDto) -> 'FlightPosition':
        """
        Creates a FlightPosition object from a FlightPositionResponseDto.

        Args:
            dto: The FlightPositionResponseDto object.

        Returns:
            A FlightPosition object.
        """
        return FlightPosition(
            fr24_id=dto.fr24_id,
            hex=dto.hex,
            callsign=dto.callsign,
            lat=dto.lat,
            lon=dto.lon,
            track=dto.track,
            alt=dto.alt,
            gspeed=dto.gspeed,
            vspeed=dto.vspeed,
            squawk=str(dto.squawk),
            timestamp=datetime.fromisoformat(dto.timestamp),
            source=dto.source,
            flight=dto.flight,
            painted_as=dto.painted_as,
            operating_as=dto.operating_as,
            orig_iata=dto.orig_iata,
            orig_icao=dto.orig_icao,
            dest_iata=dto.dest_iata,
            dest_icao=dto.dest_icao,
            eta=datetime.fromisoformat(dto.eta) if dto.eta else None,
            type=dto.type,
            reg=dto.reg,
        )


class CountResponse(BaseModel):
    """
    Represents a count of records.
    """
    record_count: int = Field(description='Total number of records matching the query.')

    @staticmethod
    def from_dto(dto: CountResponseDto) -> 'CountResponse':
        """
        Creates a CountResponse object from a CountResponseDto.

        Args:
            dto: The CountResponseDto object.

        Returns:
            A CountResponse object.
        """
        return CountResponse(
            record_count=dto.record_count,
        )
