from collections import defaultdict, deque
import math, datetime

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
                if q.__contains__(v):
                    q.remove(v)
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


    def vorace(self, p, t):
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

        # approximation du nombre d'extensions lineaires
        # TODO: log est en base 2!
        h = 0
        for c in L:
            h = h + ((len(c)/self.V )* math.log((len(c)/self.V)))
        n = self.V # n est le nombre de sommets
        g = math.pow(2,0.5 * h * n)

        time_end = datetime.datetime.now()
        time_delta = time_end - time_init

        if p:
            print(g)
        if t:
            print(time_delta)


# g = Graph("tp2-donnees/poset10-4a")
g = Graph("test")
g.vorace(True, True)