# This algorithm works for graphs, sort the number of the nodes in graph in top sort 

from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # Dictionary containing adjacency list
        self.V = vertices # No. vertices

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topological_sort
    def topological_sort_util(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] =True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        # Push current vertyex to stack which stroes result
        stack.append(v)


    # The function  to do Toplogical Sort. It uses recursive
    # topological_sort_utl() -> Dfs algorithm
    def topological_sort(self):
        # Mark all vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store toplogical
        # sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        # Print contents of the stack
        print(stack[::-1]) # List in reverse order


# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print ("Following is a Topological Sort of the given graph")

# Function Call
g.topological_sort()


# Complexity: O(V+E) Axuliary space: O(V)
