from abc import ABC, abstractmethod
from typing import List

from flight_radar.models import (
    Airline,
    Airport,
    AirportLight,
    ApiUsage,
    ApiUsageRequest,
    CountResponse,
    FlightPosition,
    FlightPositionLight,
    FlightSummary,
    FlightSummaryCountRequest,
    FlightSummaryLight,
    FlightSummaryRequest,
    FlightTrack,
    FlightTrackRequest,
    HistoricFlightPositionCountRequest,
    HistoricFlightPositionRequest,
    LiveFlightPositionCountRequest,
    LiveFlightPositionRequest,
)
from flight_radar.models.historic_flight_event import (
    HistoricFlightEventLightResponseEntry,
    HistoricFlightEventRequest,
    HistoricFlightEventResponseEntry,
)


class BaseFlightRadarClient(ABC):
    @abstractmethod
    def get_airlines_light(self, icao: str) -> Airline:
        pass

    @abstractmethod
    def get_airports_light(self, code: str) -> AirportLight:
        pass

    @abstractmethod
    def get_airports(self, code: str) -> Airport:
        pass

    @abstractmethod
    def get_live_flight_positions_light(self, request: LiveFlightPositionRequest) -> List[FlightPositionLight]:
        pass

    @abstractmethod
    def get_live_flight_positions(self, request: LiveFlightPositionRequest) -> List[FlightPosition]:
        pass

    @abstractmethod
    def get_live_flight_position_count(self, request: LiveFlightPositionCountRequest) -> CountResponse:
        pass

    @abstractmethod
    def get_historic_positions_light(self, request: HistoricFlightPositionRequest) -> List[FlightPositionLight]:
        pass

    @abstractmethod
    def get_historic_positions(self, request: HistoricFlightPositionRequest) -> List[FlightPosition]:
        pass

    @abstractmethod
    def get_historic_positions_count(self, request: HistoricFlightPositionCountRequest) -> CountResponse:
        pass

    @abstractmethod
    def get_flight_summary_light(self, request: FlightSummaryRequest) -> List[FlightSummaryLight]:
        pass

    @abstractmethod
    def get_flight_summary(self, request: FlightSummaryRequest) -> List[FlightSummary]:
        pass

    @abstractmethod
    def get_flight_summary_count(self, request: FlightSummaryCountRequest) -> CountResponse:
        pass

    @abstractmethod
    def get_flight_tracks(self, request: FlightTrackRequest) -> tuple[str, List[FlightTrack]]:
        pass

    @abstractmethod
    def get_api_usage(self, request: ApiUsageRequest) -> List[ApiUsage]:
        pass

    @abstractmethod
    def get_historic_flight_events_light(
        self, request: HistoricFlightEventRequest
    ) -> List[HistoricFlightEventLightResponseEntry]:
        pass

    @abstractmethod
    def get_historic_flight_events(self, request: HistoricFlightEventRequest) -> List[HistoricFlightEventResponseEntry]:
        pass
