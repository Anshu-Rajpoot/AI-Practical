class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
    
    def f(self):
        return self.g + self.h

    def __lt__(self, other):
        return self.f() < other.f()

def heuristic(state):
    n = len(state)
    attacking_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                attacking_pairs += 1
    return attacking_pairs

def astar(initial_state):
    open_list = [Node(initial_state, None, 0, heuristic(initial_state))]
    closed_list = []
    while open_list:
        current_node = min(open_list)
        open_list.remove(current_node)
        closed_list.append(current_node)
        if current_node.h == 0:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]
        for next_state in generate_states(current_node.state):
            next_node = Node(next_state, current_node, current_node.g+1, heuristic(next_state))
            if next_node in closed_list:
                continue
            if next_node not in open_list:
                open_list.append(next_node)
            else:
                index = open_list.index(next_node)
                if next_node.g < open_list[index].g:
                    open_list[index] = next_node
    return None

def generate_states(state):
    n = len(state)
    states = []
    for i in range(n):
        for j in range(i+1, n):
            new_state = list(state)
            new_state[i], new_state[j] = new_state[j], new_state[i]
            states.append(tuple(new_state))
    return states

# Test the algorithm
initial_state = (0, 1, 2, 3, 4, 5, 6, 7)
solution_path = astar(initial_state)
if solution_path is None:
    print("No solution found")
else:
    print("Solution path:", solution_path)
    print("Number of steps:", len(solution_path)-1)

