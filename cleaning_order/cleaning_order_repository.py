import psycopg2
from cleaning_order.cleaning_order_dao import CleaningOrderDAO
from cleaning_order.cleaning_order_status import CleaningOrderStatus

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS cleaning_orders_zhamila (
        id SERIAL PRIMARY KEY,
        objectName VARCHAR(255) NOT NULL,
        description VARCHAR(255) NOT NULL,
        deadline DATE DEFAULT NOW(),
        status INTEGER NOT NULL,
        supervisor_email VARCHAR(255) NOT NULL
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_order(order: CleaningOrderDAO):
    query = """
    INSERT INTO cleaning_orders_zhamila (objectName, description, deadline, status, supervisor_email)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (order.objectName, order.description, order.deadline, order.status, order.supervisor_email))
    conn.commit()


def update_order_status(status_id: int, order_id: int):
    query = "UPDATE cleaning_orders_zhamila SET status=:status WHERE id=:order_id;"
    cursor = conn.cursor()
    cursor.execute(query, status=status_id, order_id=order_id)
    conn.commit()


def get_orders() -> list[CleaningOrderDAO]:
    query = "SELECT * FROM cleaning_orders_zhamila;"
    cursor = conn.cursor()
    cursor.execute(query)
    return [CleaningOrderDAO(
        id=order[0],
        objectName=order[1],
        description=order[2],
        deadline=order[3],
        status=order[4],
        supervisor_email=order[5]
    ) for order in cursor.fetchall()]