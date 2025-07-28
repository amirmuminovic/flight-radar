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
    def __init__(self, api_client: FlightRadarApiClient):
        self.api_client = api_client

    def get_airlines_light(self, icao: str) -> Airline:
        """
        Get airline light data

        Args:
            icao: ICAO code of the airline

        Returns:
            Airline: Airline model
        """
        dto = self.api_client.get(
            f'/static/airlines/{icao}/light',
            GetAirlineLightResponseDto,
        )

        return Airline.from_dto(dto)

    def get_airports_light(self, code: str) -> AirportLight:
        """
        Get airport light data

        Args:
            code: ICAO code of the airport

        Returns:
            AirportLight: Airport light model
        """
        dto = self.api_client.get(
            f'/static/airports/{code}/light',
            GetAirportLightResponseDto,
        )

        return AirportLight.from_dto(dto)

    def get_airports(self, code: str) -> Airport:
        """
        Get airport data

        Args:
            code: ICAO code of the airport

        Returns:
            Airport: Airport model
        """
        dto = self.api_client.get(
            f'/static/airports/{code}/full',
            GetAirportResponseDto,
        )

        return Airport.from_dto(dto)

    def get_live_flight_positions_light(self, request: LiveFlightPositionRequest) -> List[FlightPositionLight]:
        """
        Get live flight positions light data

        Args:
            request: LiveFlightPositionRequest

        Returns:
            List[FlightPositionLight]: List of flight position light models
        """
        dto = self.api_client.get(
            '/live/flight-positions/light',
            GetLiveFlightPositionLightResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightPositionLight.from_dto(flight_position) for flight_position in dto.data]

    def get_live_flight_positions(self, request: LiveFlightPositionRequest) -> List[FlightPosition]:
        """
        Get live flight positions data

        Args:
            request: LiveFlightPositionRequest

        Returns:
            List[FlightPosition]: List of flight position models
        """
        dto = self.api_client.get(
            '/live/flight-positions/full',
            GetLiveFlightPositionResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightPosition.from_dto(flight_position) for flight_position in dto.data]

    def get_live_flight_position_count(self, request: LiveFlightPositionCountRequest) -> CountResponse:
        """
        Get live flight positions count

        Args:
            request: LiveFlightPositionCountRequest

        Returns:
            CountResponse: Count response model
        """
        dto = self.api_client.get(
            '/live/flight-positions/count',
            GetLiveFlightPositionCountResponseDto,
            request.to_dto().model_dump(),
        )

        return CountResponse.from_dto(dto)

    def get_historic_positions_light(self, request: HistoricFlightPositionRequest) -> List[FlightPositionLight]:
        """
        Get historic flight positions light data

        Args:
            request: HistoricFlightPositionRequest

        Returns:
            List[FlightPositionLight]: List of flight position light models
        """
        dto = self.api_client.get(
            '/historic/flight-positions/light',
            GetHistoricFlightPositionLightResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightPositionLight.from_dto(flight_position) for flight_position in dto.data]

    def get_historic_positions(self, request: HistoricFlightPositionRequest) -> List[FlightPosition]:
        """
        Get historic flight positions data

        Args:
            request: HistoricFlightPositionRequest

        Returns:
            List[FlightPosition]: List of flight position models
        """
        dto = self.api_client.get(
            '/historic/flight-positions/full',
            GetHistoricFlightPositionResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightPosition.from_dto(flight_position) for flight_position in dto.data]

    def get_historic_positions_count(self, request: HistoricFlightPositionCountRequest) -> CountResponse:
        """
        Get historic flight positions count

        Args:
            request: HistoricFlightPositionCountRequest

        Returns:
            CountResponse: Count response model
        """
        dto = self.api_client.get(
            '/historic/flight-positions/count',
            GetHistoricFlightPositionCountResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return CountResponse.from_dto(dto)

    def get_flight_summary_light(self, request: FlightSummaryRequest) -> List[FlightSummaryLight]:
        """
        Get flight summary light data

        Args:
            request: FlightSummaryRequest

        Returns:
            List[FlightSummaryLight]: List of flight summary light models
        """
        dto = self.api_client.get(
            '/flight-summary/light',
            GetFlightSummaryLightResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightSummaryLight.from_dto(flight_summary) for flight_summary in dto.data]

    def get_flight_summary(self, request: FlightSummaryRequest) -> List[FlightSummary]:
        """
        Get flight summary data

        Args:
            request: FlightSummaryRequest

        Returns:
            List[FlightSummary]: List of flight summary models
        """
        dto = self.api_client.get(
            '/flight-summary/full',
            GetFlightSummaryResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [FlightSummary.from_dto(flight_summary) for flight_summary in dto.data]

    def get_flight_summary_count(self, request: FlightSummaryCountRequest) -> CountResponse:
        """
        Get flight summary count

        Args:
            request: FlightSummaryCountRequest

        Returns:
            CountResponse: Count response model
        """
        dto = self.api_client.get(
            '/flight-summary/count',
            GetFlightSummaryCountResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return CountResponse.from_dto(dto)

    def get_flight_tracks(self, request: FlightTrackRequest) -> tuple[str, List[FlightTrack]]:
        """
        Get flight tracks

        Args:
            request: FlightTrackRequest

        Returns:
            tuple[str, List[FlightTrack]]: Tuple containing the flight ID and list of flight tracks
        """
        dto = self.api_client.get_many(
            '/flight-tracks',
            GetFlightTracksResponseDto,
            request.to_dto().model_dump(),
        )

        return (dto[0].fr24_id, [FlightTrack.from_dto(track) for track in dto[0].tracks])

    def get_api_usage(self, request: ApiUsageRequest) -> List[ApiUsage]:
        """
        Get API usage

        Args:
            request: ApiUsageRequest

        Returns:
            List[ApiUsage]: List of API usage models
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
        Get historic flight events light data

        Args:
            request: HistoricFlightEventRequest

        Returns:
            List[HistoricFlightEventLightResponseEntry]: List of historic flight events light models
        """
        dto = self.api_client.get(
            '/historic/flight-events/light',
            HistoricFlightEventLightResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [HistoricFlightEventLightResponseEntry.from_dto(event) for event in dto.data]

    def get_historic_flight_events(self, request: HistoricFlightEventRequest) -> List[HistoricFlightEventResponseEntry]:
        """
        Get historic flight events data

        Args:
            request: HistoricFlightEventRequest

        Returns:
            List[HistoricFlightEventResponse]: List of historic flight events models
        """
        dto = self.api_client.get(
            '/historic/flight-events/full',
            HistoricFlightEventResponseDto,
            request.to_dto().model_dump(exclude_none=True),
        )

        return [HistoricFlightEventResponseEntry.from_dto(event) for event in dto.data]
