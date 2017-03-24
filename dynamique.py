from collections import defaultdict, deque
import datetime

# Class to represent a graph
class Graph:
    # creates a graph from a file
    def __init__(self, f):
        with open(f) as file:
            lines = file.readlines()

        self.mat = []
        self.longestChains = []

        self.V = int(lines[0].split(" ")[0])  # No. of vertices
        lines.pop(0)
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        for i in range(0, self.V):
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

    def vorace(self):
        L = []
        c = self.longestChain()
        while len(c) > 0:
            for v in c:
                self.removeVertice(v)
            L.append(c)
            c = self.longestChain()
        for u in self.graph:
            L.append(u)
        self.longestChains = L

    def floydFermetureTransitive(self):
        n = len(self.graph)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.graph[i].__contains__(k):
                        if self.graph[k].__contains__(j):
                            self.graph[i].append(j)

    # A : Array
    # v : A[2][4][1][2] -> every value is a dim index
    # returns value at that cell.
    def returnValue(self, A, v):
        return A

    # L : longest chains
    def createMat(self, L):
        v = []
        for l in L:
            v.append(len(l) + 1)

        length = 1
        for i in v:
            length *= i
        self.mat = [1] * length

    def dynamic(self, p, t):
        self.floydFermetureTransitive() # effectuer la fermeture transitive
        self.vorace()
        self.createMat(self.longestChains)

        v = [0] * len(self.longestChains) # represente l'index de l'elem que l'on accede
        for i in self.mat:
            i = self.longestChains - 1
            for c in self.longestChains:
                v[i]


    def calcLinExt(self, v):
        for i in v:
            print(str(i) + ' ')
        print('\n')



#g = Graph("tp2-donnees/poset18-8c")
g = Graph('ex')
g.dynamic(True, True)