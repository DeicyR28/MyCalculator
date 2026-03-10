from app.operations.operation import Operation

class IntegerDivision(Operation):
    def __init__(self, operand1: float, operand2: float):
        super().__init__(operand1, operand2)
        self.calcType = 'IntegerDivide'

    def execute(self):
        if self.operand2 == 0:
            raise ValueError("Cannot divide by zero")

        self.result = self.operand1 // self.operand2
        return self.result