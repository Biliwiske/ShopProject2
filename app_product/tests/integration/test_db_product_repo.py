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
                    ord_id=UUID('31babbb3-5541-4a2a-8201-537cdff25fed'),
                    type='test_product_type_1', create_date=datetime.now(),
                    product='test_product_product_1', customer_info='test_customer_info_0')


@pytest.fixture(scope='session')
def second_product() -> Product:
    return Product(product_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
                    ord_id=UUID('45309954-8e3c-4635-8066-b342f634252c'),
                    type='test_product_type_2', create_date=datetime.now(),
                    product='test_product_product_2', customer_info='test_customer_info_1')


# def test_empty_list(product_repo: ProductRepo) -> None:
#     product_repo.delete_all_product()
#     assert product_repo.get_product() == []


def test_add_first_product(first_product: Product, product_repo: ProductRepo) -> None:
    assert product_repo.create_product(first_product) == first_product


def test_add_first_product_repeat(first_product: Product, product_repo: ProductRepo) -> None:
    with pytest.raises(KeyError):
        product_repo.create_product(first_product)


def test_get_product_by_id(first_product: Product, product_repo: ProductRepo) -> None:
    assert productument_repo.get_productument_by_id(first_productument.product_id) == first_productument


def test_get_productument_by_id_error(productument_repo: ProductRepo) -> None:
    with pytest.raises(KeyError):
        productument_repo.get_productument_by_id(uuid4())


def test_add_second_productument(first_productument: Product, second_productument: Product, productument_repo: ProductRepo) -> None:
    assert productument_repo.create_productument(second_document) == second_document
    documents = [document_repo.get_document_by_id(first_document.doc_id),
                 document_repo.get_document_by_id(second_document.doc_id)]
    assert len(documents) == 2
    assert documents[0] == first_document
    assert documents[1] == second_document


def test_delete_created_order(first_document: Product, second_document: Product, document_repo: Product) -> None:
    assert document_repo.delete_document_by_id(first_document.doc_id) == first_document
    assert document_repo.delete_document_by_id(second_document.doc_id) == second_document
