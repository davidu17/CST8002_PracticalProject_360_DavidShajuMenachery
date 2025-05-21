"""
Course: CST8002 - Programming Language Research Project
Professor: Stanley Pieda
Due Date: May 25, 2025
Author: David Shaju Menachery
"""

class Record:
    """
    Represents a data record from the provided dataset.
    """

    def __init__(self, sample_no, region, function, origin, product, result, unit):
        self.sample_no = sample_no
        self.region = region
        self.function = function
        self.origin = origin
        self.product = product
        self.result = result
        self.unit = unit

    def __str__(self):
        return (f"{self.sample_no} | {self.region} | {self.function} | {self.origin} | "
                f"{self.product} | {self.result} {self.unit}")
