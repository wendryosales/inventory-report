import pytest

from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


@pytest.fixture
def stock():
    return vars(ProductFactory())


def test_cria_produto(stock):
    produto = Product(**stock)

    assert produto.id == stock["id"]
    assert produto.nome_da_empresa == stock["nome_da_empresa"]
    assert produto.nome_do_produto == stock["nome_do_produto"]
    assert produto.data_de_fabricacao == stock["data_de_fabricacao"]
    assert produto.data_de_validade == stock["data_de_validade"]
    assert (
        produto.instrucoes_de_armazenamento
        == stock["instrucoes_de_armazenamento"]
    )
