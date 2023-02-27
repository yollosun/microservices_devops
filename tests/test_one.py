from sqlalchemy import create_engine
import datetime
import sys
sys.path.insert(0, 'C:/Users/Zhamila/Desktop/devops/microservices')
from cleaning_order.cleaning_order_dao import CleaningOrderDAO
from cleaning_order.cleaning_order_status import CleaningOrderStatus
from cleaning_order.cleaning_order_repository import insert_order, get_orders, update_order_status


def test_insert_order(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()
    order = CleaningOrderDAO(
        objectName="test_objectName 1",
        description="test_description 1",
        deadline=datetime.datetime(2023, 2, 16, 10, 20, 12, 99000),
        status=CleaningOrderStatus.created.value,
        supervisor_email="test@gmail.com"
    )
    insert_order(conn, order)

    orders = get_orders(conn)
    assert len(orders) == 4
    order = orders[-1]
    assert order.objectName == "test_objectName 1"
    assert order.status == 1
    engine.dispose(conn_with_data)


def test_update_order_status(conn_with_data: str):
    engine = create_engine(conn_with_data)
    conn = engine.connect()

    orders = get_orders(conn)
    for order in orders:
        if order.deadline < datetime.datetime.now().date():
            update_order_status(conn, CleaningOrderStatus.overdue.value, order.id)
    updated_orders = get_orders(conn)
    for order in updated_orders:
        assert order.status == CleaningOrderStatus.overdue.value
    engine.dispose(conn_with_data)