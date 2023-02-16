import time
import datetime
from cleaning_order.cleaning_order_repository import create_table, update_order_status, get_orders
from cleaning_order.cleaning_order_status import CleaningOrderStatus

create_table()

def notify_supervisor(email: str):
    print("Sended email about deadline to {}".format(email))

if __name__ == '__main__':
    while True:
        orders = get_orders()
        for order in orders:
            if order.status == CleaningOrderStatus.overdue.value:
                notify_supervisor(order.supervisor_email)
        print("email sended")
        time.sleep(20)
