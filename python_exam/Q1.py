"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""
import pandas as pd
from heapq import heapify,heappop,heappush

class Graph:
    
    def __init__(self, connections_file, directed=False):
        self._graph = {}
        self._directed = directed
        self._vertices_count = 0
        self._vertices = connections_file['initial node'].unique()
        self.create_graph(connections_file)

        
    def create_graph(self,connections_file):
            
        u = connections_file['initial node']
        v = connections_file['terminal node']
        d = connections_file['free flow time']
        
        for ind in range(len(connections_file.index)):
            self._graph[u[ind]] = []
            self._graph[v[ind]] = []
            
        for ind in range(len(connections_file.index)):
            self._graph[u[ind]].append([v[ind],d[ind]])
            if(self._directed==False):
                self._graph[v[ind]].append([u[ind],d[ind]])
        
            
    def get_graph(self):
        return self._graph



def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    graph_object = None
    try:
        f = open('/Users/kalashkala/Desktop/Python Code/ChicagoSketch_net.tntp','r')
        file_data = f.readlines()
        for i in range(9,len(file_data)):
            file_data[i] = file_data[i].split('\t')
            for j in range(1,len(file_data[i])-1):
                file_data[i][j] = float(file_data[i][j])
            file_data[i] = file_data[i][1:len(file_data[i])-1]

        file_data = file_data[9:]
        col = ['initial node','terminal node','capacity','length','free flow time','b','power','speed','toll','link type']
        file_data_df = pd.DataFrame(file_data,columns=col)

        file_data_df[['initial node','terminal node']] = file_data_df[['initial node','terminal node']].astype('int64')
                
        graph_object = Graph(file_data_df,True).get_graph()
                
        return graph_object
    except:
        return graph_object


def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1
    try:
        
        distance = [float('inf')] * (len(graph_object.keys())+1)
        distance[source] = 0
        visited = set()
        min_heap = []
        
        heappush(min_heap,(distance[source],source))
            
        while(len(min_heap)>0):
            node_dist, node = heappop(min_heap)
            visited.add(node)
                
            for connection, dist in graph_object[node]:
                if connection not in visited:
                    d = node_dist + dist
                    if d<distance[connection]:
                        distance[connection] = d
                        heappush(min_heap,(distance[connection],connection))
            
        if(distance[destination]==float('inf')):
            return -1

        shortest_path_distance = distance[destination]
        
        return shortest_path_distance
    except:
        return shortest_path_distance
