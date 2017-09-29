import numpy as np

#kruskal = None


class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parent = np.array(range(n))
        self.rnk = np.zeros(n)

    def reset(self):
        self.parent = np.array(range(self.n))
        self.rnk = np.zeros(self.n)

    def add(self, e):
        x = self.find(e.source)
        y = self.find(e.destination)

        if self.rnk[x] > self.rnk[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
        if self.rnk[x] == self.rnk[y]:
            self.rnk[y] += 1

    def makes_cycle(self, e):
        return self.find(e.source) == self.find(e.destination)

    def find(self, u):
        if u != self.parent[u]:
            return self.find(self.parent[u])
        else:
            return u


class Kruskal(object):
    def __init__(self, g):
        self.uf = UnionFind(g.N)
        self.g = g
        
   
    def getMSTCost(self, sol, source):
        self.uf.reset()
        self.uf.add(self.g.get_edge(source, sol.visited[0]))
        # add edges from the existing solution
        for i in range(len(sol.visited) - 1):
            self.uf.add(self.g.get_edge(sol.visited[i], sol.visited[i+1])) 
        # get edges from not visited vertices
        # no need due to kruskal algorithm
        
        # compute kruskal on not visited vertices
        kruskalCost = 0
        for e in self.g.get_sorted_edges():
            if e.source in sol.visited and e.source is not source:
                continue
            if e.destination in sol.visited and e.destination is not source:
                continue
            if not self.uf.makes_cycle(e):
                self.uf.add(e)
                kruskalCost = kruskalCost + e.cost        
        return kruskalCost
            
                
                
		

