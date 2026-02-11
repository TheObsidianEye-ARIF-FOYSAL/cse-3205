from calculator import Calculator

class ExpressionEvaluator:
    def __init__(self):
        self.calc = Calculator()

    def _tokenize(self, expression: str):
        """Return list of tokens: numbers (as floats), operators, and parentheses."""
        expression = expression.replace(" ", "")
        tokens = []
        number = ""

        for ch in expression:
            if ch.isdigit() or ch == '.':
                number += ch
            else:
                # if we have accumulated digits, flush them as a number
                if number != "":
                    # convert to float to support decimals
                    tokens.append(float(number))
                    number = ""
                # ch is operator or parenthesis
                if ch in "+-*/()":
                    tokens.append(ch)
                else:
                    raise ValueError(f"Unsupported character: {ch}")

        # flush last number
        if number != "":
            tokens.append(float(number))

        return tokens

    def _to_rpn(self, tokens):
        """Convert infix tokens to RPN (Reverse Polish Notation) using shunting-yard."""
        output_queue = []
        op_stack = []

        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        left_assoc = {'+': True, '-': True, '*': True, '/': True}

        for token in tokens:
            if isinstance(token, (int, float)):
                output_queue.append(token)
            elif token in precedence:
                while op_stack:
                    top = op_stack[-1]
                    if top in precedence and (
                        (left_assoc[token] and precedence[token] <= precedence[top]) or
                        (not left_assoc[token] and precedence[token] < precedence[top])
                    ):
                        output_queue.append(op_stack.pop())
                    else:
                        break
                op_stack.append(token)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                # pop until '('
                while op_stack and op_stack[-1] != '(':
                    output_queue.append(op_stack.pop())
                if not op_stack:
                    raise ValueError("Mismatched parentheses")
                op_stack.pop()  # remove '('
            else:
                raise ValueError(f"Unknown token: {token}")

        while op_stack:
            top = op_stack.pop()
            if top in ('(', ')'):
                raise ValueError("Mismatched parentheses")
            output_queue.append(top)

        return output_queue

    def _eval_rpn(self, rpn_tokens):
        """Evaluate RPN using Calculator methods. Returns float or int-compatible number."""
        stack = []

        for token in rpn_tokens:
            if isinstance(token, (int, float)):
                stack.append(token)
            elif token in ('+', '-', '*', '/'):
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                b = stack.pop()
                a = stack.pop()
                # use calculator methods (they work with floats too)
                if token == '+':
                    res = self.calc.add(a, b)
                elif token == '-':
                    res = self.calc.subtract(a, b)
                elif token == '*':
                    res = self.calc.multiply(a, b)
                elif token == '/':
                    res = self.calc.divide(a, b)
                stack.append(res)
            else:
                raise ValueError(f"Unsupported RPN token: {token}")

        if len(stack) != 1:
            raise ValueError("Invalid expression evaluation")

        return stack[0]

    def evaluate(self, expression: str):
        """
        Evaluate a math expression string using Calculator class for operations.
        Supports +, -, *, /, parentheses and floating-point numbers.
        """
        if not expression or expression.strip() == "":
            raise ValueError("Empty expression")

        tokens = self._tokenize(expression)
        rpn = self._to_rpn(tokens)
        result = self._eval_rpn(rpn)
        return result
