from algorithms.tree_search import Node
from collections import deque

def search(state, goal_state):
    """Breadth-first search"""
    queue = deque()
	
    current_node = Node(state)
    goal_node = Node(goal_state)

    queue.appendleft(current_node)
    visited = []

    while not current_node.is_same(goal_node) and len(queue)!=0:

        flag = True
        while(flag):
            if( len(queue) == 0 ):
                return []
            current_node = queue.pop()
            flag = False
            for node in visited:
                if(current_node.is_same(node)):
                    flag = True
                    break
        visited.append(current_node)
        current_node.expand()
        queue.extendleft(current_node.children)

    output = []
    output.append(current_node.state)
    for parent in current_node.parents():
        output.append(parent.state)
    output.reverse()

    return output