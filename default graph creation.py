
class Graph:
    # number of vertices as in number of cities
    __n = 0
    # adjacency matrix is created
    __g = [[0 for x in range(10)] for y in range(10)]
   
    # constructor for Graph class, sets it all to 0s
    def __init__(self, x):
        self.__n = x
        # initializing each element of the adjacency matrix to zero
        for i in range(0, self.__n):
            for j in range(0, self.__n):
                self.__g[i][j] = 0
    
    # displaying the 2D array            
    def displayAdjacencyMatrix(self):
        print("\nAdjacency Matrix:", end="")
        for i in range(0, self.__n):
            print()
            for j in range(0, self.__n):
                print("", self.__g[i][j], end="")

    def addEdge(self, x, y):
        # checks if the vertex exists in the graph
        if (x >= self.__n) or (y >= self.__n):
            print("Vertex does not exists !")
        # checks if the vertex is connecting to itself
        if (x == y):
            print("Same Vertex !")
        else:
            # creating directed edge
            self.__g[x][y] = 1

#    def randEdge_adder(self,x,y)


default_graph = Graph(5)

default_graph.addEdge(0, 4)
default_graph.addEdge(4, 3)
default_graph.addEdge(1, 3)
default_graph.addEdge(2, 1)
default_graph.addEdge(2, 0)

print("\nThe adjacency graph for the default matrix")
default_graph.displayAdjacencyMatrix()




