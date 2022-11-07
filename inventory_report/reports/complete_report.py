from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        output = ""

        products_by_company = Counter(
            company["nome_da_empresa"] for company in products
        )
        for company, count in products_by_company.items():
            output += f"- {company}: {count}\n"

        return (
            super().generate(products)
            + "\nProdutos estocados por empresa:\n"
            + output
        )
