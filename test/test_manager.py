### test/test_manager.py

import unittest
from model.record import Record
from business.manager import RecordManager

class TestRecordManager(unittest.TestCase):
    def test_add_record(self):
        mgr = RecordManager()
        rec = Record("S1", "East", "Domestic", "Canada", "Bread", "2025-06-01",
                     "TestA", "Coumarin", "5.5", "µg/g", "P001")
        mgr.add(rec)
        self.assertEqual(len(mgr.get_all()), 1)
        self.assertEqual(mgr.get(0).sample_no, "S1")

if __name__ == '__main__':
    unittest.main()
