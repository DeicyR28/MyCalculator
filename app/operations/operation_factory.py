from app.operations import addition, division, subtraction, multiply, modular, power
from app.operations.modular import Modular
from app.operations.operation import Operation

class OperationFactory:
    @staticmethod
    def create_operation(operation_type: str) -> Operation:
        inputWords = operation_type.split()
        if len(inputWords) != 3:
            raise ValueError("Invalid input: " + operation_type)
        op_name = inputWords[0].lower()
        try:
            operand1 = float(inputWords[1])
            operand2 = float(inputWords[2])
        except ValueError:
            raise ValueError("Operands must be numbers: " + " ".join(inputWords[1:]))
        if op_name == "add":
            return addition.Addition(operand1, operand2)
        
        if op_name == "subtract":   
            return subtraction.Subtraction(operand1, operand2)
        
        if op_name == "multiply":
            return multiply.Multiply(operand1, operand2)
        
        if op_name == "divide":
            return division.Division(operand1, operand2)
        
        if op_name == "modular":
            return modular.Modular(operand1, operand2)
        
        if op_name == "power":
            return power.Power(operand1, operand2)
        
        else:
            raise ValueError("Invalid operation: " + inputWords[0])
        
        


