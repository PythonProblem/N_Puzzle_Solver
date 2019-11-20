import random
from algorithms.tree_search import Node
from algorithms.bfs import search as bfs_search
from algorithms.manhattan_distance import search as man_search
from algorithms.misplaced_tiles import search as mis_search
from algorithms.custom import search1 as cus_search1
from algorithms.custom import search2 as cus_search2
from tkinter import *
import time
import matplotlib.pyplot as plt

random.seed(31)
searches = [bfs_search, mis_search, man_search, cus_search1]
names = ['BFS', 'Misplaced Tiles', 'Manhattan Distance', 'Custom Heuristic']

# searches = [cus_search1, cus_search2]
# names = ['Custom_1', 'Custom_2']

m, n = 3, 3
goal_state = []
for i in range(m):
    goal_state.append([i*m+j for j in range(n)])

search_length = len(searches)
max_steps = 30
l = [[] for i in range(search_length)]
files = [open('./analysis_data/'+names[i]+'.txt', 'w')
         for i in range(search_length)]
start_states = []

for steps in range(max_steps):

    start_node = Node(goal_state)
    visited = []
    for i in range(steps):
        visited.append(start_node)
        start_node.expand()
        children_nodes = [
            node for node in start_node.children if not start_node.is_same(node)]
        for child in children_nodes:
            f = 1
            for vis in visited:
                if(child.state == vis.state):
                    f = 0
                    break
            if(f):
                start_node = child
    start_state = start_node.state
    start_states.append(start_state)

    for i in range(search_length):
        search = searches[i]
        start_time = time.time()
        search(start_state, goal_state)
        end_time = time.time()
        l[i].append(end_time-start_time)
        files[i].write(str(end_time-start_time)+'\n')

states_map = [i for i in range(max_steps)]
states_map.sort(key=lambda x: l[0][x])

for i in range(search_length):
    plt.plot([j for j in range(max_steps)], [l[i][j] for j in states_map])

# for i in range(search_length):
#     plt.plot(l[i])


plt.legend(names)
plt.xlabel('Step size')
plt.ylabel('Time (s)')
plt.title('Comparison between different search functions')
plt.show()
# print(l)
