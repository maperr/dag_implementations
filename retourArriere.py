from collections import defaultdict
import datetime

# Class to represent a graph
class Graph:
    # creates a graph from a file
    def __init__(self, f):
        with open(f) as file:
            lines = file.readlines()

        # get nb of vertices
        nbVertices = int(lines[0].split(" ")[0])
        lines.pop(0)
        self.V = nbVertices  # No. of vertices
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.indegree = [0] * nbVertices
        self.result = 0
        for i in range(0, nbVertices):
            self.graph[i] = []

        for l in lines:
            l = l.replace('\n', '')
            v = int(l.split(" ")[0])
            e = int(l.split(" ")[1])
            self.addEdge(v, e)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v] += 1

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, res, visited):
        flag = False

        for i in range(self.V):
            if self.indegree[i] == 0 and visited[i] == False:
                for j in self.graph[i]:
                    self.indegree[j] -= 1 # DOES IT WORK???
                res.append(i)
                visited[i] = True
                self.topologicalSortUtil(res,visited)

                visited[i] = False
                res.pop()
                for j in self.graph[i]:
                    self.indegree[j] += 1
                flag = True

        if flag == False:
            self.result += 1

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self, p, t):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        res = []

        time_init = datetime.datetime.now()
        self.topologicalSortUtil(res, visited)
        time_end = datetime.datetime.now()
        time_delta = time_end - time_init

        if p:
            print(self.result)
        if t:
            print(time_delta)

g = Graph("test")
g.topologicalSort(True, True)