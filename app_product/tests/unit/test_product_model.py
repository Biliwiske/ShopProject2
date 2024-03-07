# /tests/unit/test_printing_model.py

from datetime import datetime
from uuid import uuid4, UUID


import pytest
from pydantic import ValidationError

from app.models.product import Product

product_id: UUID
order_id: UUID
name: str
brand: str
price: float
created_at: datetime


def test_product_creation():
    product_id = uuid4()
    order_id = uuid4()
    name = 'test_product_name_1'
    brand = 'test_product_brand_1'
    price = 10000
    created_at = datetime.now()

    product = Product(product_id=product_id, order_id=order_id, name=name, brand=brand, price=price,
                        created_at=created_at)

    assert dict(product) == {'product_id': product_id, 'order_id': order_id, 'name': name,
                              'brand': brand, 'price': price,
                              'created_at': created_at}


def test_product_date_required():
    with pytest.raises(ValidationError):
        Product(product_id=uuid4(),
                 order_id=uuid4(),
                 name='test_product_name_1',
                 brand='test_product_brand_1',
                 price=10000)


def test_product_order_id_required():
    with pytest.raises(ValidationError):
        Product(product_id=uuid4(),
                 name='test_product_name_1',
                 brand='test_product_brand_1',
                 price=10000,
                 created_at=datetime.now())
