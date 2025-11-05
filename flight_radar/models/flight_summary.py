from datetime import datetime, timedelta, timezone
from typing import Annotated

from pydantic import BaseModel, Field, model_validator

from flight_radar.dtos import (
    FlightSummaryBaseRequestDto,
    FlightSummaryDto,
    FlightSummaryLightDto,
    GetFlightSummaryRequestDto,
)
from flight_radar.enums.enums import Sort
from flight_radar.models.common import (
    ConstrainedAirportWithDirectionList,
    ConstrainedRouteList,
    ConstrainedStringList,
)


class FlightSummaryBaseRequest(BaseModel):
    """
    Represents the base request for flight summary data.
    """
    flight_ids: ConstrainedStringList | None = Field(
        description='fr24_ids (maximum 15 IDs). Cannot be combined with flight_datetime',
        default=None,
    )
    flight_datetime_from: datetime | None = Field(
        description="""Flight date lower range, uses first_seen.
        Cannot be combined with flight_ids. The maximum permitted date range is 14 days.""",
        default=None,
    )
    flight_datetime_to: datetime | None = Field(
        description="""Flight date upper range, uses last_seen.
        Cannot be combined with flight_ids. The maximum permitted date range is 14 days.""",
        default=None,
    )
    flights: ConstrainedStringList | None = Field(
        description='Flight numbers (max 15).',
        default=None,
    )
    callsigns: ConstrainedStringList | None = Field(
        description='Flight callsigns (max 15).',
        default=None,
    )
    registrations: ConstrainedStringList | None = Field(
        description='Aircraft registration numbers (max 15).',
        default=None,
    )
    painted_as: ConstrainedStringList | None = Field(
        description="""Aircraft painted in an airline's livery, identified by ICAO code,
        but not necessarily operated by that airline, such as a regional airline operating a flight for a larger airline
        (max 15).""",
        default=None,
    )
    operating_as: ConstrainedStringList | None = Field(
        description="""Aircraft operating under an airline's call sign, identified by ICAO code,
        but not necessarily an aircraft belonging to that airline, such as an aircraft on lease from another airline
        (max 15).""",
        default=None,
    )
    airports: ConstrainedAirportWithDirectionList | None = Field(
        description='Airports (comma-separated values, max 15).',
        default=None,
    )
    routes: ConstrainedRouteList | None = Field(
        description="""Flights between different airports or countries.
        Airports specified by IATA or ICAO codes or countries specified by ISO 3166-1 alpha-2 codes (max 15).""",
        default=None,
    )
    aircraft: ConstrainedStringList | None = Field(
        description='Aircraft ICAO type codes (comma-separated values, max 15).',
        default=None,
    )

    @model_validator(mode='after')
    def validate(self):
        """
        Validates the request parameters.
        """
        time_range_specific = bool(self.flight_datetime_from and self.flight_datetime_to)

        if not time_range_specific and not self.flight_ids:
            raise ValueError('Either flight_datetime_from and flight_datetime_to or flight_ids must be provided')

        field_names = list(FlightSummaryBaseRequest.model_fields.keys())
        query_field_names = [fn for fn in field_names if fn not in ['flight_datetime_from', 'flight_datetime_to']]
        if all(getattr(self, field_name) is None for field_name in query_field_names):
            raise ValueError('At least one filter parameter must be provided')

        if self.flight_datetime_from and self.flight_datetime_to:
            if self.flight_datetime_from < datetime.now(tz=timezone.utc) - timedelta(days=14):
                raise ValueError('flight_datetime_from must be within the last 14 days')
            if self.flight_datetime_from > self.flight_datetime_to:
                raise ValueError('flight_datetime_from must be before flight_datetime_to')

        return self

    def to_dto(self) -> FlightSummaryBaseRequestDto:
        """
        Converts the request to a DTO.

        Returns:
            A FlightSummaryBaseRequestDto object.
        """
        return FlightSummaryBaseRequestDto(
            flight_ids=','.join(self.flight_ids) if self.flight_ids else None,
            flight_datetime_from=(self.flight_datetime_from.isoformat() if self.flight_datetime_from else None),
            flight_datetime_to=(self.flight_datetime_to.isoformat() if self.flight_datetime_to else None),
            flights=','.join(self.flights) if self.flights else None,
            callsigns=','.join(self.callsigns) if self.callsigns else None,
            registrations=','.join(self.registrations) if self.registrations else None,
            painted_as=','.join(self.painted_as) if self.painted_as else None,
            operating_as=','.join(self.operating_as) if self.operating_as else None,
            airports=','.join(map(str, self.airports)) if self.airports else None,
            routes=','.join(map(str, self.routes)) if self.routes else None,
            aircraft=','.join(self.aircraft) if self.aircraft else None,
        )


MAX_FLIGHT_SUMMARY_LIMIT = 20000


class FlightSummaryRequest(FlightSummaryBaseRequest):
    """
    Represents a request for flight summary data.
    """
    limit: Annotated[int, Field(ge=1, le=MAX_FLIGHT_SUMMARY_LIMIT)] | None = Field(
        default=None,
        description=f'Limit of results. Max value {MAX_FLIGHT_SUMMARY_LIMIT}',
    )
    sort: Sort | None = Field(
        default=None,
        description="""Sorting order of the results by first_seen.
        Default: asc (ascending). Available options: asc, desc.""",
    )

    def to_dto(self) -> GetFlightSummaryRequestDto:
        """
        Converts the request to a DTO.

        Returns:
            A GetFlightSummaryRequestDto object.
        """
        dto = super().to_dto()
        return GetFlightSummaryRequestDto(
            **dto.model_dump(),
            limit=self.limit if self.limit else None,
            sort=self.sort.value if self.sort else None,
        )


