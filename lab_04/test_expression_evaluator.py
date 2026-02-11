import pytest
from expression_evaluator import ExpressionEvaluator

def test_simple_expression():
    evaluator = ExpressionEvaluator()
    assert evaluator.evaluate("4+3") == 7

def test_operator_precedence():
    evaluator = ExpressionEvaluator()
    assert evaluator.evaluate("4+9/3*2-1") == 9  # 4 + 3*2 - 1 = 4 + 6 - 1

def test_expression_with_spaces():
    evaluator = ExpressionEvaluator()
    assert evaluator.evaluate(" 4 - 7 / 7 + 2 ") == 5  # 4 - 1 + 2 = 5

def test_subtraction_expression():
    evaluator = ExpressionEvaluator()
    assert evaluator.evaluate("10-3*2") == 4  # 10 - 6

def test_division_by_zero_in_expression():
    evaluator = ExpressionEvaluator()
    with pytest.raises(ValueError):
        evaluator.evaluate("5/0 + 2")
