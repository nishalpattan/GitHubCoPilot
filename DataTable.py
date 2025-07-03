# util_lib.py
import csv
import statistics

class DataTable:
    def __init__(self, table: list[list[str]]):
        self.table = table

    @classmethod
    def load(cls, path: str) -> "DataTable":
        with open(path) as f:
            table = list(csv.reader(f))
        return cls(table)

    def mean(self, col_idx: int) -> float:
        return statistics.mean(float(row[col_idx]) for row in self.table)

    def stddev(self, col_idx: int) -> float:
        return statistics.stdev(float(row[col_idx]) for row in self.table)

    def save(self, path: str) -> None:
        with open(path, "w", newline="") as f:
            csv.writer(f).writerows(self.table)