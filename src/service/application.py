from typing import Optional, Sequence

from src.kafka.producer import kafka
from src.models import ApplicationModel
from src.schemas.application import ApplicationSchema, ApplicationResponse
from src.service.base import BaseService
from src.utils.unit_of_work import transaction_mode


class ApplicationService(BaseService):
    base_repository = 'applications'

    @transaction_mode
    async def create_application(
            self,
            application_data: ApplicationSchema,
    ) -> ApplicationModel:
        """
        Create a new application in the database.
        """
        new_application: ApplicationModel = await self.uow.applications.add_one_and_get_obj(
            user_name=application_data.user_name,
            description=application_data.description,
        )
        message = {
            'id': new_application.id,
            'user_name': new_application.user_name,
            'description': new_application.description,
            'created_at': new_application.created_at.isoformat(),
        }
        await kafka.send_message(message)
        return new_application

    @transaction_mode
    async def get_applications(
            self,
            user_name: Optional[str],
            page: int,
            size: int,
    ) -> list[ApplicationResponse]:

        result: Sequence[ApplicationModel] = await self.uow.applications.get_applications(user_name, page, size)
        applications = [application.to_pydantic_schema() for application in result]
        return applications
