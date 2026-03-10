from app.operations.operation import Operation

class Root(Operation):
    def __init__(self, operand1: float, operand2: float):
        """
        operand1: the number you want the root of (x)
        operand2: the root degree (n)
        """
        super().__init__(operand1, operand2)
        self.calcType = 'Root'

    def execute(self):
        if self.operand2 == 0:
            raise ValueError("Cannot calculate zeroth root")
        if self.operand1 < 0 and self.operand2 % 2 == 0:
            raise ValueError("Cannot calculate even root of a negative number")
        
        self.result = self.operand1 ** (1 / self.operand2)
        return self.result