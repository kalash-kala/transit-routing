"""
Enter the solution for Q2 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""

from heapq import heappush, heappop, heapify

def bidirectional_dij(source: int, destination: int, graph_object) -> int:
    """
    Bi-directional Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    shortest_path_distance = -1

    try:
        mu = float('inf')
    
        distance_forward = [float('inf')]*(len(graph_object.keys())+1)
        distance_backward = [float('inf')]*(len(graph_object.keys())+1)
        
        distance_forward[source] = 0
        distance_backward[destination] = 0
        
        visited_forward = set()
        visited_backward = set()
        
        min_heap_forward = []
        min_heap_backward = []
        
        heappush(min_heap_forward,(distance_forward[source],source))
        heappush(min_heap_backward,(distance_backward[destination],destination))
        
        while(len(min_heap_forward)>0 and len(min_heap_backward)>0):
            
            node_dist_forward, node_forward = heappop(min_heap_forward)
            node_dist_backward, node_backward = heappop(min_heap_backward)
            
            visited_forward.add(node_forward)
            visited_backward.add(node_backward)
            
            # For Forward dijkstra
            for connection, dist in graph_object[node_forward]:
                if connection not in visited_forward:
                    d = dist + node_dist_forward
                    if d<distance_forward[connection]:
                        distance_forward[connection] = d
                        heappush(min_heap_forward,(distance_forward[connection],connection))
                if ((connection in visited_backward) and (distance_forward[node_forward] + dist + distance_backward[connection] < mu)):
                    mu = distance_forward[node_forward] + dist + distance_backward[connection]
            
            # For Backward dijkstra
            for connection, dist in graph_object[node_backward]:
                if connection not in visited_backward:
                    d = dist + node_dist_backward
                    if d<distance_backward[connection]:
                        distance_backward[connection] = d
                        heappush(min_heap_backward,(distance_backward[connection],connection))
                if ((connection in visited_forward) and (distance_backward[node_backward] + dist + distance_forward[connection] < mu)):
                    mu = distance_backward[node_backward] + dist + distance_forward[connection]
            
            # Terminating Condition
            if (distance_forward[node_forward] + distance_backward[node_backward] >= mu):
                return round(mu)
            
        return shortest_path_distance
            
    except:
        return shortest_path_distance
