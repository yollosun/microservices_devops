FROM python:3.10-slim-buster

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
RUN mkdir /cleaning_order

COPY cleaning_order_deadline_service.py /app
COPY cleaning_order/cleaning_order_repository.py /app/cleaning_order/cleaning_order_repository.py
COPY cleaning_order/cleaning_order_dao.py /app/cleaning_order/cleaning_order_dao.py
COPY cleaning_order/cleaning_order_status.py /app/cleaning_order/cleaning_order_status.py
COPY for_container.py /app

CMD ["python", "/app/cleaning_order_deadline_service.py"]