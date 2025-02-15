import itertools

class PropLogicSolver:
    def __init__(self, expression):
        self.expression = expression

        # Extract the unique variables
        self.variables = sorted(set(filter(str.isalpha, expression)))

    def evaluate(self, assignment):
        # Assign value to each variable
        local_vars = {var: val for var, val in zip(self.variables, assignment)}

        # Replacing symbols
        expr = self.expression
        expr = expr.replace("¬", "~").replace("∧", "&").replace("∨", "|").replace("→", ">").replace("↔", "==")

        return eval(expr, local_vars)

    # Generate truth table for expression
    def truth_table(self):
        print(" | ".join(self.variables) + " | " + self.expression)
        print("-" * (len(self.variables) * 4 + len(self.expression)))

        for values in itertools.product([True, False], repeat = len(self.variables)):
            result = self.evaluate(values)
            row = " | ".join('T' if v else 'F' for v in values) + " | " + ('T' if result else 'F')
            print(row)

solver = PropLogicSolver("(p ∨ q) → (r ∧ ¬s) ∨ t")

solver.truth_table()