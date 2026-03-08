from abc import ABC, abstractmethod

class Operation(ABC):
    operand1: float       # The first operand in the calculation
    operand2: float       # The second operand in the calculation
    calcType: str | None = None
    result: float

    def __init__(self, operand1 : float, operand2 : float, calcType=None, result=None):
        self.operand1 = operand1
        self.operand2 = operand2
        self.calcType = calcType
        self.result = result

    def __str__(self) -> str:
        return f"{self.calcType}({self.operand1}, {self.operand2}) = {self.result}"
    
    @abstractmethod
    def execute(self, a, b):
        pass

    def to_dict(self):
        return {
            "operand1": self.operand1,
            "operand2": self.operand2,
            "calcType": self.calcType,
            "result": self.result
        }
    
    # @classmethod
    # def from_dict(cls, data: dict):
        
    #     return cls(
    #         operand1=data["operand1"],
    #         operand2=data["operand2"],
    #         calcType=data["calcType"],
    #         result=data.get("result")
    #     )
