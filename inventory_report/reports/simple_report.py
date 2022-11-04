from collections import Counter
from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, inventory: list[dict]) -> str:

        oldest_date = min(
            inventory,
            key=lambda x: date.fromisoformat(x["data_de_fabricacao"]),
        )["data_de_fabricacao"]

        closest_date = min(
            [
                date.fromisoformat(product["data_de_validade"])
                for product in inventory
            ],
            key=lambda x: abs(x - date.today()),
        )

        company_bigger_stock = Counter(
            [product["nome_da_empresa"] for product in inventory]
        ).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {company_bigger_stock}"
        )


if __name__ == "__main__":
    inventory = [
        {
            "id": 1,
            "nome_do_produto": "Produto 1",
            "nome_da_empresa": "Empresa 1",
            "data_de_fabricacao": "2020-01-01",
            "data_de_validade": "2020-01-01",
            "numero_de_serie": "123456789",
            "instrucoes_de_armazenamento": "Em local seco",
        },
        {
            "id": 2,
            "nome_do_produto": "Produto 2",
            "nome_da_empresa": "Empresa 2",
            "data_de_fabricacao": "2020-01-01",
            "data_de_validade": "2020-01-01",
            "numero_de_serie": "123456789",
            "instrucoes_de_armazenamento": "Em local seco",
        },
        {
            "id": 2,
            "nome_do_produto": "Produto 2",
            "nome_da_empresa": "Empresa 2",
            "data_de_fabricacao": "2020-01-01",
            "data_de_validade": "2023-01-01",
            "numero_de_serie": "123456789",
            "instrucoes_de_armazenamento": "Em local seco",
        },
    ]
    print(SimpleReport.generate(inventory))
