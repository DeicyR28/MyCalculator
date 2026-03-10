from app.operations.operation import Operation

class Percent(Operation):
    def __init__(self, operand1: float, operand2: float):
        super().__init__(operand1, operand2)
        self.calcType = 'Percent'

    def execute(self):
        if self.operand2 == 0:
            raise ValueError("Cannot calculate percent with a denominator of zero")

        self.result = (self.operand1 / self.operand2) * 100
        return self.result