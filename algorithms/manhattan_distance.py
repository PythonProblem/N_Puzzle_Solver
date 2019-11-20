import heapq
import algorithms.best_first_seach as bfs

def search(state, goal_state):
    """A* tree search using manhattan distance heuristic"""

    def gn(node):
        return node.gn()

    tiles_places = []
    for i in range(len(goal_state)):
        for j in range(len(goal_state[i])):
            heapq.heappush(tiles_places, (goal_state[i][j], (i, j)))

    def hn(node):
        cost = 0
        for i in range(len(node.state)):
            for j in range(len(node.state[i])):
                tile_i, tile_j = tiles_places[node.state[i][j]][1]
                if i != tile_i or j != tile_j:
                    cost += abs(tile_i - i) + abs(tile_j - j)
        return cost

    def fn(node):
        return gn(node) + hn(node)

    return bfs.search(state, goal_state, fn)