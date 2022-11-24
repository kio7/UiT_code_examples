from heapdict import heapdict

def dijkstra(graph, start):
    """ Find shortest path to all nodes using Dijkstra's algorithm
    
    # Input parameters:
    graph:    Dictionary of dictionaries:
              Key (1. level): Name of vertex.
              Value (1. level): Dictionary with weighted edges from vertex
              Key (2. level): Name of neighbor
              Value (2. level): Weight of edge to neighbor
              
              Example: {'A':{'B':5,'C':7}}
              (edge A->B with weight 5, edge A->C with weight 7)
              
    start:    Name of start vertex
        
    # Returns:
    dist:       Shortest distances to all nodes
    came_from:  Dict with "previous" node along shortest path to each node
    
    """
    
    # Initialize data strucures
    q = heapdict()        # Priority queue
    came_from = {}        # Dict, key = node, value = previous node
    dist = {}             # Dict, key = node, value = shortest dist. to node
    visited = {}          # Dict, key = node, value = True if node visited
    for node in graph.keys():
        dist[node] = float('inf')
        visited[node] = False
        
    # Add start vertex to queue and set its distance to zero
    q[start] = 0
    dist[start] = 0
    
    # Traverse graph until queue is empty  
    while len(q) > 0:    
        (current,_) = q.popitem()         # Pop node with shortest distance 
        visited[current] = True           # Mark node as visited

        # Check all neighbors of current vertex, relax edges if needed
        for neighbor in graph[current].keys():
            if not visited[neighbor]:
                dist_via_curr = dist[current] + graph[current][neighbor]
                if dist[neighbor] > dist_via_curr:     # If path via current node is shorter
                    q[neighbor] = dist_via_curr        # Insert into / update priority queue
                    dist[neighbor] = dist_via_curr     # Update shortest distance
                    came_from[neighbor] = current      # Update path to neighbor  
                    
    return dist, came_from


