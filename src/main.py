import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api import router
from src.kafka.producer import kafka


@asynccontextmanager
async def lifespan(app: FastAPI):
    await kafka.producer_start()
    yield
    await kafka.producer_stop()


def create_fast_api_app() -> FastAPI:
    load_dotenv(find_dotenv('.env'))
    env_name = os.getenv('MODE', 'DEV')

    if env_name != 'PROD':
        fastapi_app = FastAPI(
            default_response_class=ORJSONResponse,
            lifespan=lifespan
        )
    else:
        fastapi_app = FastAPI(
            default_response_class=ORJSONResponse,
            lifespan=lifespan,
            docs_url=None,
            redoc_url=None,
        )

    fastapi_app.include_router(router, prefix='/api')
    return fastapi_app


app = create_fast_api_app()
