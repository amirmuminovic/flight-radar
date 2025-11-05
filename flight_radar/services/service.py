from typing import List

from flight_radar.clients.api_client import FlightRadarApiClient
from flight_radar.dtos import (
    GetAirlineLightResponseDto,
    GetAirportLightResponseDto,
    GetAirportResponseDto,
    GetApiUsageResponseDto,
    GetFlightSummaryCountResponseDto,
    GetFlightSummaryLightResponseDto,
    GetFlightSummaryResponseDto,
    GetFlightTracksResponseDto,
    GetHistoricFlightPositionCountResponseDto,
    GetHistoricFlightPositionLightResponseDto,
    GetHistoricFlightPositionResponseDto,
    GetLiveFlightPositionCountResponseDto,
    GetLiveFlightPositionLightResponseDto,
    GetLiveFlightPositionResponseDto,
    HistoricFlightEventLightResponseDto,
    HistoricFlightEventResponseDto,
)

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
    HistoricFlightEventLightResponseEntry,
    HistoricFlightEventRequest,
    HistoricFlightEventResponseEntry,
)
from flight_radar.services.base import BaseFlightRadarClient


class FlightRadarClient(BaseFlightRadarClient):
    """
    Client for the Flight Radar API.
    """
    def __init__(self, api_client: FlightRadarApiClient):
        """
        Initializes the FlightRadarClient.

        Args:
            api_client: An instance of the FlightRadarApiClient.
        """
        self.api_client = api_client

    def get_airlines_light(self, icao: str) -> Airline:
        """
        Retrieves a light version of an airline's data.

        Args:
            icao: The ICAO code of the airline.

        Returns:
            An Airline object.
        """
        dto = self.api_client.get(
            f'/static/airlines/{icao}/light',
            GetAirlineLightResponseDto,
        )

        return Airline.from_dto(dto)

    def get_airports_light(self, code: str) -> AirportLight:
        """
        Retrieves a light version of an airport's data.

        Args:
            code: The ICAO or IATA code of the airport.

        Returns:
            An AirportLight object.
        """
        dto = self.api_client.get(
            f'/static/airports/{code}/light',
            GetAirportLightResponseDto,
        )

        return AirportLight.from_dto(dto)

    def get_airports(self, code: str) -> Airport:
        """
        Retrieves a full version of an airport's data.

        Args:
            code: The ICAO or IATA code of the airport.

        Returns:
            An Airport object.
        """
        dto = self.api_client.get(
            f'/static/airports/{code}/full',
            GetAirportResponseDto,
        )

        return Airport.from_dto(dto)

    def get_live_flight_positions_light(self, request: LiveFlightPositionRequest) -> List[FlightPositionLight]:
        """
        Retrieves a light version of live flight positions.

        Args:
            request: A LiveFlightPositionRequest object.

        Returns:
            A list of FlightPositionLight objects.
        """
        dto = self.api_client.get(
            '/live/flight-positions/light',
            GetLiveFlightPositionLightResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightPositionLight.from_dto(flight_position) for flight_position in dto.data]

    def get_live_flight_positions(self, request: LiveFlightPositionRequest) -> List[FlightPosition]:
        """
        Retrieves a full version of live flight positions.

        Args:
            request: A LiveFlightPositionRequest object.

        Returns:
            A list of FlightPosition objects.
        """
        dto = self.api_client.get(
            '/live/flight-positions/full',
            GetLiveFlightPositionResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightPosition.from_dto(flight_position) for flight_position in dto.data]

    def get_live_flight_position_count(self, request: LiveFlightPositionCountRequest) -> CountResponse:
        """
        Retrieves a count of live flight positions.

        Args:
            request: A LiveFlightPositionCountRequest object.

        Returns:
            A CountResponse object.
        """
        dto = self.api_client.get(
            '/live/flight-positions/count',
            GetLiveFlightPositionCountResponseDto,
            request.to_dto().model_dump(),
        )

        return CountResponse.from_dto(dto)

    def get_historic_positions_light(self, request: HistoricFlightPositionRequest) -> List[FlightPositionLight]:
        """
        Retrieves a light version of historic flight positions.

        Args:
            request: A HistoricFlightPositionRequest object.

        Returns:
            A list of FlightPositionLight objects.
        """
        dto = self.api_client.get(
            '/historic/flight-positions/light',
            GetHistoricFlightPositionLightResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightPositionLight.from_dto(flight_position) for flight_position in dto.data]

    def get_historic_positions(self, request: HistoricFlightPositionRequest) -> List[FlightPosition]:
        """
        Retrieves a full version of historic flight positions.

        Args:
            request: A HistoricFlightPositionRequest object.

        Returns:
            A list of FlightPosition objects.
        """
        dto = self.api_client.get(
            '/historic/flight-positions/full',
            GetHistoricFlightPositionResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightPosition.from_dto(flight_position) for flight_position in dto.data]

    def get_historic_positions_count(self, request: HistoricFlightPositionCountRequest) -> CountResponse:
        """
        Retrieves a count of historic flight positions.

        Args:
            request: A HistoricFlightPositionCountRequest object.

        Returns:
            A CountResponse object.
        """
        dto = self.api_client.get(
            '/historic/flight-positions/count',
            GetHistoricFlightPositionCountResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return CountResponse.from_dto(dto)

    def get_flight_summary_light(self, request: FlightSummaryRequest) -> List[FlightSummaryLight]:
        """
        Retrieves a light version of a flight summary.

        Args:
            request: A FlightSummaryRequest object.

        Returns:
            A list of FlightSummaryLight objects.
        """
        dto = self.api_client.get(
            '/flight-summary/light',
            GetFlightSummaryLightResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightSummaryLight.from_dto(flight_summary) for flight_summary in dto.data]

    def get_flight_summary(self, request: FlightSummaryRequest) -> List[FlightSummary]:
        """
        Retrieves a full version of a flight summary.

        Args:
            request: A FlightSummaryRequest object.

        Returns:
            A list of FlightSummary objects.
        """
        dto = self.api_client.get(
            '/flight-summary/full',
            GetFlightSummaryResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightSummary.from_dto(flight_summary) for flight_summary in dto.data]

    def get_flight_summary_count(self, request: FlightSummaryCountRequest) -> CountResponse:
        """
        Retrieves a count of flight summaries.

        Args:
            request: A FlightSummaryCountRequest object.

        Returns:
            A CountResponse object.
        """
        dto = self.api_client.get(
            '/flight-summary/count',
            GetFlightSummaryCountResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return CountResponse.from_dto(dto)

    def get_flight_tracks(self, request: FlightTrackRequest) -> tuple[str, List[FlightTrack]]:
        """
        Retrieves flight tracks.

        Args:
            request: A FlightTrackRequest object.

        Returns:
            A tuple containing the flight ID and a list of FlightTrack objects.
        """
        dto = self.api_client.get_many(
            '/flight-tracks',
            GetFlightTracksResponseDto,
            request.to_dto().model_dump(),
        )

        return (dto[0].fr24_id, [FlightTrack.from_dto(track) for track in dto[0].tracks])

    def get_api_usage(self, request: ApiUsageRequest) -> List[ApiUsage]:
        """
        Retrieves API usage data.

        Args:
            request: An ApiUsageRequest object.

        Returns:
            A list of ApiUsage objects.
        """
        dto = self.api_client.get(
            '/usage',
            GetApiUsageResponseDto,
            request.to_dto().model_dump(),
        )

        return [ApiUsage.from_dto(usage) for usage in dto.data]

    def get_historic_flight_events_light(
        self, request: HistoricFlightEventRequest
    ) -> List[HistoricFlightEventLightResponseEntry]:
        """
        Retrieves a light version of historic flight events.

        Args:
            request: A HistoricFlightEventRequest object.

        Returns:
            A list of HistoricFlightEventLightResponseEntry objects.
        """
        dto = self.api_client.get(
            '/historic/flight-events/light',
            HistoricFlightEventLightResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [HistoricFlightEventLightResponseEntry.from_dto(event) for event in dto.data]

    def get_historic_flight_events(self, request: HistoricFlightEventRequest) -> List[HistoricFlightEventResponseEntry]:
        """
        Retrieves a full version of historic flight events.

        Args:
            request: A HistoricFlightEventRequest object.

        Returns:
            A list of HistoricFlightEventResponseEntry objects.
        """
        dto = self.api_client.get(
            '/historic/flight-events/full',
            HistoricFlightEventResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [HistoricFlightEventResponseEntry.from_dto(event) for event in dto.data]
