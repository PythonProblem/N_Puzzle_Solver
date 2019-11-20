from copy import deepcopy

def is_same_state(state1, state2):
    for i in range(len(state1)):
        for j in range(len(state1[i])):
            if state1[i][j] != state2[i][j]:
                return False
    return True

def create_new_states(state):
    states = []

    zero_i = None
    zero_j = None

    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                zero_i = i
                zero_j = j
                break

    def add_swap(i, j):
        new_state = deepcopy(state)
        new_state[i][j], new_state[zero_i][zero_j] = new_state[zero_i][zero_j], new_state[i][j]
        states.append(new_state)

    if zero_i != 0:
        add_swap(zero_i - 1, zero_j)

    if zero_j != 0:
        add_swap(zero_i, zero_j - 1)

    if zero_i != len(state) - 1:
        add_swap(zero_i + 1, zero_j)

    if zero_j != len(state) - 1:
        add_swap(zero_i, zero_j + 1)

    return states


class Node:
    def __init__(self, state=None, parent=None, cost=0, depth=0, children=[]):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.depth = depth
        self.children = children

    def is_same(self, node):
        return is_same_state(self.state, node.state)

    def expand(self):
        new_states = create_new_states(self.state)
        self.children = []
        for state in new_states:
            self.children.append(Node(state, self, self.cost + 1, self.depth + 1))

    def parents(self):
        current_node = self
        while current_node.parent:
            yield current_node.parent
            current_node = current_node.parent

    def gn(self):
        costs = self.cost
        for parent in self.parents():
            costs += parent.cost

        return costs
