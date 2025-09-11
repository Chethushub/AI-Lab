import heapq

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

def manhattan_distance(state):
    distance = 0
    for index, value in enumerate(state):
        if value == 0:
            continue
        # Goal position
        goal_pos = value - 1
        current_row, current_col = divmod(index, 3)
        goal_row, goal_col = divmod(goal_pos, 3)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_successors(state):
    zero_pos = state.index(0)
    successors = []
    for move in MOVES[zero_pos]:
        new_state = list(state)
        new_state[zero_pos], new_state[move] = new_state[move], new_state[zero_pos]
        successors.append(tuple(new_state))
    return successors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def a_star(start_state):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start_state), 0, start_state))
    
    came_from = {}
    g_score = {start_state: 0}
    
    while open_set:
        _, current_cost, current = heapq.heappop(open_set)
        
        if current == GOAL_STATE:
            return reconstruct_path(came_from, current)
        
        for neighbor in get_successors(current):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(neighbor)
                heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))
    return None

def print_path(path):
    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

# Example usage:
start_state = (0, 1, 3,
               4, 2, 6,
               7, 5, 8)

solution = a_star(start_state)
if solution:
    print(f"Solution found in {len(solution)-1} moves:")
    print_path(solution)
else:
    print("No solution found.")
