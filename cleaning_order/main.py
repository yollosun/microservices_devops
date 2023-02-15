import time
import random
from cleaning_order_repository import create_table, insert_order
from cleaning_order_dao import CleaningOrderDAO
from cleaning_order_status import CleaningOrderStatus
import datetime

create_table()



if __name__ == '__main__':
    while True:
        datetimes = [datetime.datetime(2023, 2, 16, 10, 11, 12, 99000),
        datetime.datetime(2023, 2, 16, 10, 20, 12, 99000),
        datetime.datetime(2023, 2, 16, 2, 40, 12, 99000),
        datetime.datetime(2023, 2, 16, 11, 11, 12, 99000)
        ]
        insert_order(
            CleaningOrderDAO(
                objectName=random.choice(["Magnum", "Small", "School 5"]),
                description=random.choice(["Clean", "Dirty", "Very dirty"]),
                deadline=random.choice(datetimes),
                status=CleaningOrderStatus.created.value
            )
        )
        print("Inserted")
        time.sleep(10)