# import fastapi
from uuid import UUID, uuid4

from src.ledgerlens.domain.value_objects.source_type import SourceType

# from typing import Any,Optional


class DataSource:
    def __init__(self, source_type: SourceType, id: UUID | None = None):
        self.id = uuid4() or id
        self.source_type = source_type


s = SourceType.CSV
d = DataSource(source_type=s)
print(d.id)
