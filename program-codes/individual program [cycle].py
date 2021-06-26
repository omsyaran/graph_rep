import sys
import networkx as nx
import matplotlib.pyplot as plt
import random

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
        print("\nAdjacency Matrix:", end="")
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
    def drawgraph(self):
        G = nx.DiGraph()
        A = ['Ed', 'Du', 'Is', 'Br', 'Jp']

        for i in range(0,self.__n):
            for j in range(0,self.__n):
                if j == i:
                    continue
                if self.__g[i][j] == 1:
                    G.add_edges_from([(A[i],A[j])])

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_edges(G, pos, connectionstyle="arc3,rad=0.2",edgelist=G.edges(), edge_color='black')
        nx.draw_networkx_labels(G, pos)
        plt.show()
    def reset_graph(self,x):
        self.__init__(x)
    

#####################################################################
       

    def cycle_det(self,start_vertex, visited,pred,lc):
        label_count = lc
        visited[start_vertex] = label_count
        for i in range(self.__n):
            if (Graph.__g[start_vertex][i] == 1 and (visited[i] == 0)):
                pred[i] = visited[start_vertex]
                label_count = label_count + 1
                visited[i] = label_count
                #print ("Visited = " + str(visited))
                #print ("Predecessor = " + str(pred))
                #print ("\n")
                self.cycle_det(i,visited,pred,label_count)
            elif (Graph.__g[start_vertex][i] == 1 and (visited[i] != -999 )): 
                print ("Cycle formed\n\n")
        visited[start_vertex] = -999
    
#####################################################################3   
    
    

def main_menu():
    print(">>> Select an option from below <<<")
    print("1) Add An Edge ")
    print("2) Remove An Edge ")
    print("3) Reset the graph")
    print("4) End Program")
    print("5) Function 2 [detect for cycle]")
    print("6) Print out the graph")
    print("7) Add random edge to the graph")

def map_menu():
    print("\nRefer to this table to key in the number")
    print("       0) Edinburgh    3) Brussels")
    print("       1) Dublin       4) Jaipur")
    print("       2) Istanbul")
  
obj = Graph(5)
print("\nThe Default graph")
obj.drawgraph()

while True:
    main_menu()
    val = int(input("Your option : "))
    if val == 1:
        print("\nAdd a directed edge based on the format below ")
        print("          'Vertex A' to 'Vertex B'")
        map_menu()
        dari = int(input("Vertex A : "))
        ke = int(input("Vertex B : "))
        obj.addEdge(dari, ke)
        print("After adding new edge ")
        obj.drawgraph()
       
    elif val == 2:
        print("\nRemove a directed edge based on the format below ")
        print("          'Vertex A' to 'Vertex B'")
        map_menu()
        dari = int(input("Vertex A : "))
        ke = int(input("Vertex B : "))
        obj.removeEdge(dari, ke)
        print("After removing the edge ")
        obj.displayAdjacencyMatrix()
        obj.drawgraph()
      
    elif val == 3:
        print("Reset back to the default graph")
        obj.reset_graph(5)
        obj.displayAdjacencyMatrix()
        obj.drawgraph()
      
    elif val == 4:
        print("Thank you for using our app")
        sys.exit()
    
    elif val == 5:
        print(">> Detection for cycle is being done now")  
        v = 5
        visited = [0] * v
        pred = [0] * v
        lc = 1
        obj.cycle_det(2, visited, pred, lc)
        print ("\n\n")
        obj.drawgraph()
    
    elif val == 6:
        obj.drawgraph()
    
    elif val == 7:
        a = random.randint(0,4)
        b = random.randint(0,4)
        print ("a = " + str(a) + "   b = " + str(b))
        obj.addEdge(a, b)
        obj.displayAdjacencyMatrix()
        obj.drawgraph()
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        