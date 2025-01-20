from typing import Optional

from fastapi import APIRouter, Depends, Query
from starlette import status

from src.models import ApplicationModel
from src.schemas.application import ApplicationSchema, ApplicationResponse, ApplicationSchemaDB
from src.service.application import ApplicationService

router = APIRouter(prefix='/applications')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_application(
        application_data: ApplicationSchema,
        application_service: ApplicationService = Depends()
) -> ApplicationSchemaDB:
    """
    Create a new application in the database and send a message to Kafka.
    """
    new_application: ApplicationModel = await application_service.create_application(application_data)
    return new_application.to_pydantic_schema()


@router.get('/', status_code=status.HTTP_200_OK)
async def get_applications(
    user_name: Optional[str] = None,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    application_service: ApplicationService = Depends(),
) -> list[ApplicationResponse]:
    """
    Retrieve a list of applications based on the provided filters.
    """
    return await application_service.get_applications(user_name=user_name, page=page, size=size)
