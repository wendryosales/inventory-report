import pytest

from inventory_report.inventory.product import Product
from tests.factories.product_factory import ProductFactory


@pytest.fixture
def stock():
    return vars(ProductFactory())


def test_relatorio_produto(stock):
    produto = Product(**stock)

    assert produto.__repr__() == (
            f"O produto {produto.nome_do_produto}"
            f" fabricado em {produto.data_de_fabricacao}"
            f" por {produto.nome_da_empresa} com validade"
            f" até {produto.data_de_validade}"
            f" precisa ser armazenado {produto.instrucoes_de_armazenamento}."
        )
