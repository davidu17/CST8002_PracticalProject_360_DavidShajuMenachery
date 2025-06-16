### business/manager.py

class RecordManager:
    def __init__(self, records=[]):
        self.records = records

    def add(self, record):
        self.records.append(record)

    def delete(self, index):
        if 0 <= index < len(self.records):
            del self.records[index]

    def update(self, index, record):
        if 0 <= index < len(self.records):
            self.records[index] = record

    def get_all(self):
        return self.records

    def get(self, index):
        return self.records[index] if 0 <= index < len(self.records) else None

    def reload(self, path, reader):
        self.records = reader(path)