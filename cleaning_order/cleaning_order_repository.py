import psycopg2
from cleaning_order_dao import CleaningOrderDAO
from cleaning_order_status import CleaningOrderStatus

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
        status INTEGER NOT NULL
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_order(order: CleaningOrderDAO):
    query = """
    INSERT INTO cleaning_orders_zhamila (objectName, description, deadline, status)
    VALUES (%s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (order.objectName, order.description, order.deadline, order.status))
    conn.commit()


def update_order_status(status: int):
    query = "UPDATE cleaning_orders_zhamila SET status='{}';".format(status)
    cursor = conn.cursor()
    cursor.execute(query)
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
        status=order[4]
    ) for order in cursor.fetchall()]