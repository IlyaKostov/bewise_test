from datetime import datetime

from pydantic import BaseModel


class ApplicationID(BaseModel):
    id: int


class ApplicationSchema(BaseModel):
    user_name: str
    description: str


class ApplicationSchemaDB(ApplicationID, ApplicationSchema):
    pass


class ApplicationResponse(ApplicationSchemaDB):
    created_at: datetime
