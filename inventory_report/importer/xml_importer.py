import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file):
        if not file.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(file, "r") as xml_file:
            return xmltodict.parse(xml_file.read())["dataset"]["record"]
