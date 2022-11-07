import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file):
        if not file.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(file, "r") as csv_file:
            return list(csv.DictReader(csv_file))
