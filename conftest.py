from typing import Generator
import pytest
import datetime
from sqlalchemy import create_engine
from testcontainers.postgres import PostgresContainer
from cleaning_order.cleaning_order_repository import create_table, insert_order
from cleaning_order.cleaning_order_dao import CleaningOrderDAO
from cleaning_order.cleaning_order_status import CleaningOrderStatus


@pytest.fixture()
def postgres_container1() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer(image="postgres:latest") as container:
        container.start()
        yield container


@pytest.fixture()
def postgres_container() -> PostgresContainer:
    container = PostgresContainer(image="postgres:latest")
    container.get_container_host_ip = lambda: 'localhost'
    container.start()
    return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    return postgres_container.get_connection_url()

@pytest.fixture()
def order():
    return CleaningOrderDAO(
            objectName="test_objectName 1",
            description="test_description 1",
            deadline=datetime.datetime(2023, 2, 16, 10, 20, 12, 99000),
            status=CleaningOrderStatus.created.value,
            supervisor_email="test@gmail.com"
        )


@pytest.fixture(scope="function")
def conn_with_data(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    orders = [
        CleaningOrderDAO(
            objectName="test_objectName 1",
            description="test_description 1",
            deadline=datetime.datetime(2023, 2, 16, 10, 20, 12, 99000),
            status=CleaningOrderStatus.created.value,
            supervisor_email="test@gmail.com"

        ),
        CleaningOrderDAO(
            objectName="test_objectName 2",
            description="test_description 2",
            deadline=datetime.datetime(2023, 2, 16, 10, 20, 12, 99000),
            status=CleaningOrderStatus.created.value,
            supervisor_email="test@gmail.com"
        ),
        CleaningOrderDAO(
            objectName="test_objectName 3",
            description="test_description 3",
            deadline=datetime.datetime(2023, 2, 16, 10, 20, 12, 99000),
            status=CleaningOrderStatus.created.value,
            supervisor_email="test@gmail.com"
        ),
    ]
    for order in orders:
        insert_order(conn, order)
    return postgres_container.get_connection_url()

@pytest.fixture()
def get_data() -> list[int]:
    return [1,2,3,4,5]