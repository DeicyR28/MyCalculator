from app.operations import addition, subtraction
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
        else:
            raise ValueError("Invalid operation: " + inputWords[0])


