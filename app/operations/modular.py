from app.operations.operation import Operation

class Modular(Operation):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self):
        result = self.operand1 % self.operand2
        return result