### model/record.py

class Record:
    def __init__(self, sample_no, region, function, origin, product, date_sampled,
                 test_type, component, result, unit, plan_code):
        self.sample_no = sample_no
        self.region = region
        self.function = function
        self.origin = origin
        self.product = product
        self.date_sampled = date_sampled
        self.test_type = test_type
        self.component = component
        self.result = float(result) if result else 0.0
        self.unit = unit
        self.plan_code = plan_code

    def to_list(self):
        return [self.sample_no, self.region, self.function, self.origin, self.product,
                self.date_sampled, self.test_type, self.component, self.result,
                self.unit, self.plan_code]

    def __str__(self):
        return f"SampleNo: {self.sample_no}, Product: {self.product}, Result: {self.result} {self.unit}"
