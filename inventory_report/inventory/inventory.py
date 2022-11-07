import csv
import json

import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def reader(cls, file):
        if ".csv" in file:
            return cls._read_csv(file)
        elif ".json" in file:
            return cls._read_json(file)
        elif ".xml" in file:
            return cls._read_xml(file)

    @staticmethod
    def _read_csv(file):
        with open(file, "r") as csv_file:
            return list(csv.DictReader(csv_file))

    @staticmethod
    def _read_json(file):
        with open(file, "r") as json_file:
            return json.load(json_file)

    @staticmethod
    def _read_xml(file):
        with open(file, "r") as xml_file:
            return xmltodict.parse(xml_file.read())["dataset"]["record"]

    @classmethod
    def import_data(cls, file: str, type: str):
        if type == "simples":
            return SimpleReport.generate(cls.reader(file=file))
        elif type == "completo":
            return CompleteReport.generate(cls.reader(file))
