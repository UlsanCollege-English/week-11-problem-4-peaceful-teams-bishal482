"""
HW04 — Peaceful Teams (Bipartite Check)

Implement:
- bipartition(graph)
"""

from collections import deque

def bipartition(graph: dict) -> tuple or None:
    """
    Return (left_set, right_set) if the graph is bipartite; else None.

    Uses BFS coloring over all components.
    """
    
    # Set of all unique nodes in the graph
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
        
    # Dictionary to store the color/partition of each node
    # color[node] = 0 (Left set) or 1 (Right set)
    color = {} 
    
    # Initialize the two partitions
    left_set = set()
    right_set = set()
    
    # Iterate through all nodes to handle disconnected components
    for start_node in all_nodes:
        if start_node not in color:
            # Start a new BFS for an uncolored component
            queue = deque([start_node])
            color[start_node] = 0  # Start with Color 0 (Left set)
            left_set.add(start_node)
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                
                # Determine the color for the neighbors
                next_color = 1 if current_color == 0 else 0
                
                # Iterate over neighbors of u (handle missing keys defensively)
                for v in graph.get(u, []):
                    
                    if v not in color:
                        # Neighbor v is uncolored: color it and add to queue
                        color[v] = next_color
                        if next_color == 0:
                            left_set.add(v)
                        else:
                            right_set.add(v)
                        queue.append(v)
                        
                    elif color[v] == current_color:
                        # Cycle detected: Neighbor v has the same color as u.
                        # This means an odd-length cycle exists (not bipartite).
                        return None
                        
    # If all components are successfully colored without conflicts, return the partitions
    return (left_set, right_set)