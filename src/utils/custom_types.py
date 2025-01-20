from collections.abc import Awaitable, Callable
from datetime import datetime
from typing import Annotated, Any

from sqlalchemy import DateTime, text
from sqlalchemy.orm import mapped_column

async_func = Callable[..., Awaitable[Any]]

dt_now_utc_sql = text("TIMEZONE('utc', now())")
created_at = Annotated[datetime, mapped_column(DateTime, server_default=dt_now_utc_sql)]
