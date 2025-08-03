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

    # Added search record method 
    def search_records(self, conditions):
        """
        Filters records based on multiple conditions.
        Each condition is a dict: {'field': 'origin', 'operator': '==', 'value': 'India'}
        """
        def record_matches(record):
            for cond in conditions:
                field = cond['field']
                operator = cond['operator']
                value = cond['value']

                try:
                    record_value = getattr(record, field)
                except AttributeError:
                    print(f"Invalid field: {field}")
                    return False

                # Attempt numeric comparison
                try:
                    record_value = float(record_value)
                    value = float(value)
                except ValueError:
                    pass

                if operator == "==" and not record_value == value:
                    return False
                elif operator == "!=" and not record_value != value:
                    return False
                elif operator == "<" and not record_value < value:
                    return False
                elif operator == ">" and not record_value > value:
                    return False
                elif operator == "<=" and not record_value <= value:
                    return False
                elif operator == ">=" and not record_value >= value:
                    return False
            return True

        return list(filter(record_matches, self.records))
