from cleaning_order.cleaning_order_dao import CleaningOrderDAO
from cleaning_order.cleaning_order_status import CleaningOrderStatus
from sqlalchemy.engine import Connection
from sqlalchemy import text

def create_table(conn: Connection):
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

    conn.execute(text(query))
    conn.commit()


def insert_order(conn: Connection, order: CleaningOrderDAO):
    query = """
    INSERT INTO cleaning_orders_zhamila (objectName, description, deadline, status, supervisor_email)
    VALUES (:objectName, :description, :deadline, :status, :supervisor_email);
    """
    conn.execute(
        text(query),
        parameters={
            "objectName": order.objectName,
            "description": order.description,
            "deadline": order.deadline,
            "status": order.status,
            "supervisor_email": order.supervisor_email
        },
    )
    conn.commit()


def update_order_status(conn: Connection, status_id: int, order_id: int):
    parameters = {
        "order_id": order_id,
        "status_id": status_id
    }
    query = f"UPDATE cleaning_orders_zhamila SET status = '{parameters['status_id']}' WHERE id= '{parameters['order_id']}';"
    conn.execute(text(query))
    conn.commit()


def get_orders(conn: Connection) -> list[CleaningOrderDAO]:
    query = "SELECT * FROM cleaning_orders_zhamila;"
    orders = conn.execute(text(query)).fetchall()
    conn.execute(text(query))
    return [CleaningOrderDAO(
        id=order[0],
        objectName=order[1],
        description=order[2],
        deadline=order[3],
        status=order[4],
        supervisor_email=order[5]
    ) for order in orders]