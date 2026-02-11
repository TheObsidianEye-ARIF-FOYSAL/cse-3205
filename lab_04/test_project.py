import pytest
from project import ProjectCalculator

def test_final_price():
    pc = ProjectCalculator()
    result = pc.calculate_final_price(100, 15)
    assert result == 115  # 100 + (100*15/100)

def test_profit():
    pc = ProjectCalculator()
    assert pc.calculate_profit(5000, 3200) == 1800

def test_employee_score():
    pc = ProjectCalculator()
    score = pc.calculate_employee_score(80, 90, 5)
    expected = (80*0.4) + (90*0.5) + 5
    assert score == expected

def test_custom_expression():
    pc = ProjectCalculator()
    assert pc.calculate_custom_expression("4+9/3*2-1") == 9

def test_expression_with_zero_division():
    pc = ProjectCalculator()
    with pytest.raises(ValueError):
        pc.calculate_custom_expression("10/0 + 5")
