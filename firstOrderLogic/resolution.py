

import re
from copy import deepcopy


class Literal:
    def __init__(self, pred, args, neg=False):
        self.pred = pred
        self.args = tuple(args)
        self.neg = neg

    def negate(self):
        return Literal(self.pred, self.args, not self.neg)

    def substitute(self, subs):
        new_args = []
        for a in self.args:
            while a in subs:
                a = subs[a]
            new_args.append(a)
        return Literal(self.pred, new_args, self.neg)

    def __eq__(self, other):
        return (self.pred == other.pred and self.args == other.args and self.neg == other.neg)

    def __hash__(self):
        return hash((self.pred, self.args, self.neg))

    def __repr__(self):
        return ("~" if self.neg else "") + f"{self.pred}({', '.join(self.args)})"

class Clause:
    def __init__(self, literals):
        self.literals = frozenset(literals)

    def substitute(self, subs):
        return Clause([lit.substitute(subs) for lit in self.literals])

    def is_empty(self):
        return len(self.literals) == 0

    def __hash__(self):
        return hash(self.literals)

    def __eq__(self, other):
        return self.literals == other.literals

    def __repr__(self):
        if self.is_empty():
            return "{}"
        return " | ".join(str(l) for l in self.literals)



def is_var(x):
    return x[0].islower()

def unify(x, y, subs):
    if subs is None:
        return None
    if x == y:
        return subs
    if is_var(x):
        return unify_var(x, y, subs)
    if is_var(y):
        return unify_var(y, x, subs)
    return None

def unify_var(v, x, subs):
    if v in subs:
        return unify(subs[v], x, subs)
    if x in subs:
        return unify(v, subs[x], subs)
    if occurs(v, x, subs):
        return None
    new = dict(subs)
    new[v] = x
    return new

def occurs(v, x, subs):
    if v == x:
        return True
    if is_var(x) and x in subs:
        return occurs(v, subs[x], subs)
    return False

def unify_literals(l1, l2):
    if l1.pred != l2.pred or l1.neg == l2.neg:
        return None
    subs = {}
    for a, b in zip(l1.args, l2.args):
        subs = unify(a, b, subs)
        if subs is None:
            return None
    return subs

def resolve(c1, c2):
    resolvents = set()
    for l1 in c1.literals:
        for l2 in c2.literals:
            subs = unify_literals(l1, l2)
            if subs is not None:
                new_literals = (c1.literals - {l1}) | (c2.literals - {l2})
                new_clause = Clause([lit.substitute(subs) for lit in new_literals])
                resolvents.add(new_clause)
    return resolvents



def resolution(kb):
    clauses = set(kb)
    new = set()

    while True:
        pairs = [(c1, c2) for c1 in clauses for c2 in clauses if c1 != c2]

        for (c1, c2) in pairs:
            resolvents = resolve(c1, c2)
            if Clause([]) in resolvents:
                print("\nEMPTY CLAUSE DERIVED → Hence proved.")
                return True
            new |= resolvents

        if new.issubset(clauses):
            return False

        clauses |= new


def parse_clause(s):
    parts = s.split("|")
    lits = []
    for p in parts:
        p = p.strip()
        neg = p.startswith("~")
        if neg: p = p[1:].strip()
        pred = p.split("(")[0]
        args = p[p.index("(")+1:p.index(")")].split(",")
        args = [a.strip() for a in args]
        lits.append(Literal(pred, args, neg))
    return Clause(lits)



kb_strings = [
    "~food(x) | likes(John,x)",
    "food(Apple)",
    "food(vegetables)",
    "~eats(y,z) | killed(y) | food(z)",
    "eats(Anil,Peanuts)",
    "alive(Anil)",
    "~eats(Anil,w) | eats(Harry,w)",
    "killed(g) | alive(g)",
    "~alive(k) | killed(k)",
]


goal = "~likes(John,Peanuts)"

kb = [parse_clause(s) for s in kb_strings]
kb.append(parse_clause(goal))

print("Clauses in KB:\n")
for c in kb:
    print("  ", c)


resolution(kb)
