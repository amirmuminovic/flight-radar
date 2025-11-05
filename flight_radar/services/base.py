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
    """
    Abstract base class for a Flight Radar client.
    """
    @abstractmethod
    def get_airlines_light(self, icao: str) -> Airline:
        """
        Get a light version of an airline.
        """
        pass

    @abstractmethod
    def get_airports_light(self, code: str) -> AirportLight:
        """
        Get a light version of an airport.
        """
        pass

    @abstractmethod
    def get_airports(self, code: str) -> Airport:
        """
        Get a full version of an airport.
        """
        pass

    @abstractmethod
    def get_live_flight_positions_light(self, request: LiveFlightPositionRequest) -> List[FlightPositionLight]:
        """
        Get a light version of live flight positions.
        """
        pass

    @abstractmethod
    def get_live_flight_positions(self, request: LiveFlightPositionRequest) -> List[FlightPosition]:
        """
        Get a full version of live flight positions.
        """
        pass

    @abstractmethod
    def get_live_flight_position_count(self, request: LiveFlightPositionCountRequest) -> CountResponse:
        """
        Get a count of live flight positions.
        """
        pass

    @abstractmethod
    def get_historic_positions_light(self, request: HistoricFlightPositionRequest) -> List[FlightPositionLight]:
        """
        Get a light version of historic flight positions.
        """
        pass

    @abstractmethod
    def get_historic_positions(self, request: HistoricFlightPositionRequest) -> List[FlightPosition]:
        """
        Get a full version of historic flight positions.
        """
        pass

    @abstractmethod
    def get_historic_positions_count(self, request: HistoricFlightPositionCountRequest) -> CountResponse:
        """
        Get a count of historic flight positions.
        """
        pass

    @abstractmethod
    def get_flight_summary_light(self, request: FlightSummaryRequest) -> List[FlightSummaryLight]:
        """
        Get a light version of a flight summary.
        """
        pass

    @abstractmethod
    def get_flight_summary(self, request: FlightSummaryRequest) -> List[FlightSummary]:
        """
        Get a full version of a flight summary.
        """
        pass

    @abstractmethod
    def get_flight_summary_count(self, request: FlightSummaryCountRequest) -> CountResponse:
        """
        Get a count of flight summaries.
        """
        pass

    @abstractmethod
    def get_flight_tracks(self, request: FlightTrackRequest) -> tuple[str, List[FlightTrack]]:
        """
        Get flight tracks.
        """
        pass

    @abstractmethod
    def get_api_usage(self, request: ApiUsageRequest) -> List[ApiUsage]:
        """
        Get API usage.
        """
        pass

    @abstractmethod
    def get_historic_flight_events_light(
        self, request: HistoricFlightEventRequest
    ) -> List[HistoricFlightEventLightResponseEntry]:
        """
        Get a light version of historic flight events.
        """
        pass

    @abstractmethod
    def get_historic_flight_events(self, request: HistoricFlightEventRequest) -> List[HistoricFlightEventResponseEntry]:
        """
        Get a full version of historic flight events.
        """
        pass
