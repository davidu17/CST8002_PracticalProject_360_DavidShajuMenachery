"""
Course: CST8002 - Programming Language Research Project
Professor: Stanley Pieda
Due Date: May 25, 2025
Author: David Shaju Menachery
"""

import csv
from record import Record
import os

def load_records(filename, max_records=5):
    """
    Loads records from a CSV file and returns a list of Record objects.
    """
    records = []
    try:
        with open(filename, mode='r', encoding='cp1252') as file:
            reader = csv.DictReader(file)
            print(" CSV Columns Detected:", reader.fieldnames)

            for i, row in enumerate(reader):
                if i >= max_records:
                    break
                record = Record(
                    sample_no=row["Sample No. – No. d’échantillon"],
                    region=row["Region - Région"],
                    function=row["Function"],
                    origin=row["Origin"],
                    product=row["Product"],
                    result=row["Result - Résultat"],
                    unit=row["Unit - Unité"]
                )
                records.append(record)
    except FileNotFoundError:
        print(" File not found. Check the file name and location.")
    except KeyError as e:
        print(f" KeyError: Could not find column: {e}")
    except Exception as e:
        print(" General Error while loading records:", e)

    return records


def main():
    print(" Developer: David Shaju Menachery")
    print(" Working Directory:", os.getcwd())

    filename = "2013-14_coumarin_in_dried_beverage_mixes_breads_baking_mixes.csv"
    print(" Attempting to read file:", filename)

    records = load_records(filename)

    print(f"Number of records loaded: {len(records)}\n")

    if not records:
        print(" No records were loaded. Check the file contents or column names.")
    else:
        print(" Displaying sample records:\n")
        for record in records:
            print(record)


if __name__ == "__main__":
    main()
