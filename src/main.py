import itertools

class PropLogicSolver:
    def __init__(self, expression):
        self.expression = expression

        # Extract the unique variables
        self.variables = sorted(set(filter(str.isalpha, expression)))

    def evaluate(self, assignment):
        # Assign assignment value to each variable
        local_vars = {var: val for var, val in zip(self.variables, assignment)}

        # Replacing symbols
        expr = self.expression
        expr = expr.replace("¬", "~").replace("∧", "&").replace("∨", "|").replace("→", ">").replace("↔", "==")

        # Evaluate the expression
        return eval(expr, {}, local_vars)

    # Generate truth table for expression
    def truth_table(self):
        results = []
        print(" | ".join(self.variables) + " | " + self.expression)
        print("-" * (len(self.variables) * 4 + len(self.expression)))

        for values in itertools.product([True, False], repeat = len(self.variables)):
            result = self.evaluate(values)
            row = " | ".join('T' if v else 'F' for v in values) + " | " + ('T' if result else 'F')
            print(row)
            results.append((values, result))
        return results

    # Returns True if all results are True
    def check_tautology(self, results):
        return all(result for _, result in results)

    # Returns True if all results are False
    def check_contradiction(self, results):
        return all(not result for _, result in results)

solver = PropLogicSolver("(p ∨ q) → (r ∧ ¬s) ∨ t")
results = solver.truth_table()

print("\nTautology: ", solver.check_tautology(results))
print("Contradiction: ", solver.check_contradiction(results))