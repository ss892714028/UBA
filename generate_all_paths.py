from collections import defaultdict
import copy
from config import nodes, trans_matrix


class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        self.paths = []
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def helper(self, u, d, visited, path):
        visited[u] = True
        path.append(u)

        if u == d:
            self.paths.append(copy.deepcopy([nodes[i] for i in path]))
        else:
            for i in self.graph[u]:
                if not visited[i]:
                    self.helper(i, d, visited, path)
        path.pop()
        visited[u] = False

    def print_all_paths(self, s, d):

        visited = [False] * self.V
        path = []
        self.helper(s, d, visited, path)


def populate(trans_matrix):
    num_action = len(trans_matrix) - 1
    g = Graph(num_action)
    for i in range(num_action):
        for j in range(num_action):
            if trans_matrix[i][j] > 0:
                g.add_edge(i, j)

    return g


if __name__ == "__main__":
    g = populate(trans_matrix)
    g.print_all_paths(0, 3)
    print(g.paths)