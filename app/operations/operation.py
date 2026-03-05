from abc import ABC, abstractmethod

class Operation(ABC):
    operand1: float       # The first operand in the calculation
    operand2: float       # The second operand in the calculation
    result: float

    @abstractmethod
    def execute(self, a, b):
        pass

    