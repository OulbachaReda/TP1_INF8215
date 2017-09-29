from heapqueue.binary_heap import BinaryHeap
import queue as Q
import copy
import time

from Graph import Graph

#from Kruskal import Kruskal

from Solution import Solution
from Solution import SOURCE


createdNodes = 0
exploredNodes = 0

class Node(object):
    def __init__(self, v, sol, heuristic_cost=0):
        self.v = v
        self.solution = Solution(sol)
        self.heuristic_cost = heuristic_cost
        global createdNodes
        createdNodes += 1

    def explore_node(self, heap):
        for nVisited in self.solution.not_visited:
            if nVisited == 0 and len(self.solution.not_visited) > 1:
                continue
            solution = Solution(self.solution)
            solution.add_edge(self.v, nVisited)
            #mst = Kruskal(solution.g)
            node = Node(nVisited, solution)  # mst.getMSTCost(solution, solution.visited[len(solution.visited) - 1]))
            heap.put(node)
        global exploredNodes
        exploredNodes += 1

    def __lt__(self, N):
        return isN2betterThanN1(N, self)


def main():
    g = Graph("N12.data")
    #import Kruskal  # prof
    #Kruskal.kruskal = Kruskal.Kruskal(g)
    heap = Q.PriorityQueue()
    s = Solution(g)
    n = Node(SOURCE, s)

    start_time = time.time()
    while len(n.solution.not_visited) != 0:
        n.explore_node(heap)
        n = heap.get()
    n.solution.print()
    end_time = time.time()
    elapsed_time = end_time-start_time
    print("Time elapsed: {} seconds, created nodes: {}, explored nodes: {}".format(elapsed_time, createdNodes, exploredNodes))


def isN2betterThanN1(N1, N2):
    fN1 = N1.heuristic_cost + N1.solution.cost
    fN2 = N2.heuristic_cost + N2.solution.cost
    if fN2 < fN1:
        return True
    return False


if __name__ == '__main__':
    main()
