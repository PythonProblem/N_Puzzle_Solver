import heapq
from algorithms.tree_search import Node

def search(state, goal_state, fn):
    """Best-first search"""

    queue = []
    entrance = 0
    current_node = Node(state)
    goal_node = Node(goal_state)

    visited = set()

    while not current_node.is_same(goal_node):
        current_state = current_node.state
        m = len(current_state)
        n = len(current_state[0])
        value = 0
        for i in range(m):
            for j in range(n):
                value += current_state[i][j]*(10**(i*m+j))
        visited.add(value)
        current_node.expand()
        for child in current_node.children:
            child_state = child.state
            m = len(child_state)
            n = len(child_state[0])
            value = 0
            for i in range(m):
                for j in range(n):
                    value += child_state[i][j]*(10**(i*m+j))
            if(value not in visited):
                queue_item = (fn(child), entrance, child)
                heapq.heappush(queue, queue_item)
                entrance += 1
        current_node = heapq.heappop(queue)[2]

    output = []
    output.append(current_node.state)
    for parent in current_node.parents():
        output.append(parent.state)
    output.reverse()

    return output
