import pytest
from app.operations.operation_factory import OperationFactory

class TestOperationFactory:
    @pytest.mark.parametrize(
        "command",
        [
            ("Add 1 1"),
            ("Subtract 1 1"),
            ("Power 1 1"),
            ("Multiply 1 1"),
            ("Divide 1 1")
        ]
    )
    def test_OperationFactory_create(self,command):
        op = OperationFactory.create_operation(command)
        inputWords = command.split()
        assert op.calcType == inputWords[0]
        assert op.operand1 == float(inputWords[1])
        assert op.operand2 == float(inputWords[2])