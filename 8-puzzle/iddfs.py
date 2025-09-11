class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child_node):
        self.children.append(child_node)

def dls(node, target, depth, path, path_set):
    # Print value when visiting each node
    print(node.value, end=' ')
    if node.value == target:
        return path + [node.value]
    if depth == 0:
        return None
    for child in node.children:
        if child.value not in path_set:
            result = dls(child, target, depth - 1, path + [child.value], path_set | {child.value})
            if result is not None:
                return result
    return None

def iddfs(root, target, max_depth=50):
    for depth in range(max_depth + 1):
        print(f"\nSearching at depth: {depth}")
        path = dls(root, target, depth, [root.value], {root.value})
        if path is not None:
            return path
    return None

# Example Tree Construction
root = Node(1)
child2 = Node(2)
child3 = Node(3)
child4 = Node(4)
child5 = Node(5)
child6 = Node(6)
child7 = Node(7)
child8 = Node(8)
child9 = Node(9)
root.add_child(child2)
root.add_child(child3)
child2.add_child(child4)
child2.add_child(child5)
child3.add_child(child6)
child3.add_child(child7)
child4.add_child(child8)
child5.add_child(child9)

target_value = 7
solution = iddfs(root, target_value, max_depth=3)
print()

