import os
import pytest
from unittest.mock import patch
from app.calculator import Calculator
from app.operations.addition import Addition  # example operation

def test_calculator_addition():
    os.environ["HISTORY_FILE_NAME"] = "test_history.csv"  # set env var for test
    user_inputs = ["add 2 3", "exit"]

    with patch("builtins.input", side_effect=user_inputs):
        calc = Calculator()
        historyLen = len(calc.history)
        calc.start() 
        assert len(calc.history) == historyLen + 1
        op = calc.history[-1]
        assert isinstance(op, Addition)
        assert op.execute() == 5  # 2 + 3