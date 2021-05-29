import sys
class Graph:
    # number of vertices
    __n = 0
    # adjacency matrix
    __g = [[0 for x in range(10)] for y in range(10)]
    # constructor
    def __init__(self, x):
        self.__n = x
        # initializing each element of the adjacency matrix to zero
        for i in range(0, self.__n):
            for j in range(0, self.__n):
                self.__g[i][j] = 0
        self.addEdge(0,4)
        self.addEdge(4,3)
        self.addEdge(1,3)
        self.addEdge(2,1)
        self.addEdge(2,0)
    def displayAdjacencyMatrix(self):
        print("\n\n Adjacency Matrix:", end="")
        # displaying the 2D array
        for i in range(0, self.__n):
            print()
            for j in range(0, self.__n):
                print("", self.__g[i][j], end="")
        print()
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
    def removeEdge(self, x, y):
        # checks if the vertex exists in the graph
        if (x >= self.__n) or (y >= self.__n):
            print("Vertex does not exists !")
        # checks if the vertex is connecting to itself
        if (x == y):
            print("Same Vertex !")
        else:
            # remove directed edge
            self.__g[x][y] = 0
    def reset_graph(self,x):
        self.__init__(x)

def menu():
    print(">>> Select an option from below <<<")
    print("1) Add An Edge ")
    print("2) Remove An Edge ")
    print("3) Reset the graph")
    print("4) End Program")


obj = Graph(5)
print("The Default graph")
obj.displayAdjacencyMatrix()

while True:
    menu()
    val = int(input())
    if val == 1:
        print("Enter the directed edge to add based on the format below ")
        print(" __ to __")
        dari = int(input())
        ke = int(input())
        obj.addEdge(dari, ke)
        print("After adding new edge ")
        obj.displayAdjacencyMatrix()
       
    elif val == 2:
        print("Enter the directed edge to remove based on the format below ")
        print(" __ to __")
        dari = int(input())
        ke = int(input())
        obj.removeEdge(dari, ke)
        print("After removing  edge ")
        obj.displayAdjacencyMatrix()
      
    elif val == 3:
        print("Reset")
        obj.reset_graph(5)
        obj.displayAdjacencyMatrix()
      
    elif val == 4:
        print("Thank you for using our app")
        sys.exit()
        