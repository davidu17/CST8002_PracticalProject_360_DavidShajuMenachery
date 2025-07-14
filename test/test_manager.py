### test/test_manager.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

print("Unit Test by David Shaju Menachery")

import unittest
from model.record import Record
from business.manager import RecordManager
from model.display_record import SimpleDisplayRecord, VerboseDisplayRecord


import unittest
from model.record import Record
from business.manager import RecordManager
from model.display_record import SimpleDisplayRecord, VerboseDisplayRecord

class TestRecordManager(unittest.TestCase):
    def test_add_record(self):
        mgr = RecordManager()
        rec = Record("S1", "East", "Domestic", "Canada", "Bread", "2025-06-01",
                     "TestA", "Coumarin", "5.5", "µg/g", "P001")
        mgr.add(rec)
        self.assertEqual(len(mgr.get_all()), 1)
        self.assertEqual(mgr.get(0).sample_no, "S1")

    def test_polymorphic_display(self):
        record = Record("S2", "West", "Import", "India", "Spice", "2025-06-01",
                        "TestB", "Coumarin", "3.2", "µg/g", "P002")
        simple = SimpleDisplayRecord(record)
        verbose = VerboseDisplayRecord(record)

        self.assertIn("S2", simple.display())
        self.assertIn("SampleNo:", verbose.display())

if __name__ == '__main__':
    unittest.main()
