import time
import datetime
from cleaning_order.cleaning_order_repository import create_table, update_order_status, get_orders
from cleaning_order.cleaning_order_status import CleaningOrderStatus
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        orders = get_orders(conn)
        for order in orders:
            if order.deadline < datetime.datetime.now().date():
                update_order_status(conn, CleaningOrderStatus.overdue.value, order.id)
        print("updated")
        time.sleep(20)