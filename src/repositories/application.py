from typing import Sequence

from sqlalchemy import select

from src.models import ApplicationModel
from src.repositories.base import SQLAlchemyRepository


class ApplicationRepository(SQLAlchemyRepository):
    model = ApplicationModel

    async def get_applications(self, user_name: str, page: int, size: int) -> Sequence[ApplicationModel]:
        """
        Retrieve a list of applications based on username and pagination parameters.
        """
        query = select(self.model)
        if user_name:
            query = query.filter_by(user_name=user_name)
        query = query.offset((page - 1) * size).limit(size)
        result = await self.session.execute(query)
        return result.scalars().all()
