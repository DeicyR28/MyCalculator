from abc import ABC, abstractmethod

class Operation(ABC):
    operand1: float       # The first operand in the calculation
    operand2: float       # The second operand in the calculation
    calcType: str | None = None
    result: float

    def __init__(self, operand1 : float, operand2 : float):
        self.operand1 = operand1
        self.operand2 = operand2
        self.calcType: str = ""
        self.result: float | None = None

    def __str__(self) -> str:
        return f"{self.calcType}({self.operand1}, {self.operand2}) = {self.result}"
    
    @abstractmethod
    def execute(self, a, b):
        pass