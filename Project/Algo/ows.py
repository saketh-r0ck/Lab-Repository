import random
import math

# Node class representing a POI
class Node:
    def __init__(self, id, x, y, services=[]):
        self.id = id
        self.x = x
        self.y = y
        self.services = services
        self.fw = float('inf')   # Forward cost from start
        self.bw = float('inf')   # Backward cost to destination
        self.est = float('inf')  # Estimated distance to destination
        self.prev = None         # Previous node in the optimal path
        self.next = None         # Next node in the optimal path
        self.out_nodes = []      # List of neighboring nodes (edges)
        
    def euclidean_distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Graph structure
class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, id, x, y, services=[]):
        node = Node(id, x, y, services)
        self.nodes[id] = node
        return node
    
    def add_edge(self, node1_id, node2_id, distance):
        # Add the edge in both directions (bi-directional)
        self.nodes[node1_id].out_nodes.append((self.nodes[node2_id], distance))
        self.nodes[node2_id].out_nodes.append((self.nodes[node1_id], distance))
    
    def get_node(self, node_id):
        if node_id not in self.nodes:
            raise ValueError(f"Node with id {node_id} not found")
        return self.nodes[node_id]

# Pruning mechanisms with debug statements
def prune_filter(vc, vn, distance):
    # Adjusted to avoid overly aggressive filtering
    return vc.fw + distance >= vn.fw

def prune_potential(vc, vn, l_opt, distance):
    # Skip pruning if l_opt is still infinite
    return l_opt != float('inf') and (vc.fw + distance + vn.est >= l_opt)

def prune_petrifaction(vn, vpetr):
    return vn in vpetr

def wilting(vc, vn, l_opt, distance):
    return min(vn.fw, l_opt - vn.est) - distance

# Reverse update function to adjust backward costs and estimation
def reverse_update(vc):
    while vc.prev:
        vp = vc.prev
        for neighbor, distance in vp.out_nodes:
            if neighbor == vc and vc.bw + distance < vp.bw:
                vp.bw = vc.bw + distance
                vp.next = vc
                vp.est = min(vn.est + dist for vn, dist in vp.out_nodes)
        vc = vp

# OWS Algorithm
class OWS:
    def __init__(self, graph, start_id, end_id, requests):
        self.graph = graph
        self.start = graph.get_node(start_id)
        self.end = graph.get_node(end_id)
        self.requests = set(requests)
        self.v_petr = set()   # Set of petrified nodes
        self.v_wilt = set()   # Set of wilted nodes
        self.l_opt = float('inf')  # Keep track of the optimal solution
        self.t = []
        
        # Debug: Check if start and end nodes are properly initialized
        print(f"Start Node: {self.start.id}, End Node: {self.end.id}")

    def run(self):
        self.start.fw = 0
        self.start.est = self.start.euclidean_distance(self.end)
        vcand = {self.start}

        while vcand:
            # Select the candidate node with the minimum forward cost
            vc = min(vcand, key=lambda v: v.fw)
            vcand.remove(vc)
            self.v_petr.add(vc)
            
            # Debug: Print current node and forward cost
            print(f"Processing node {vc.id}, forward cost: {vc.fw}")
            
            for vn, distance in vc.out_nodes:
                # Prune and check with detailed debug logs
                print(f"Pruning filter for {vc.id} -> {vn.id} with distance {distance}")
                if prune_filter(vc, vn, distance):
                    print(f"Pruning node {vn.id}")
                    continue
                
                vn.fw = vc.fw + distance
                vn.prev = vc
                self.v_wilt.discard(vn)
                
                # Apply pruning checks with additional logging
                if not prune_potential(vc, vn, self.l_opt, distance) and not prune_petrifaction(vn, self.v_petr):
                    vcand.add(vn)
                    
                    # Debug: Show when node is added to candidate list
                    print(f"Adding node {vn.id} to candidate list")
                
                # Check if we reached the end node and update route
                if vn == self.end:
                    self.t = self.trace_route(vn)
                    self.l_opt = min(self.l_opt, vc.fw + distance)  # Set l_opt to the best route found
                    print("Route found!")
                    return self.t
            
            # Debug: Show current candidate nodes after expansion
            print(f"Candidate nodes: {[node.id for node in vcand]}")

            self.v_wilt.add(vc)
            if vc.next:
                vc.fw = wilting(vc, vc.next, self.l_opt, distance)
            reverse_update(vc)
        
        # If no valid route is found
        print("No valid route found")
        return self.t if self.t else []

    def trace_route(self, end_node):
        # Trace the path from end_node to start_node
        route = []
        current_node = end_node
        while current_node:
            route.append(current_node.id)
            current_node = current_node.prev
        route.reverse()  # Reverse to get the path from start to end
        return route



# Now run the OWS algorithm for a specific start and end node
ows = OWS(graph, start_id=1, end_id=3, requests=['A', 'B'])
route = ows.run()

print("Optimal Route:", route)
