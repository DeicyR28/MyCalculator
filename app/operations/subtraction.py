from app.operations.operation import Operation

class Subtraction(Operation):
    def __init__(self, operand1: float, operand2: float):
        super().__init__(operand1,operand2)
        self.calcType = 'Substract'

    def execute(self):
        self.result = self.operand1 - self.operand2
        return self.result