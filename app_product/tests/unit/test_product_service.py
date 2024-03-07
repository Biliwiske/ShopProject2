from uuid import uuid4, UUID

import pytest

from app.repositories.local_product_repo import ProductRepo
from app.services.product_service import ProductService


@pytest.fixture(scope='session')
def product_service() -> ProductService:
    return ProductService(ProductRepo(clear=True))


@pytest.fixture(scope='session')
def first_product_data() -> tuple[UUID, str, str, float]:
    return uuid4(), 'test_product_name_1', 'test_product_brand_1', 10000


@pytest.fixture(scope='session')
def second_product_data() -> tuple[UUID, str, str, float]:
    return uuid4(), 'test_product_name_2', 'test_product_brand_2', 20000


def test_empty_product(product_service: ProductService) -> None:
    assert product_service.get_product() == []


def test_create_first_product(
        first_product_data: tuple[UUID, str, str, float],
        product_service: ProductService
) -> None:
    order_id, name, brand, price = first_product_data
    product = product_service.create_product(order_id, name, brand, price)
    assert product.order_id == order_id
    assert product.name == name
    assert product.brand == brand
    assert product.price == price


def test_create_second_product(
        second_product_data: tuple[UUID, str, str, float],
        product_service: ProductService
) -> None:
    order_id, name, brand, price = second_product_data
    product = product_service.create_product(order_id, name, brand, price)
    assert product.order_id == order_id
    assert product.name == name
    assert product.brand == brand
    assert product.price == price


def test_get_product_full(
        first_product_data: tuple[UUID, str, str, float],
        second_product_data: tuple[UUID, str, str, float],
        product_service: ProductService
) -> None:
    products = product_service.get_product()
    assert len(products) == 2
    assert products[0].order_id == first_product_data[0]
    assert products[0].name == first_product_data[1]
    assert products[0].brand == first_product_data[2]
    assert products[0].price == first_product_data[3]

    assert products[1].order_id == second_product_data[0]
    assert products[1].name == second_product_data[1]
    assert products[1].brand == second_product_data[2]
    assert products[1].price == second_product_data[3]
