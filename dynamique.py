from collections import defaultdict, deque
import itertools
import copy
import datetime
import sys

def main(argv):
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

# Class to represent a graph
class Graph:
    # creates a graph from a file
    def __init__(self, f):
        with open(f) as file:
            lines = file.readlines()

        self.mat = []
        self.longestChains = []
        self.matrixIndexVector = []
        self.iteratorVector = []

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
        for l in L:
            l.insert(0,-1)
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
            v.append(len(l))

        length = 1
        for i in v:
            length *= i
        self.mat = [0] * length
        self.mat[0] = 1

    def dynamic(self, p, t):
        graph = copy.deepcopy(self.graph)

        time_init = datetime.datetime.now()
        self.vorace()
        self.graph = graph
        self.createMat(self.longestChains)
        self.floydFermetureTransitive() # effectuer la fermeture transitive

        # calculate the matrix index vector needed to get the matrix index from the vector indexes
        self.matrixIndexVector = [0] * len(self.longestChains)
        i = len(self.longestChains) - 1
        m = 1
        for c in reversed(self.longestChains):
            self.matrixIndexVector[i] = m
            m *= len(c)
            i -= 1

        # iterate through all the elements
        self.iteratorVector = [0] * len(self.longestChains)
        for i in range(len(self.longestChains)):
            n = len(self.longestChains[i])
            v = []
            for j in range(n):
                v.append(j)
            self.iteratorVector[i] = v
        for index in itertools.product(*self.iteratorVector):
            self.calcLinExt(list(index))

        time_end = datetime.datetime.now()
        time_delta = time_end - time_init
        if p:
            print(self.mat[-1])
        if t:
            print(time_delta)

    def getMatIndex(self, index):
        m = 0  # matrix index
        for c in range(len(self.matrixIndexVector)):
            m += self.matrixIndexVector[c] * index[c]
        return m

    def getMatValue(self, index):
        return self.mat[self.getMatIndex(index)]

    def calcLinExt(self, index):
        m = self.getMatIndex(index)

        if m == 0: # cas special: s'il s'agit du premier elem, on assigne 1 simplement
            self.mat[0] = 1
            return

        result = 0
        for i in range(len(index)):
            sub_graph = copy.deepcopy(index)
            sub_graph[i] -= 1
            if sub_graph[i] == -1: continue
            removed_vertex = self.longestChains[i][sub_graph[i]+1]
            sigma = 1
            for j in range(len(index)):
                if j == i: continue
                end_vertex = self.longestChains[j][sub_graph[j]]
                if self.graph[removed_vertex].__contains__(end_vertex):
                    sigma = 0
            if sigma == 1:
                result += self.getMatValue(sub_graph)
        self.mat[m] = result

    def prettyPrint(self, index, tab):
        s = ""
        for t in range(tab):
            s += "   "
        s += "m["
        for i in range(len(index)):
            s += str(self.longestChains[i][index[i]])
            s += " "
        s += "]"
        print(s)


#g = Graph("tp2-donnees/poset14-8g")
#g = Graph('ex')
#g.dynamic(True, True)