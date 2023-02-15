import enum

class CleaningOrderStatus(enum.Enum):
    created = 1
    viewed = 2
    started = 3
    completed = 4
    cancelled = 5
    overdue = 6