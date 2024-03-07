# /tests/integration/app_repositories/test_db_delivery_repo.py

from datetime import datetime
from uuid import UUID, uuid4

import pytest

from app.models.product import Product
from app.repositories.db_product_repo import ProductRepo


@pytest.fixture()
def product_repo() -> ProductRepo:
    repo = ProductRepo()
    return repo


@pytest.fixture(scope='session')
def product_id() -> UUID:
    return uuid4()


@pytest.fixture(scope='session')
def first_product() -> Product:
    return Product(product_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                    order_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                    name='Ipad Air 3', brand='Iphone',
                    price=30000, created_at=datetime.now())


@pytest.fixture(scope='session')
def second_product() -> Product:
    return Product(product_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
                    order_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
                   name='Iphone 16 pro max ultra deluxe edition', brand='Iphone',
                   price=300000, created_at=datetime.now())


# def test_empty_list(product_repo: ProductRepo) -> None:
#     product_repo.delete_all_product()
#     assert product_repo.get_product() == []


def test_add_first_product(first_product: Product, product_repo: ProductRepo) -> None:
    assert product_repo.create_product(first_product) == first_product


def test_add_first_product_repeat(first_product: Product, product_repo: ProductRepo) -> None:
    with pytest.raises(KeyError):
        product_repo.create_product(first_product)


def test_get_product_by_id(first_product: Product, product_repo: ProductRepo) -> None:
    assert product_repo.get_product_by_id(first_product.product_id) == first_product


def test_get_product_by_id_error(product_repo: ProductRepo) -> None:
    with pytest.raises(KeyError):
        product_repo.get_product_by_id(uuid4())


def test_add_second_product(first_product: Product, second_product: Product, product_repo: ProductRepo) -> None:
    assert product_repo.create_product(second_product) == second_product
    products = [product_repo.get_product_by_id(first_product.product_id),
                 product_repo.get_product_by_id(second_product.product_id)]
    assert len(products) == 2
    assert products[0] == first_product
    assert products[1] == second_product


def test_delete_created_order(first_product: Product, second_product: Product, product_repo: Product) -> None:
    assert product_repo.delete_product_by_id(first_product.product_id) == first_product
    assert product_repo.delete_product_by_id(second_product.product_id) == second_product