class FlightSummaryCountRequest(FlightSummaryBaseRequest):
    """
    Represents a request for a count of flight summary data.
    """
    pass


class FlightSummaryLight(BaseModel):
    """
    Represents a light version of a flight summary.
    """
    fr24_id: str = Field(description='Unique identifier assigned by Flightradar24 to the flight leg.')
    flight: str | None = Field(description='Commercial flight number.', default=None)
    callsign: str | None = Field(
        description="""Callsign used by Air Traffic Control to denote
        a specific flight (as sent by aircraft transponder).""",
        default=None,
    )
    operating_as: str | None = Field(
        description='ICAO code of the airline carrier as derived from flight callsign.',
        default=None,
    )
    painted_as: str | None = Field(
        description="ICAO code of the carrier mapped from FR24's internal database.",
        default=None,
    )
    type: str | None = Field(description='Aircraft ICAO type code.', default=None)
    reg: str | None = Field(
        description='Aircraft registration as matched from Mode-S identifier.',
        default=None,
    )
    orig_icao: str | None = Field(description='Origin airport ICAO code.', default=None)
    datetime_takeoff: datetime | None = Field(description='Datetime of takeoff in UTC', default=None)
    dest_icao: str | None = Field(
        description='Destination airport ICAO code.',
        default=None,
    )
    datetime_landed: datetime | None = Field(
        description='Datetime of landing in UTC',
        default=None,
    )
    hex: str | None = Field(
        description='24 bit Mode-S identifier expressed in hexadecimal format.',
        default=None,
    )
    first_seen: datetime | None = Field(
        description='Datetime when the aircraft was first detected for this flight leg (UTC)',
        default=None,
    )
    last_seen: datetime | None = Field(
        description='Datetime when the aircraft was last detected for this flight leg (UTC)',
        default=None,
    )
    flight_ended: bool | None = Field(
        description='Flag indicating if the flight is live (currently tracked) or historical.',
        default=None,
    )

    @staticmethod
    def from_dto(dto: FlightSummaryLightDto) -> 'FlightSummaryLight':
        """
        Creates a FlightSummaryLight object from a FlightSummaryLightDto.

        Args:
            dto: The FlightSummaryLightDto object.

        Returns:
            A FlightSummaryLight object.
        """
        return FlightSummaryLight(
            fr24_id=dto.fr24_id,
            flight=dto.flight,
            callsign=dto.callsign,
            operating_as=dto.operating_as,
            painted_as=dto.painted_as,
            type=dto.type,
            reg=dto.reg,
            orig_icao=dto.orig_icao,
            datetime_takeoff=datetime.fromisoformat(dto.datetime_takeoff) if dto.datetime_takeoff else None,
            dest_icao=dto.dest_icao,
            datetime_landed=datetime.fromisoformat(dto.datetime_landed) if dto.datetime_landed else None,
            hex=dto.hex,
            first_seen=datetime.fromisoformat(dto.first_seen) if dto.first_seen else None,
            last_seen=datetime.fromisoformat(dto.last_seen) if dto.last_seen else None,
            flight_ended=dto.flight_ended,
        )


class FlightSummary(FlightSummaryLight):
    """
    Represents a flight summary.
    """
    orig_iata: str | None = Field(
        description='Origin airport IATA code.',
        default=None,
    )
    runway_takeoff: str | None = Field(
        description='Identifier of the runway used for takeoff.',
        default=None,
    )
    dest_iata: str | None = Field(
        description='Destination airport IATA code.',
        default=None,
    )
    dest_icao_actual: str | None = Field(
        description='ICAO code for the actual destination airport (different when diverted).',
        default=None,
    )
    dest_iata_actual: str | None = Field(
        description='IATA code for the actual destination airport (different when diverted).',
        default=None,
    )
    runway_landed: str | None = Field(
        description='Identifier of the runway used for landing.',
        default=None,
    )
    flight_time: float | None = Field(
        description='Duration of the flight from takeoff to landing in seconds.',
        default=None,
    )
    actual_distance: float | None = Field(
        description='Actual ground distance the aircraft traveled (in km).',
        default=None,
    )
    circle_distance: float | None = Field(
        description='Great-circle distance between the first and last position (in km).',
        default=None,
    )

    @staticmethod
    def from_dto(dto: FlightSummaryDto) -> 'FlightSummary':
        """
        Creates a FlightSummary object from a FlightSummaryDto.

        Args:
            dto: The FlightSummaryDto object.

        Returns:
            A FlightSummary object.
        """
        return FlightSummary(
            fr24_id=dto.fr24_id,
            flight=dto.flight,
            callsign=dto.callsign,
            operating_as=dto.operating_as,
            painted_as=dto.painted_as,
            type=dto.type,
            reg=dto.reg,
            orig_icao=dto.orig_icao,
            datetime_takeoff=datetime.fromisoformat(dto.datetime_takeoff) if dto.datetime_takeoff else None,
            dest_icao=dto.dest_icao,
            datetime_landed=datetime.fromisoformat(dto.datetime_landed) if dto.datetime_landed else None,
            hex=dto.hex,
            first_seen=datetime.fromisoformat(dto.first_seen) if dto.first_seen else None,
            last_seen=datetime.fromisoformat(dto.last_seen) if dto.last_seen else None,
            orig_iata=dto.orig_iata,
            runway_takeoff=dto.runway_takeoff,
            dest_iata=dto.dest_iata,
            dest_icao_actual=dto.dest_icao_actual,
            dest_iata_actual=dto.dest_iata_actual,
            runway_landed=dto.runway_landed,
            flight_time=dto.flight_time,
            flight_ended=dto.flight_ended,
            actual_distance=dto.actual_distance,
            circle_distance=dto.circle_distance,
        )
