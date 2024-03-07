from uuid import uuid4, UUID

import pytest

from app.repositories.local_product_repo import ProductRepo
from app.services.product_service import ProductService


@pytest.fixture(scope='session')
def product_service() -> ProductService:
    return ProductService(ProductRepo(clear=True))


@pytest.fixture(scope='session')
def first_product_data() -> tuple[UUID, str, str, str]:
    return (uuid4(), 'test_product_type_1', 'test_product_product_1', 'test_product_customer_info_1')


@pytest.fixture(scope='session')
def second_product_data() -> tuple[UUID, str, str, str]:
    return (uuid4(), 'test_product_type_2', 'test_product_product_2', 'test_product_customer_info_2')


def test_empty_product(product_service: ProductService) -> None:
    assert product_service.get_product() == []


def test_create_first_product(
        first_product_data: tuple[UUID, str, str, str],
        product_service: ProductService
) -> None:
    ord_id, type, product, customer_info = first_product_data
    product = product_service.create_product(ord_id, type, product, customer_info)
    assert product.ord_id == ord_id
    assert product.type == type
    assert product.customer_info == customer_info
    assert product.product == product


def test_create_second_product(
        second_product_data: tuple[UUID, str, str, str],
        product_service: ProductService
) -> None:
    ord_id, type, product, customer_info = second_product_data
    product = product_service.create_product(ord_id, type, product, customer_info)
    assert product.ord_id == ord_id
    assert product.type == type
    assert product.customer_info == customer_info
    assert product.product == product


def test_get_product_full(
        first_product_data: tuple[UUID, str, str, str],
        second_product_data: tuple[UUID, str, str, str],
        product_service: ProductService
) -> None:
    products = product_service.get_product()
    assert len(products) == 2
    assert products[0].ord_id == first_product_data[0]
    assert products[0].type == first_product_data[1]
    assert products[0].product == first_product_data[2]
    assert products[0].customer_info == first_product_data[3]

    assert products[1].ord_id == second_product_data[0]
    assert products[1].type == second_product_data[1]
    assert products[1].product == second_product_data[2]
    assert products[1].customer_info == second_product_data[3]
