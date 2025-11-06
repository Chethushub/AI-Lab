class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, premise, conclusion):
        self.rules.append((premise, conclusion))

    def forward_chain(self):
        added = True
        while added:
            added = False
            for premise, conclusion in self.rules:
                for fact in list(self.facts):
                    substitution = self.unify(premise, fact)
                    if substitution is not None:
                        new_fact = self.apply_substitution(conclusion, substitution)
                        if new_fact not in self.facts:
                            print(f"Derived {new_fact} from {fact} using {premise} -> {conclusion}")
                            self.facts.add(new_fact)
                            added = True
        return self.facts

    def unify(self, expr1, expr2):
        
        if type(expr1) != tuple or type(expr2) != tuple:
            return None
        if expr1[0] != expr2[0]:
            return None
        if len(expr1) != len(expr2):
            return None
        substitution = {}
        for a, b in zip(expr1[1:], expr2[1:]):
            if a.islower():  
                substitution[a] = b
            elif b.islower():
                substitution[b] = a
            elif a != b:
                return None
        return substitution

    def apply_substitution(self, expr, substitution):
        if type(expr) != tuple:
            return expr
        return (expr[0],) + tuple(substitution.get(arg, arg) for arg in expr[1:])



kb = KnowledgeBase()


kb.add_fact(("Man", "Marcus"))
kb.add_fact(("Pompeian", "Marcus"))


kb.add_rule(("Pompeian", "x"), ("Roman", "x"))
kb.add_rule(("Roman", "x"), ("Loyal", "x"))
kb.add_rule(("Man", "x"), ("Person", "x"))
kb.add_rule(("Person", "x"), ("Mortal", "x"))

print("=== Forward Reasoning Inference ===")
derived_facts = kb.forward_chain()

print("\nAll Derived Facts:")
for f in derived_facts:
    print(" -", f)


query = ("Mortal", "Marcus")
print("\nQuery:", query)

if query in derived_facts:
    print(" RESULT: Marcus is Mortal.")
else:
    print(" RESULT: Could not prove Marcus is Mortal.")
