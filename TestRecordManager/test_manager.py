from model.display_record import SimpleDisplayRecord, VerboseDisplayRecord

def test_polymorphic_display(self):
    record = Record("S2", "West", "Import", "India", "Spice", "2025-06-01",
                    "TestB", "Coumarin", "3.2", "µg/g", "P002")
    simple = SimpleDisplayRecord(record)
    verbose = VerboseDisplayRecord(record)

    self.assertIn("S2", simple.display())
    self.assertIn("SampleNo:", verbose.display())
