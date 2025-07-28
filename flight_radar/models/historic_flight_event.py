from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from flight_radar.dtos import (
    HistoricFlightEventBaseResponseDto,
    HistoricFlightEventDetailsDto,
    HistoricFlightEventDto,
    HistoricFlightEventRequestDto,
    HistoricFlightEventResponseEntryDto,
)
from flight_radar.enums.enums import HistoricFlightEventTypes
from flight_radar.models.common import ConstrainedStringList


class HistoricFlightEventRequest(BaseModel):
    flight_ids: ConstrainedStringList = Field(
        description='List of fr24_ids (maximum 15 IDs). Cannot be combined with event_datetime.',
    )
    event_types: List[HistoricFlightEventTypes] | None = Field(
        description='Event types to filter by',
        default=None,
    )

    def _map_event_types(self) -> str | None:
        if not self.event_types:
            return HistoricFlightEventTypes.ALL.value

        return ','.join([event_type.value for event_type in self.event_types])

    def to_dto(self) -> HistoricFlightEventRequestDto:
        return HistoricFlightEventRequestDto(
            flight_ids=','.join(self.flight_ids),
            event_types=self._map_event_types(),
        )


class HistoricFlightEventDetails(BaseModel):
    gate_ident: str | None = Field(
        description='Gate identifier.',
        default=None,
    )
    gate_lat: float | None = Field(
        description='Latitude of the gate.',
        default=None,
    )
    gate_lon: float | None = Field(
        description='Longitude of the gate.',
        default=None,
    )
    takeoff_runway: str | None = Field(
        description='Runway used during takeoff.',
        default=None,
    )
    landed_icao: str | None = Field(
        description='ICAO code of the destination airport.',
        default=None,
    )
    landed_runway: str | None = Field(
        description='Runway used during landing.',
        default=None,
    )
    exited_airspace: str | None = Field(
        description='Name of the airspace exited.',
        default=None,
    )
    exited_airspace_id: str | None = Field(
        description='ID of the airspace exited.',
        default=None,
    )
    entered_airspace: str | None = Field(
        description='Name of the airspace entered.',
        default=None,
    )
    entered_airspace_id: str | None = Field(
        description='ID of the airspace entered.',
        default=None,
    )

    @staticmethod
    def from_dto(dto: HistoricFlightEventDetailsDto) -> 'HistoricFlightEventDetails':
        return HistoricFlightEventDetails(
            gate_ident=dto.gate_ident,
            gate_lat=dto.gate_lat,
            gate_lon=dto.gate_lon,
            takeoff_runway=dto.takeoff_runway,
            landed_icao=dto.landed_icao,
            landed_runway=dto.landed_runway,
            exited_airspace=dto.exited_airspace,
            exited_airspace_id=dto.exited_airspace_id,
            entered_airspace=dto.entered_airspace,
            entered_airspace_id=dto.entered_airspace_id,
        )


class HistoricFlightEvent(BaseModel):
    type: HistoricFlightEventTypes = Field(description='Type of the event (e.g., gate_departure, takeoff, cruising).')
    timestamp: datetime = Field(description='Time of the event in UTC.')
    lat: float | None = Field(description='Latitude at the time of the event.', default=None)
    lon: float | None = Field(description='Longitude at the time of the event.', default=None)
    alt: int | None = Field(description='Altitude at the time of the event.', default=None)
    gspeed: int | None = Field(description='Ground speed at the time of the event.', default=None)
    details: HistoricFlightEventDetails | None = Field(
        description='Additional context depending on the event type.',
        default=None,
    )

    @staticmethod
    def from_dto(dto: HistoricFlightEventDto) -> 'HistoricFlightEvent':
        return HistoricFlightEvent(
            type=HistoricFlightEventTypes(dto.type),
            timestamp=datetime.fromisoformat(dto.timestamp),
            lat=dto.lat,
            lon=dto.lon,
            alt=dto.alt,
            gspeed=dto.gspeed,
            details=HistoricFlightEventDetails.from_dto(dto.details) if dto.details else None,
        )


class HistoricFlightEventLightResponseEntry(BaseModel):
    fr24_id: str = Field(description='Unique identifier for the flight.')
    callsign: str = Field(description='Flight number or callsign.')
    hex: str = Field(description='Aircraft hex code.')
    events: list[HistoricFlightEvent] = Field(description='List of events associated with the flight.')

    @staticmethod
    def from_dto(
        dto: HistoricFlightEventBaseResponseDto,
    ) -> 'HistoricFlightEventLightResponseEntry':
        return HistoricFlightEventLightResponseEntry(
            fr24_id=dto.fr24_id,
            callsign=dto.callsign,
            hex=dto.hex,
            events=[HistoricFlightEvent.from_dto(event) for event in dto.events],
        )


class HistoricFlightEventResponseEntry(HistoricFlightEventLightResponseEntry):
    painted_as: str | None = Field(
        description='The airline or operator the flight is painted as.',
        default=None,
    )
    operating_as: str | None = Field(
        description='The airline or operator actually operating the flight.',
        default=None,
    )
    orig_icao: str = Field(description='ICAO code for the origin airport.')
    orig_iata: str = Field(description='IATA code for the origin airport.')
    dest_iata: str = Field(description='IATA code for the destination airport.')
    dest_icao: str = Field(description='ICAO code for the destination airport.')

    @staticmethod
    def from_dto(
        dto: HistoricFlightEventResponseEntryDto,
    ) -> 'HistoricFlightEventResponseEntry':
        return HistoricFlightEventResponseEntry(
            fr24_id=dto.fr24_id,
            callsign=dto.callsign,
            hex=dto.hex,
            events=[HistoricFlightEvent.from_dto(event) for event in dto.events],
            painted_as=dto.painted_as,
            operating_as=dto.operating_as,
            orig_icao=dto.orig_icao,
            orig_iata=dto.orig_iata,
            dest_iata=dto.dest_iata,
            dest_icao=dto.dest_icao,
        )
