import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def reader(self, file):
        if file.suffix == ".csv":
            return self._read_csv(file)

    def _read_csv(self, file):
        with open(file, "r") as csv_file:
            return list(csv.DictReader(csv_file))

    @classmethod
    def import_data(cls, file: str, type: str):
        if type == "simples":
            return SimpleReport.generate(cls.reader(file))
        elif type == "completo":
            return CompleteReport.generate(cls.reader(file))
