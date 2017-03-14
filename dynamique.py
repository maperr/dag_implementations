from collections import defaultdict, deque
import math, datetime
import numpy

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
        for i in range(0,nbVertices):
            self.graph[i] = []

        for l in lines:
            l = l.replace('\n', '')
            v = int(l.split(" ")[0])
            e = int(l.split(" ")[1])
            self.addEdge(v, e)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # si on avait deja en memoire tout les arcs qui finissent a un certain vertex ce serait mieux
    # on devrait le faire a l'initialisation
    def getArcsEndingAt(self, v):
        r = []
        for u in self.graph:
            for d in self.graph[u]:
                if d == v:
                    r.append(u)
        return r

    def longestChain(self):
        pred = defaultdict(int)
        q = deque()
        for v in self.graph:
            pred[v] = -1
            if len(self.graph[v]) == 0:
                q.append(v)
        last = -1
        while len(q) != 0:
            u = q.pop()
            last = u
            vertexes = self.getArcsEndingAt(u)
            for v in vertexes:
                pred[v] = u
                #if q.__contains__(v):
                for i in q:
                    if i == v:
                        q.remove(v)
                        break
                q.append(v)
        c = []
        while last != -1:
            c.append(last)
            last = pred[last]
        return c

    def removeVertice(self, u):
        for v in self.graph:
            if self.graph[v].__contains__(u):
                self.graph[v].remove(u)
        self.graph.pop(u)


    def vorace(self):
        time_init = datetime.datetime.now()

        L = []
        c = self.longestChain()
        while len(c) > 0:
            for v in c:
                self.removeVertice(v)
            L.append(c)
            c = self.longestChain()
        for u in self.graph:
            L.append(u)

        return L

    def dynamique(self, p, t):
        L = self.vorace()

        # creation du tableau, on ajoute une dimension par chaine obtenue.
        # on commence par trouver la chaine la plus longue, ce sera le nb d'elem par dimension
        max = 0
        for c in L:
            if len(c) > max:
                max = len(c)
        max += 1
        arr = numpy.zeros(max)
        for dim in range(len(c) - 1):
            arr = numpy.expand_dims(arr, axis=1)
        for dim in arr:
            dim = numpy.zeros(max)
        x = 2


    # g = Graph("tp2-donnees/poset10-4a")
g = Graph("ex")
g.dynamique(True, True)