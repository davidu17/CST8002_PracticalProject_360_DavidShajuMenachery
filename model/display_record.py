# model/display_record.py

class DisplayRecord:
    def display(self):
        raise NotImplementedError("Subclasses should implement this method")


class SimpleDisplayRecord(DisplayRecord):
    def __init__(self, record):
        self.record = record

    def display(self):
        return f"{self.record.sample_no} - {self.record.product}: {self.record.result} {self.record.unit}"


class VerboseDisplayRecord(DisplayRecord):
    def __init__(self, record):
        self.record = record

    def display(self):
        return str(self.record)  # Full format from Record.__str__()
