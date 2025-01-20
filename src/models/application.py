from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from src.models import BaseModel
from src.schemas.application import ApplicationResponse


class ApplicationModel(BaseModel):
    __tablename__ = 'applications'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str]
    description: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def to_pydantic_schema(self) -> ApplicationResponse:
        return ApplicationResponse(**self.__dict__)
