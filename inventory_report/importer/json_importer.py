import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file):
        if not file.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(file, "r") as json_file:
            return json.load(json_file)
