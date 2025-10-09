import random
import math
 

def random_state(n):
  
    return [random.randint(0, n - 1) for _ in range(n)]

def heuristic(state):
   
    h = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                h += 1
    return h

def print_board(state):
    
    n = len(state)
    for i in range(n):
        row = ["Q" if state[i] == j else "." for j in range(n)]
        print(" ".join(row))
    print()



def get_best_neighbor(state):
    """Return the best neighbor and its heuristic."""
    n = len(state)
    best = list(state)
    best_h = heuristic(state)

    for row in range(n):
        for col in range(n):
            if col != state[row]:
                new_state = list(state)
                new_state[row] = col
                new_h = heuristic(new_state)
                if new_h < best_h:
                    best = new_state
                    best_h = new_h
    return best, best_h

def hill_climbing(n, max_restarts=1000):
  
    for restart in range(max_restarts):
        current = random_state(n)
        current_h = heuristic(current)
        steps = 0

        print(f"\nRestart {restart + 1}: initial heuristic = {current_h}")
        while True:
            neighbor, neighbor_h = get_best_neighbor(current)
            steps += 1
            print(f"  Step {steps}: heuristic = {neighbor_h}")

            if neighbor_h >= current_h:
                
                break

            current, current_h = neighbor, neighbor_h

            if current_h == 0:
                print(f"\n Solved using Hill Climbing after {restart} restarts and {steps} steps!")
                print_board(current)
                return current

    print(" Hill Climbing failed to find a solution.")
    return None



def simulated_annealing(n, max_steps=10000, temp=1000.0, cooling=0.995):
   
    current = random_state(n)
    current_h = heuristic(current)
    T = temp

    print(f"\nStarting Simulated Annealing with initial heuristic = {current_h}")
    for step in range(1, max_steps + 1):
        if current_h == 0:
            print(f"\n Solved using Simulated Annealing in {step} steps!")
            print_board(current)
            return current

        
        row = random.randint(0, n - 1)
        col = random.randint(0, n - 1)
        while col == current[row]:
            col = random.randint(0, n - 1)
        new_state = list(current)
        new_state[row] = col
        new_h = heuristic(new_state)
        delta = new_h - current_h

        
        if delta < 0 or random.random() < math.exp(-delta / T):
            current, current_h = new_state, new_h

       
        if step % 100 == 0 or new_h < current_h:
            print(f"  Step {step}: heuristic = {current_h}, temperature = {T:.4f}")

        
        T *= cooling
        if T < 1e-6:
            T = 1e-6

    print(" Simulated Annealing failed to find a solution.")
    return None


if __name__ == "__main__":
    n = 4
    hill_climbing(n)
    simulated_annealing(n)
