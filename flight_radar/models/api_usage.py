from pydantic import BaseModel, Field

from flight_radar.dtos import ApiUsageBaseRequestDto, ApiUsageDto
from flight_radar.enums.enums import TimePeriod


class ApiUsageRequest(BaseModel):
    """
    Represents a request for API usage data.
    """
    period: TimePeriod = TimePeriod.DAY

    def to_dto(self) -> ApiUsageBaseRequestDto:
        """
        Converts the request to a DTO.

        Returns:
            An ApiUsageBaseRequestDto object.
        """
        return ApiUsageBaseRequestDto(
            period=self.period.value,
        )


class ApiUsage(BaseModel):
    """
    Represents API usage data.
    """
    endpoint: str = Field(description='Endpoint of the API call')
    request_count: int = Field(description='Number of requests')
    credits: int = Field(description='Number of credits used')

    @staticmethod
    def from_dto(dto: ApiUsageDto) -> 'ApiUsage':
        """
        Creates an ApiUsage object from an ApiUsageDto.

        Args:
            dto: The ApiUsageDto object.

        Returns:
            An ApiUsage object.
        """
        return ApiUsage(
            endpoint=dto.endpoint,
            request_count=dto.request_count,
            credits=dto.credits,
        )
