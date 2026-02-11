from expression_evaluator import ExpressionEvaluator

class ProjectCalculator:
    def __init__(self):
        self.evaluator = ExpressionEvaluator()

    def calculate_final_price(self, base_price, tax_percent):
        expression = f"{base_price} + ({base_price} * {tax_percent} / 100)"
        return self.evaluator.evaluate(expression)

    def calculate_employee_score(self, attendance, performance, bonus):
        # Example formula: score = att*0.4 + per*0.5 + bonus
        expression = f"{attendance}*0 + {attendance}*0.4 + {performance}*0.5 + {bonus}"
        return self.evaluator.evaluate(expression)

    def calculate_profit(self, revenue, cost):
        expression = f"{revenue} - {cost}"
        return self.evaluator.evaluate(expression)

    def calculate_custom_expression(self, expr: str):
        return self.evaluator.evaluate(expr)


if __name__ == "__main__":
    project = ProjectCalculator()

    print("Final Price:", project.calculate_final_price(100, 15))  # Output: 115
    print("Profit:", project.calculate_profit(5000, 3200))        # Output: 1800
    print("Score:", project.calculate_employee_score(80, 90, 5))  # Example
    print("Custom:", project.calculate_custom_expression("4+9/3*2-1"))
