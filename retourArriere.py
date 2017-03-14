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

    # get the vertexes that don't have ancestors
    def possibleVertex(self):
        p = []
        for v in self.graph:
            if len(v) == 0:
                p.append(v)
        return p

    # def backtrack(G)
    #   for n in [possible vertex (no ancestor)]
    #       enlever n
    #       backtrack(G)
    #       rajouter n
    def backtrack(self):
        for v in self.possibleVertex():
            self.graph.pop(v)
            self.backtrack()




#g = Graph("test")
g = Graph("tp2-donnees/poset18-8c")
g.topologicalSort(True, True)