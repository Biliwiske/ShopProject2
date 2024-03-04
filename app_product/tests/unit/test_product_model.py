# /tests/unit/test_printing_model.py

from datetime import datetime
from uuid import uuid4, UUID


import pytest
from pydantic import ValidationError

from app.models.product import Product

product_id: UUID
ord_id: UUID
type: str
customer_info: str
create_date: datetime
product: str


def test_product_creation():
    product_id = uuid4()
    ord_id = uuid4()
    type = 'test_product_type_1'
    create_date = datetime.now()
    product = 'test_product_product_1'
    customer_info = 'test_customer_info_0'

    product = Product(product_id=product_id, ord_id=ord_id, type=type, create_date=create_date, product=product,
                        customer_info=customer_info)

    assert dict(product) == {'product_id': product_id, 'ord_id': ord_id, 'type': type,
                              'create_date': create_date, 'product': product,
                              'customer_info': customer_info}


def test_product_date_required():
    with pytest.raises(ValidationError):
        Product(product_id=uuid4(),
                 ord_id=uuid4(),
                 type='test_product_type_1',
                 product='test_product_product_1',
                 customer_info='test_customer_info_0')


def test_product_ord_id_required():
    with pytest.raises(ValidationError):
        Product(product_id=uuid4(),
                 type='test_product_type_1',
                 create_date=datetime.now(),
                 product='test_product_product_1',
                 customer_info='test_customer_info_0')
