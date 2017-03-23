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
        self.result = 0  # No. of linear extensions
        self.V = nbVertices  # No. of vertices
        self.graph = defaultdict(list)  # dictionary containing adjacency List
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

    # get the vertexes that don't have ancestors
    def possibleVertex(self):
        p = []
        for v in self.graph:
            if len(self.graph[v]) == 0:
                p.append(v)
        return p

    def removeVertex(self, u):
        L = []
        self.graph.pop(u)
        for v in self.graph:
            if self.graph[v].__contains__(u):
                L.append(v)
                self.graph[v].remove(u)
        return L

    def reinsertVertex(self, u, pointedBy, pointsTo):
        self.graph[u] = pointsTo
        for v in pointedBy:
            self.graph[v].append(u)

    def backtrackutil(self):
        if len(self.possibleVertex()) == 0:
            self.result += 1
        else:
            for v in self.possibleVertex():
                pointsTo = self.graph[v]
                pointedBy = self.removeVertex(v)
                self.backtrackutil()
                self.reinsertVertex(v, pointedBy, pointsTo)

    def backtrack(self, p, t):
        time_init = datetime.datetime.now()
        self.backtrackutil()
        time_end = datetime.datetime.now()
        time_delta = time_end - time_init
        if p:
            print(self.result)
        if t:
            print(time_delta)


# g = Graph("ex")
g = Graph("tp2-donnees/poset10-4a")
g.backtrack(True, True)
