# model/display_record.py
# Author: David Shaju Menachery
"""
This module demonstrates polymorphism via display formatting.
It defines an abstract DisplayRecord class and two subclasses
that override the display method differently.
"""

class DisplayRecord:
    """Base class for displaying a record. Must override display()."""
    def display(self):
        raise NotImplementedError("Subclasses should implement this method")

class SimpleDisplayRecord(DisplayRecord):
    """Displays a record in a simple format."""
    def __init__(self, record):
        self.record = record

    def display(self):
        """
        Returns a compact string with basic record info.
        Format: <Sample No.> - <Product>: <Result> <Unit>
        """
        return f"{self.record.sample_no} - {self.record.product}: {self.record.result} {self.record.unit}"

class VerboseDisplayRecord(DisplayRecord):
    """Displays a record using the full __str__ format of the Record object."""
    def __init__(self, record):
        self.record = record

    def display(self):
        """
        Returns the verbose string from the Record class.
        """
        return str(self.record)  # Full format from Record.__str__()

