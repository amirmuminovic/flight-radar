from pydantic import BaseModel


### Common DTOs ###
class ApiUsageDto(BaseModel):
    endpoint: str
    request_count: int
    credits: int


###### Request DTOs ######
class ApiUsageBaseRequestDto(BaseModel):
    period: str


###### Response DTOs ######
class GetApiUsageResponseDto(BaseModel):
    data: list[ApiUsageDto]
