# the code for DFS using the adjacency matrix
import networkx as nx
import matplotlib.pyplot as plt
import random

class Graph:
    adj = []
    
    # function to fill the matrix
    def __init__(self,v):
        self.v = v
        Graph.adj = [[0 for i in range(v)]
                     for j in range(v)]
        self.addedge(0,4) # edin -> jp
        self.addedge(1,3) # dub -> br
        self.addedge(2,0) # ista -> edin
        self.addedge(2,1) # ista -> dub
        self.addedge(4,3) # jp -> br 
        
    # add edge function [between 2 vertex]
    def addedge(self, start, e):
        # checks if the vertex exists in the graph
        if (start >= self.v) or (e >= self.v):
            print("Vertex does not exists !")
        # checks if the vertex is connecting to itself
        if (start == e):
            print("Same Vertex !")
        else:
            # creating directed edge
            self.adj[start][e] = 1
    
    # the DFS function itself
    def DFS(self, start, visited):
        # the current node is printed
        print("Start : " + str(start))
        # the current node is set as visited
        visited[start] = True
        # for every node in the graph
        for i in range(self.v):
           # print ("i = " + str(i))
            # the '1' indicates the presence of the edge in the matrix
                # where '1' means the edge between them is there
            # visited[i] = checks the label of the vertex
                # if the vertex is 0 (not visited)
                # if the vertext is 1 (visited)
            if (Graph.adj[start][i] == 1 and (not visited[i])):
                # to enter: must have an edge and that vertex is not visited
                self.DFS(i, visited)
            elif (Graph.adj[start][i] == 1 and (visited[i])):
                print("A cycle has formed")

    def cycle_printer(self,pred,visited,pred_local):
        map_list = ['Ed','Du','Is','Br','Jp'] 
        count = 0
        loop_c = 5
        cycle_list = []
        print("pred local is = " + str(pred_local))
        for c in range(5): # runs 0 to 4
            if(pred[c] == 999):
                count = count+1
        loop_c = loop_c - count
        print(loop_c)
        for xii in range (loop_c):
            max_val = -20
            for xi in range(5): # runs 0 to 4
                if ( ( (pred[xi] != 999) and ( (pred[xi] >= max_val) ) and (visited[xi] != -1) )) :
                    max_val = pred[xi]
                    index = xi
                    #print("max_val = " + str(max_val))
                    #print("xi = " + str(xi))
                    #print("pred[xi] = " + str(pred[xi]))
               
            print("final max_val = " + str(max_val))
            if(max_val != -20):
                cycle_list.append(map_list[index])
                pred[index] = 999
            #print(pred)
        cycle_list.append(cycle_list[0])
        print(cycle_list) #prints out the cycle man
        
    def cycle_det(self,start_vertex, visited,pred,lc,local_pos,pred_local):
        label_count = lc
        visited[start_vertex] = label_count
        if (label_count == 1):
            pred[start_vertex] = -10
            pred_local[start_vertex] = local_pos
        for i in range(self.v):
            # 1 [to see if there is an edge or not] && 0 [indicates tht it is not visited]
            if (Graph.adj[start_vertex][i] == 1 and (visited[i] == 0)): 
                local_pos = local_pos + 1
                pred[i] = start_vertex
                pred_local[i] = local_pos
                label_count = label_count + 1
                visited[i] = label_count
                #print ("Visited = " + str(visited))
                #print ("Predecessor = " + str(pred))
                #print ("\n")
                self.cycle_det(i,visited,pred,label_count,local_pos,pred_local)
            elif (Graph.adj[start_vertex][i] == 1 and (visited[i] != -1 )):  # check this != condition over here
                print ("Cycle formed")
                print ("Visited = " + str(visited))
                print ("Predecs = " + str(pred))
                print ("\n")
                self.cycle_printer(pred,visited,pred_local)

        visited[start_vertex] = -1 # labelled as -1 when it is no longer considered, when you have backtracked
         
    def random_edge(self):
        a = random.randint(0,4)
        b = random.randint(0,4)
        self.addedge(a, b)
    
    def drawgraph(self):
        G = nx.DiGraph()
        A = ['Ed', 'Du', 'Is', 'Br', 'Jp']

        for i in range(0,self.v):
            for j in range(0,self.v):
                if j == i:
                    continue
                if self.adj[i][j] == 1:
                    G.add_edges_from([(A[i],A[j])])

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_edges(G, pos, connectionstyle="arc3,rad=0.2",edgelist=G.edges(), edge_color='black')
        nx.draw_networkx_labels(G, pos)
        plt.show()
    
# v is the num_of_vertex in the graph
# e is the num_of_edge in the graph    

obj = Graph(5)
v = 5
visited = [0] * v
pred = [999] * v
pred_local = [-7] * v
lc = 1
local_pos = 1
print("'Ed','Du','Is','Br','Jp'")
# br --> ed (3,0)
# du --> is (1,2) 
# br --> is (3,2)
obj.addedge(0,2)
obj.drawgraph()
obj.cycle_det(2, visited, pred, lc,local_pos,pred_local)




















