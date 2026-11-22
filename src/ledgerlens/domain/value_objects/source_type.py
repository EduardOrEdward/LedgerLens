from enum import Enum


class SourceType(Enum):
    REST_API = "rest_api"
    CSV = "csv"
    POSTGRESQL = "postgresql"
