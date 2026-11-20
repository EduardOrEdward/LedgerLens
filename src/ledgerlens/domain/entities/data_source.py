# import fastapi
from enum import Enum
from uuid import UUID, uuid4

# from typing import Any,Optional


class Source_type(Enum):
    REST_API = "rest_api"
    CVS = "cvs"
    POSTGRESQL = "postgresql"


class DataSource:
    def __init__(self, id: UUID | None, source_type: Source_type):
        self.id = uuid4() or id
        self.source_type = source_type
