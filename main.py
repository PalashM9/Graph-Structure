import math
import sys
from collections import defaultdict


class GraphTemplate(object):
    _nodes = []  # ! list of NodeTemplate ONLY
    _minPriorityQueue = []  # ! list of NodeTemplate ONLY

    def __init__(self):
        pass

   
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])



class NodeTemplate(object):
    # _label               #! string
    adjacentNodes = {}  # ! dict of pairs (NodeTemplate : integer)
    parent = None  # ! reference to NodeTemplate
    distance = math.inf  # ! number (float)

    def __init__(self):
        pass


    ################################################## Kruskal Algorithm starts here ###################################################################


class Graph:


    # Constructor
    # Creating emptyset - A
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Adding edge function
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # the function to check the index and set values
    def find(self, parent, index):
        if parent[index] == index:
            return index
        return self.find(parent, parent[index])

    # Union function in the pseudocode
    def apply_union(self, parent, set, x, y):
        u_value = self.find(parent, x)
        v_value = self.find(parent, y)
        if set[u_value] < set[v_value]:
            parent[u_value] = v_value
        elif set[u_value] > set[v_value]:
            parent[v_value] = u_value
        else:
            parent[v_value] = u_value
            set[u_value] += 1

    #  Applying Kruskal algorithm from the pseudocode provided by the slides
    def kruskal_algo(self):
        # Creating empty set
        A = []
        u_index, v_index = 0, 0
        # SORT-WEIGHTS(G.E)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        # foreach v in G.V :
        for node in range(self.V):
            # MAKE-SET(v)
            parent.append(node)
            rank.append(0)
        # foreach (u,v) in G.v_index :
        while v_index < self.V - 1:
            u, v, w = self.graph[u_index]
            u_index = u_index + 1
            set_u = self.find(parent, u)
            set_v = self.find(parent, v)
            # if SET(u) != SET(v) :
            if set_u != set_v:
                v_index = v_index + 1
                # A.add({(u,v)})
                A.append([u, v, w])
                # UNION(u,v)
                self.apply_union(parent, rank, set_u, set_v)
        # return A
        for u, v, optimumWeight in A:
            print("%d - %d: %d" % (u, v, optimumWeight))

    #function to provide inputs and perform the algorithm
    def perform_kruskal():
        g = Graph(6)
        g.add_edge(0, 1, 4)
        g.add_edge(0, 2, 4)
        g.add_edge(1, 2, 2)
        g.add_edge(1, 0, 4)
        g.add_edge(2, 0, 4)
        g.add_edge(2, 1, 2)
        g.add_edge(2, 3, 3)
        g.add_edge(2, 5, 2)
        g.add_edge(2, 4, 4)
        g.add_edge(3, 2, 3)
        g.add_edge(3, 4, 3)
        g.add_edge(4, 2, 4)
        g.add_edge(4, 3, 3)
        g.add_edge(5, 2, 2)
        g.add_edge(5, 4, 3)

        print(" ")
        print("Running Kruskal's Algorithm")
        g.kruskal_algo()
        print(" ")

    ################################################## Kruskal Algorithm ends here ###################################################################

    ################################################## Dijkstra Algorithm starts here ################################################################


# Initializing the Graph Class
class GraphD:
    # foreach u in G.V : u.dist = INFINITY, u.parent = NIL
    # Constructor of class
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    # function to add nodes
    def addNode(self, value):
        self.nodes.add(value)

    # function to add edges
    def addEdge(self, initial, final, distance):
        self.edges[initial].append(final)
        self.distances[(initial, final)] = distance

    # Implementing Dijkstra's Algorithm#er as per the pseudocode
    # G is a weighted graph and s(initial) is the chosen source
    def dijkstra(graph, initial):
        # creating initial set as empty
        visited = {initial: 0}
        path = defaultdict(list)

        # S stores nodes already processed
        nodes = set(graph.nodes)

        # while Q != emptySet :
        while nodes:
            minNode = None
            # u = EXTRACT-MIN(Q)
            for node in nodes:
                if node in visited:
                    # S = S.add(u) - adding u to S
                    if minNode is None:
                        minNode = node
                    elif visited[node] < visited[minNode]:
                        minNode = node
            if minNode is None:
                break

            nodes.remove(minNode)
            currentEfficient = visited[minNode]

            # foreach v in u.Neighbours : RELAX (u,v,w(u,v) )
            # check if it is possible to reach nodes, in a more efficient ways from u
            for edge in graph.edges[minNode]:
                optimumWeight = currentEfficient + graph.distances[(minNode, edge)]
                if edge not in visited or optimumWeight < visited[edge]:
                    visited[edge] = optimumWeight
                    path[edge].append(minNode)

        return visited, path

    # function to provide inputs and perform the algorithm
    def perform_dijkstra():
        createChart = GraphD()
        createChart.addNode("A")
        createChart.addNode("B")
        createChart.addNode("C")
        createChart.addNode("D")
        createChart.addNode("E")
        createChart.addNode("F")
        createChart.addNode("G")
        createChart.addEdge("A", "B", 3)
        createChart.addEdge("A", "C", 4)
        createChart.addEdge("B", "C", 5)
        createChart.addEdge("B", "D", 2)
        createChart.addEdge("B", "E", 6)
        createChart.addEdge("C", "F", 7)
        createChart.addEdge("D", "E", 1)
        createChart.addEdge("E", "G", 9)
        createChart.addEdge("F", "G", 8)

        print("Running Dijkstra's Algorithm")
        print(GraphD.dijkstra(createChart, "A"))

    ################################################## Dijkstra Algorithm ends here ################################################################


if __name__ == "__main__":

  

    Graph.perform_kruskal()
    GraphD.perform_dijkstra()