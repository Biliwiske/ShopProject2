# /tests/unit/test_printing_model.py

from datetime import datetime
from uuid import uuid4

import pytest
from pydantic import ValidationError

from app.models.order import Order, OrderStatus


def test_order_creation():
    order_id = uuid4()
    status = OrderStatus.CREATE
    address_info = "address_info"
    customer_info = "customer_info"
    create_date = datetime.now()
    completion_date = None
    order_info = "order_info"

    order = Order(order_id=order_id, status=status, address_info=address_info, customer_info=customer_info,
                  create_date=create_date, completion_date=completion_date, order_info=order_info)

    assert dict(order) == {'order_id': order_id, 'status': status, 'address_info': address_info,
                           'customer_info': customer_info, 'create_date': create_date,
                           'completion_date': completion_date, 'order_info': order_info}


def test_order_date_required():
    with pytest.raises(ValidationError):
        Order(order_id=uuid4(),
              status=OrderStatus.CREATE,
              address_info="address_info",
              customer_info="customer_info",
              order_info="order_info")


def test_order_status_required():
    with pytest.raises(ValidationError):
        Order(order_id=uuid4(),
              address_info="address_info",
              customer_info="customer_info",
              create_date=datetime.now(),
              completion_date=None,
              order_info="order_info")
