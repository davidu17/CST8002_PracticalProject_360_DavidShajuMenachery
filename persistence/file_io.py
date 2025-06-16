import csv
import uuid
from model.record import Record
import os

def read_dataset(file_path):
    records = []
    try:
        with open(file_path, newline='', encoding='ISO-8859-1') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if i >= 100:
                    break
                rec = Record(
                    row['Sample No. \x96 No. d\x92échantillon'],
                    row['Region - Région'],
                    row['Function'],
                    row['Origin'],
                    row['Product'],
                    row['Date Sampled \x96 Date d\x92échantillonage'],
                    row['Type of Test'],
                    row['Component'],
                    row['Result - Résultat'],
                    row['Unit - Unité'],
                    row['Plan Code - Code du régime']
                )
                records.append(rec)
    except Exception as e:
        print("Error reading dataset:", e)
    return records

def write_dataset(records, folder='output/'):
    os.makedirs(folder, exist_ok=True)
    filename = folder + str(uuid.uuid4()) + ".csv"
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['SampleNo', 'Region', 'Function', 'Origin', 'Product',
                             'DateSampled', 'TestType', 'Component', 'Result', 'Unit', 'PlanCode'])
            for record in records:
                writer.writerow(record.to_list())
        return filename
    except Exception as e:
        print("Error writing dataset:", e)
        return None
