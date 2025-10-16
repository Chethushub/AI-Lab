import itertools
import re
import pandas as pd


def truth_table(expression):
    # Extract variables (capital letters only)
    variables = sorted(set(re.findall(r'\b[A-Z]\b', expression)))

    if not variables:
        print("No propositional variables found (use uppercase like A, B, C).")
        return

    print(' | '.join(variables) + ' | Result')
    print('-' * (6 * len(variables) + 10))

    # Generate truth values
    for values in itertools.product([False, True], repeat=len(variables)):
        env = dict(zip(variables, values))
        expr_eval = expression
        for var, val in env.items():
            expr_eval = expr_eval.replace(var, str(val))
        try:
            result = eval(expr_eval)
        except Exception as e:
            print("Error evaluating:", expression, "-", e)
            return
        truth_values = [str(v).ljust(5) for v in values]
        print(' | '.join(truth_values) + ' | ' + str(result).ljust(5))





# variables = ['Q', 'P', 'R']


# rows = []
# for q, p, r in itertools.product([False, True], repeat=3):
#     kb1 = (not q or p)         
#     kb2 = (not p or (not q))    
#     kb3 = (q or r)              
#     kb_true = kb1 and kb2 and kb3  
#     row = {
#         'Q': q,
#         'P': p,
#         'R': r,
#         'Q -> P': kb1,
#         'P -> not Q': kb2,
#         'Q or R': kb3,
#         'KB True': kb_true
#     }
#     rows.append(row)


# truth_table = pd.DataFrame(rows)
# print(truth_table)




# variables = ['A', 'B', 'C']


# rows = []
# for a, b, c in itertools.product([False, True], repeat=3):
#     alpha = (a or b)
#     kb_clause1 = (a or c)
#     kb_clause2 = (b or (not c))
#     kb = kb_clause1 and kb_clause2
#     row = {
#         'A': a,
#         'B': b,
#         'C': c,
#         'A or C': kb_clause1,
#         'B or not C': kb_clause2,
#         'KB': kb,
#         'alpha': alpha
#     }
#     rows.append(row)

# truth_table = pd.DataFrame(rows)
# print(truth_table)
