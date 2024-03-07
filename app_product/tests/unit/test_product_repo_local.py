# /tests/unit/test_printing_repo.py

from datetime import datetime
from uuid import uuid4, UUID

import pytest

from app.models.product import Product
from app.repositories.local_product_repo import ProductRepo

product_test_repo = ProductRepo()


def test_empty_list() -> None:
    assert product_test_repo.get_product() == []


def test_add_first_product() -> None:
    product = Product(product_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                        ord_id=uuid4(),
                        type='test_product_type_1',
                        create_date=datetime.now(),
                        product='test_product_product_1',
                        customer_info='test_customer_info_0')
    assert product_test_repo.create_product(product) == product


def test_add_first_product_repeat() -> None:
    product = Product(product_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                        ord_id=uuid4(),
                        type='test_product_type_1',
                        create_date=datetime.now(),
                        product='test_product_product_1',
                        customer_info='test_customer_info_0')
    # product_test_repo.create_product(product)
    with pytest.raises(KeyError):
        product_test_repo.create_product(product)


def test_get_product_by_id() -> None:
    product = Product(product_id=uuid4(),
                        ord_id=uuid4(),
                        type='test_product_type_1',
                        create_date=datetime.now(),
                        product='test_product_product_1',
                        customer_info='test_customer_info_0')
    product_test_repo.create_product(product)
    assert product_test_repo.get_product_by_id(product.product_id) == product


def test_get_product_by_id_error() -> None:
    with pytest.raises(KeyError):
        product_test_repo.get_product_by_id(uuid4())
