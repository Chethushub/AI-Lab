GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def is_goal(state):
    return state == GOAL_STATE

def get_successors(state):
    zero_pos = state.index(0)
    successors = []
    for move in MOVES[zero_pos]:
        new_state = list(state)
        new_state[zero_pos], new_state[move] = new_state[move], new_state[zero_pos]
        successors.append(tuple(new_state))
    return successors

def dls(state, depth, path, path_set):
    if is_goal(state):
        return path
    if depth == 0:
        return None
    
    for succ in get_successors(state):
        if succ not in path_set:
            result = dls(succ, depth - 1, path + [succ], path_set | {succ})
            if result is not None:
                return result
    return None

def iddfs(start_state, max_depth=50):
    for depth in range(max_depth):
        print(f"Trying depth {depth}")
        path = dls(start_state, depth, [start_state], {start_state})
        if path is not None:
            return path
    return None

def print_path(path):
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

start_state = (0, 1, 3,
               4, 2, 6,
               7, 5, 8)

solution = iddfs(start_state, max_depth=30)
if solution:
    print(f"Solution found in {len(solution)-1} moves:")
    print_path(solution)
else:
    print("No solution found within the max depth limit.")
