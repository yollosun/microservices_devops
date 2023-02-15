from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from cleaning_order_status import CleaningOrderStatus


@dataclass
class CleaningOrderDAO:
    objectName: str
    description: str
    deadline: datetime
    status: int = CleaningOrderStatus.created.value
    id: Optional[int] = None


