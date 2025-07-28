from pydantic import BaseModel, Field

from flight_radar.dtos import ApiUsageBaseRequestDto, ApiUsageDto
from flight_radar.enums.enums import TimePeriod


class ApiUsageRequest(BaseModel):
    period: TimePeriod = TimePeriod.DAY

    def to_dto(self) -> ApiUsageBaseRequestDto:
        return ApiUsageBaseRequestDto(
            period=self.period.value,
        )


class ApiUsage(BaseModel):
    endpoint: str = Field(description='Endpoint of the API call')
    request_count: int = Field(description='Number of requests')
    credits: int = Field(description='Number of credits used')

    @staticmethod
    def from_dto(dto: ApiUsageDto) -> 'ApiUsage':
        return ApiUsage(
            endpoint=dto.endpoint,
            request_count=dto.request_count,
            credits=dto.credits,
        )
