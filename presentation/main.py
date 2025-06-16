### presentation/main.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from model.record import Record
from persistence.file_io import read_dataset, write_dataset
from business.manager import RecordManager

def display_menu():
    print("\n=== Coumarin Data Manager ===")
    print("Program by David Shaju Menachery")
    print("1. Display All Records")
    print("2. Add Record")
    print("3. Edit Record")
    print("4. Delete Record")
    print("5. Reload Data")
    print("6. Save to File")
    print("0. Exit")

def get_record_input():
    return Record(
        input("Sample No.: "),
        input("Region: "),
        input("Function: "),
        input("Origin: "),
        input("Product: "),
        input("Date Sampled: "),
        input("Test Type: "),
        input("Component: "),
        input("Result: "),
        input("Unit: "),
        input("Plan Code: ")
    )

def main():
    FILE_PATH = "2013-14_coumarin_in_dried_beverage_mixes_breads_baking_mixes.csv"
    records = read_dataset(FILE_PATH)
    manager = RecordManager(records)

    while True:
        display_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            for i, rec in enumerate(manager.get_all()):
                print(f"{i+1}: {rec}")
        elif choice == "2":
            manager.add(get_record_input())
        elif choice == "3":
            idx = int(input("Index to edit: ")) - 1
            manager.update(idx, get_record_input())
        elif choice == "4":
            idx = int(input("Index to delete: ")) - 1
            manager.delete(idx)
        elif choice == "5":
            manager.reload(FILE_PATH, read_dataset)
            print("Data reloaded.")
        elif choice == "6":
            filename = write_dataset(manager.get_all())
            print("Data saved to:", filename)
        elif choice == "0":
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()