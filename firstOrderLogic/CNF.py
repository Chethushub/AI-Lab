from sympy import symbols
from sympy.logic.boolalg import to_cnf
from sympy.logic.inference import satisfiable
from sympy.abc import x, y


Animal_y = symbols('Animal_y')
Loves_xy = symbols('Loves_xy')
Loves_yx = symbols('Loves_yx')


formula = (~(Animal_y >> Loves_xy)) | Loves_yx


cnf_formula = to_cnf(formula, simplify=True)


print("Original formula:")
print(formula)
print("\nConverted to CNF:")
print(cnf_formula)
