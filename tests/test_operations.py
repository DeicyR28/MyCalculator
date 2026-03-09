import pytest
from app.operations.addition import Addition
from app.operations.subtraction import Subtraction
from app.operations.multiply import Multiply
from app.operations.division import Division
from app.operations.modular import Modular
from app.operations.power import Power


class TestOperations:
    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (2,3,5),
            (4,5,9),
            (-1,-1,-2)
        ]
    )
    def test_addition_execute(self,a,b,expected):
        op = Addition(a,b)
        assert op.execute() == expected
        
    # Subtraction
    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (5,3,2),
            (10,5,5),
            (-2,-3,1)
        ]
    )
    def test_subtraction_execute(self, a, b, expected):
        op = Subtraction(a, b)
        assert op.execute() == expected

    # Multiply
    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (2,3,6),
            (4,5,20),
            (-2,3,-6)
        ]
    )
    def test_multiply_execute(self, a, b, expected):
        op = Multiply(a, b)
        assert op.execute() == expected

    # Division
    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (6,3,2),
            (10,2,5),
            (-9,3,-3)
        ]
    )
    def test_division_execute(self, a, b, expected):
        op = Division(a, b)
        assert op.execute() == expected

    # Modular
    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (5,3,2),
            (10,4,2),
            (7,7,0)
        ]
    )
    def test_modular_execute(self, a, b, expected):
        op = Modular(a, b)
        assert op.execute() == expected

    # Power
    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (2,3,8),
            (5,2,25),
            (3,0,1)
        ]
    )
    def test_power_execute(self, a, b, expected):
        op = Power(a, b)
        assert op.execute() == expected