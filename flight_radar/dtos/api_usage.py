from pydantic import BaseModel


### Common DTOs ###
class ApiUsageDto(BaseModel):
    """
    Represents API usage data.

    Attributes:
        endpoint: The API endpoint.
        request_count: The number of requests made to the endpoint.
        credits: The number of credits consumed by the endpoint.
    """
    endpoint: str
    request_count: int
    credits: int


###### Request DTOs ######
class ApiUsageBaseRequestDto(BaseModel):
    """
    Represents the base request for API usage data.

    Attributes:
        period: The period for which to retrieve API usage data.
    """
    period: str


###### Response DTOs ######
class GetApiUsageResponseDto(BaseModel):
    """
    Represents the response for API usage data.

    Attributes:
        data: A list of API usage data.
    """
    data: list[ApiUsageDto]
