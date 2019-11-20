from algorithms.tree_search import Node

def search(state, goal_state):
    """Depth-first"""

    goal_node = Node(goal_state)
    visited = []

    def dfs(node):
        if node.is_same(goal_node):
            return node
        
        print(node.state)
        visited.append(node)
        node.expand()
        
        for child in node.children:
            result = None
            flag = False
            for node in visited:
                if(child.is_same(node)):
                    flag = True

            if(flag):
                continue
            
            result = dfs(child)

            if result is not None:
                return result

        return None

    answer = None
    while not answer:
        answer = dfs(Node(state))

    output = []
    output.append(answer.state)
    for parent in answer.parents():
        output.append(parent.state)
    output.reverse()

    return output