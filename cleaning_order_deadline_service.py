import time
import datetime
from cleaning_order.cleaning_order_repository import create_table, update_order_status, get_orders
from cleaning_order.cleaning_order_status import CleaningOrderStatus

create_table()

if __name__ == '__main__':
    while True:
        orders = get_orders()
        for order in orders:
            if order.deadline < datetime.datetime.now().date():
                update_order_status(CleaningOrderStatus.overdue.value, order.id)
        print("updated")
        time.sleep(20)