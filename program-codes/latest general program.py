import sys
import networkx as nx
import matplotlib.pyplot as plt
import random

class Graph:
    # number of vertices
    __n = 0
    # adjacency matrix
    __g = [[0 for x in range(10)] for y in range(10)]
    hascycle = False
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
        self.hascycle = False # setting this as false, means it has no cycle in it lah
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
    def cycle_det(self, start_vertex, visited, pred, lc, local_pos, pred_local):
        label_count = lc
        visited[start_vertex] = label_count
        if label_count == 1:
            pred[start_vertex] = -10
            pred_local[start_vertex] = local_pos
        for i in range(self.__n):
            # 1 [to see if there is an edge or not] && 0 [indicates tht it is not visited]
            if Graph.__g[start_vertex][i] == 1 and (visited[i] == 0):
                local_pos = local_pos + 1
                pred[i] = start_vertex
                pred_local[i] = local_pos
                label_count = label_count + 1
                visited[i] = label_count
                self.cycle_det(i, visited, pred, label_count, local_pos, pred_local)
            elif Graph.__g[start_vertex][i] == 1 and (visited[i] != -1):  # check this != condition over here
                print("\nCycle detected :")
                self.hascycle = True
                self.print_cycle(visited, i)
        visited[start_vertex] = -1  # labelled as -1 when it is no longer considered, when you have backtracked
    def print_cycle(self, visited, i):
        map_list = ['Ed', 'Du', 'Is', 'Br', 'Jp']
        #print(i)
        count = [False] * self.__n
        cycle = [-1] * self.__n
        reach = 0
        max = 0
        num = 0
        for m in range(self.__n):
            for j in range(self.__n):
                if visited[j] >= max and count[j] == False:
                    max = visited[j]
                    num = j
                    #print("num", num)
            if num == i:
                reach = 1
            count[num] = True
            for k in range(self.__n):
                if cycle[k] == -1:
                    cycle[k] = num
                    break
            max = -1
            if reach == 1:
                break
        #print(cycle)
        for p in range(4, -1, -1):
            if cycle[p] != -1:
                print(map_list[cycle[p]], "-->", end=" ")
        for p in range(4, -1, -1):
            if cycle[p] != -1:
                print(map_list[cycle[p]])
                break
    
    # show this to the boys 
    def add_rand_Edge(self,x,y):
        if ( ((x >= self.__n) or (y >= self.__n)) == False ): 
            if ( (x == y) == False ):
                 self.__g[x][y] = 1
                 #print("   Edge between " + str(x) + " and " + str(y) + " is added.")  
    
    def random_edge(self):
        a = random.randint(0,4)
        b = random.randint(0,4)
        self.add_rand_Edge(a, b)

def main_menu():
    print(">>> Select an option from below <<<")
    print("1) Add An Edge ")
    print("2) Remove An Edge ")
    print("3) Reset the graph")
    print("4) Cycle Detection")
    print("5) End Program")

def map_menu():
    print("\nRefer to this table to key in the number")
    print("       0) Edinburgh    3) Brussels")
    print("       1) Dublin       4) Jaipur")
    print("       2) Istanbul")

v = 5
obj = Graph(v)
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
        obj.displayAdjacencyMatrix()
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
        print(">> Cycle detection process has started << ")
        visited = [0] * v
        pred = [999] * v
        pred_local = [-7] * v
        lc = 1
        local_pos = 1
        for xii in range(5):
            obj.cycle_det(xii, visited, pred, lc, local_pos, pred_local)
            if (obj.hascycle == False):
                print("No cycle detected, random edges will be added!!")
            while(obj.hascycle == False):
                obj.random_edge()
                obj.cycle_det(xii, visited, pred, lc, local_pos, pred_local)
        print("\n")
        obj.drawgraph()
      
    elif val == 5:
        print("Thank you for using our app")
        sys.exit()
             
    
        
        
        
        
        
        
        
        
        
        
        
        