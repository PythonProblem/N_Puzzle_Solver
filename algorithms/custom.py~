import heapq
import algorithms.best_first_seach as bfs


def search1(state, goal_state):
    """A* tree search using custom distance heuristic"""

    def gn(node):
        return node.gn()

    tiles_places = []
    for i in range(len(goal_state)):
        for j in range(len(goal_state[i])):
            heapq.heappush(tiles_places, (goal_state[i][j], (i, j)))
    # print(tiles_places)

    def hn(node):
        cost = 0
        m = len(node.state)
        n = len(node.state[0])
        for i in range(m):
            for j in range(n):
                strength = node.state[i][j]
                tile_i, tile_j = tiles_places[node.state[i][j]][1]
                if i != tile_i or j != tile_j:
                    cost += (abs(tile_i - i) + abs(tile_j - j))*strength
        # print(cost)
        return cost

    def fn(node):
        return gn(node) + hn(node)

    return bfs.search(state, goal_state, fn)


def search2(state, goal_state):
    """A* tree search using custom distance heuristic"""

    def gn(node):
        return node.gn()

    tiles_places = []
    for i in range(len(goal_state)):
        for j in range(len(goal_state[i])):
            heapq.heappush(tiles_places, (goal_state[i][j], (i, j)))

    def hn(node):
        cost = 0
        m = len(node.state)
        n = len(node.state[0])
        for i in range(m):
            for j in range(n):
                strength = m*n - (i*m+j)
                tile_i, tile_j = tiles_places[node.state[i][j]][1]
                if i != tile_i or j != tile_j:
                    cost += (abs(tile_i - i) + abs(tile_j - j))*strength
        return cost

    def fn(node):
        return gn(node) + hn(node)

    return bfs.search(state, goal_state, fn)
