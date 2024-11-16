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
        R = 6371.0

        # Convert latitude and longitude from degrees to radians
        lat1 = math.radians(self.x)
        lon1 = math.radians(self.y)
        lat2 = math.radians(other.x)
        lon2 = math.radians(other.y)

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Distance in kilometers
        distance = R * c * 1000
        return distance

# Graph structure
class Graph:
    def __init__(self):
        self.nodes = {}
        self.services_dict = {}
    
    def add_node(self, id, x, y, services=[]):
        node = Node(id, x, y, services)
        self.nodes[id] = node
        
        for service in services:
            if service not in self.services_dict:
                self.services_dict[service] = []
            self.services_dict[service].append(id)
        return node
    
    def add_edge_with_dis(self, node1_id, node2_id, distance):
        # Add the edge in both directions (bi-directional)
        self.nodes[node1_id].out_nodes.append((self.nodes[node2_id], distance))
        self.nodes[node2_id].out_nodes.append((self.nodes[node1_id], distance))

    def add_edge(self, node1_id, node2_id):
        # Calculate the Haversine distance between the two nodes
        node1 = self.get_node(node1_id)
        node2 = self.get_node(node2_id)
        distance = node1.euclidean_distance(node2)

        # Add the edge in both directions (bi-directional) with the Haversine distance
        self.add_edge_with_dis(node1_id, node2_id, distance)

    def get_node(self, node_id):
        if node_id not in self.nodes:
            raise ValueError(f"Node with id {node_id} not found")
        return self.nodes[node_id]
    def find_nodes_by_service(self, service):
        # Quickly return nodes providing the requested service
        return self.services_dict.get(service, [])

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
    def __init__(self, graph, start_id, end_id):
        self.graph = graph
        self.start = graph.get_node(start_id)
        self.end = graph.get_node(end_id)
        self.v_petr = set()   # Set of petrified nodes
        self.v_wilt = set()   # Set of wilted nodes
        self.l_opt = float('inf')  # Keep track of the optimal solution
        self.t = []
        
        # Debug: Check if start and end nodes are properly initialized
        print(f"Start Node: {self.start.id}, End Node: {self.end.id}")

    def run(self, start_id=None, end_id=None):
        # Update start and end if provided
        if start_id:
            self.start = self.graph.get_node(start_id)
            print(f"Updated Start Node: {self.start.id}")
        if end_id:
            self.end = self.graph.get_node(end_id)
            print(f"Updated End Node: {self.end.id}")
        
        self.start.fw = 0
        self.start.est = self.start.euclidean_distance(self.end)
        vcand = {self.start}

        while vcand:
            # Select the candidate node with the minimum forward cost
            vc = min(vcand, key=lambda v: v.fw)
            vcand.remove(vc)
            self.v_petr.add(vc)
            
            for vn, distance in vc.out_nodes:
                if prune_filter(vc, vn, distance):
                    continue
                
                vn.fw = vc.fw + distance
                vn.prev = vc
                self.v_wilt.discard(vn)
                
                if not prune_potential(vc, vn, self.l_opt, distance) and not prune_petrifaction(vn, self.v_petr):
                    vcand.add(vn)
                
                if vn == self.end:
                    self.t = self.trace_route(vn)
                    self.l_opt = min(self.l_opt, vc.fw + distance)  # Set l_opt to the best route found
                    print("Route found!", self.t)
                    return self.t
            
            self.v_wilt.add(vc)
            if vc.next:
                vc.fw = wilting(vc, vc.next, self.l_opt, distance)
            reverse_update(vc)
        
        print("No valid route found")
        return self.t if self.t else [], 0.0

    def trace_route(self, end_node):
        route = []
        total_distance = 0.0
        current_node = end_node

        while current_node.prev:
            route.append(current_node.id)
            for neighbor, distance in current_node.prev.out_nodes:
                if neighbor == current_node:
                    total_distance += distance
            current_node = current_node.prev
        
        route.append(self.start.id)
        route.reverse()
        
        return route, total_distance


graph = Graph()
# Adding nodes to the graph
graph.add_node(1, 13.0107776, 74.7917341, ["ITD"])
graph.add_node(2, 13.011471, 74.7922009, ["ECED"])
graph.add_node(3, 13.0107528, 74.7920782, ["LHCC"])
graph.add_node(4, 13.010026, 74.7922319, ["parking lot"])
graph.add_node(5, 13.009465969653366, 74.79259760997458,["small gate entrance"])
graph.add_node(6, 13.0113432, 74.7920815, ["ISH", "canteen"])
graph.add_node(7, 13.0120582, 74.7923465, ["CSED"])
graph.add_node(8, 13.0129008, 74.7925532, ["Guest House"])
graph.add_node(9, 13.0129325, 74.7907513, ["Beach gate"])
graph.add_node(10, 13.0131107, 74.7907264, ["CPWD office"])
graph.add_node(11, 13.0145691, 74.7939598, ["school"])
graph.add_node(12, 13.0148886, 74.7945828, ["park"])
graph.add_node(13, 13.0117295, 74.7939968, ["CivilDept"])
graph.add_node(14, 13.0118349, 74.7939458, ["Environment Engineering Lab"])
graph.add_node(15, 13.011729, 74.793978, ["Mining dept"])
graph.add_node(16, 13.0119497, 74.7940661, ["structural labratory"])
graph.add_node(17, 13.0120075, 74.7938492, ["Water resources dept"])
graph.add_node(18, 13.01083705594445, 74.79426821611641, ["main dept entrance"])
graph.add_node(19, 13.0106995, 74.79408, ["Main building"])
graph.add_node(20, 13.0102545, 74.7940875, ["library"])
graph.add_node(21, 13.009730313898858, 74.79397730744158, ["LHCA"])
graph.add_node(22, 13.009448, 74.7943881, ["Dept of math"])
graph.add_node(23, 13.0094902, 74.7943771, ["CRF","research"])
graph.add_node(24, 13.0098862, 74.7949371, ["Digital library","library"])
graph.add_node(25, 13.0105237, 74.7948251, ["Dept of metullargy"])
graph.add_node(26, 13.0105237, 74.7948251, ["old chemical"])
graph.add_node(27, 13.0108744, 74.7948716, ["Pavilion"])
graph.add_node(28, 13.0120437, 74.7950259, ["cafe"])
graph.add_node(29, 13.0120605, 74.7955351, ["Dept of mech"])
graph.add_node(30, 13.0123832, 74.7960155, ["cooperative society"])
graph.add_node(31, 13.0127717, 74.7963389, ["Laundry"])
graph.add_node(32, 13.0118813, 74.7960862, ["Tennis court"])
graph.add_node(33, 13.0110986, 74.7963568, ["Swimming pool"])
graph.add_node(34, 13.0110986, 74.7963568, ["Basket ball court"])
graph.add_node(35, 13.0110986, 74.7963568, ["Vollyball court"])
graph.add_node(36, 13.0106786, 74.7970429, ["Main ground"])
graph.add_node(37, 13.0102621, 74.796795, ["New sports complex"])
graph.add_node(38, 13.0093685, 74.7971621, ["New pg block"])
graph.add_node(39, 13.0093685, 74.7971621, ["pushpagiri block"])
graph.add_node(40, 13.0084656, 74.7972016, ["NITK Naga temple"])
graph.add_node(41, 13.008802630263537, 74.79574736143074, ["SJA"])
graph.add_node(42, 13.0085909, 74.7955107, ["Food court","food"])
graph.add_node(43, 13.0087431, 74.7947499, ["CDC"])
graph.add_node(44, 13.008991, 74.7938159, ["SBI Bank"])
graph.add_node(45, 13.0088676, 74.7931261, ["post office"])
graph.add_node(46, 13.0089088, 74.793703, ["saloon"])
graph.add_node(47, 13.0088161, 74.7937339, ["Bank"])
graph.add_node(48, 13.0087468, 74.7937848, ["Xerox"])
graph.add_node(49, 13.0082447, 74.7938913, ["Shiwalik"])
graph.add_node(50, 13.007173170247455, 74.79473622645236, ["Gym"])
graph.add_node(51, 13.007328481475865, 74.79382635907791, ["Trishul night canteen"])
graph.add_node(52, 13.00677657214907, 74.79455382041358, ["Nandini"])
graph.add_node(53, 13.0068866, 74.7949673, ["Mega block 2"])
graph.add_node(54, 13.0061193, 74.7948629, ["NIlagiri hostel"])
graph.add_node(55, 13.006136039852649, 74.79562091065486, ["satpura"])
graph.add_node(56, 13.0066526861426, 74.79644212793897, ["Vindhya"])
graph.add_node(57, 13.0068869, 74.796698, ["Aravali"])
graph.add_node(58, 13.0078941, 74.7969239, ["Karavali"])
graph.add_node(59, 13.0080377, 74.7968358, ["Sahyadri"])
graph.add_node(60, 13.0108134, 74.7934104, ["Busstop"])
graph.add_node(61, 13.012484, 74.792784, ["nitk west gate"])
graph.add_node(62, 13.012501486377898, 74.79322916359563, ["nitk east gate"])
graph.add_node(63,13.0090699,74.7967176,["amul"])
# Adding edges between nodes
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(3,4)
graph.add_edge(4,5)
graph.add_edge(4,45)
graph.add_edge(2,6)
graph.add_edge(2,7)
graph.add_edge(6,61)
graph.add_edge(61,8)
graph.add_edge(8,10)
graph.add_edge(8,9)
graph.add_edge(7,8)
graph.add_edge(61,62)
graph.add_edge(8,11)
graph.add_edge(11,62)
graph.add_edge(60,62)
graph.add_edge(11,12)
graph.add_edge(62,13)
graph.add_edge(13,15)
graph.add_edge(13,16)
graph.add_edge(16,17)
graph.add_edge(15,19)
graph.add_edge(19,20)
graph.add_edge(20,21)
graph.add_edge(21,22)
graph.add_edge(22,23)
graph.add_edge(23,24)
graph.add_edge(19,27)
graph.add_edge(24,25)
graph.add_edge(13,29)
graph.add_edge(29,30)
graph.add_edge(30,31)
graph.add_edge(29,32)
graph.add_edge(29,33)
graph.add_edge(29,34)
graph.add_edge(34,35)
graph.add_edge(35,36)
graph.add_edge(36,63)
graph.add_edge(63,38)
graph.add_edge(39,38)
graph.add_edge(39,37)
graph.add_edge(36,37)
graph.add_edge(39,40)
graph.add_edge(63,41)
graph.add_edge(41,42)
graph.add_edge(42,43)
graph.add_edge(43,44)
graph.add_edge(44,45)
graph.add_edge(44,46)
graph.add_edge(46,48)
graph.add_edge(48,49)
graph.add_edge(49,51)
graph.add_edge(47,48)
graph.add_edge(44,46)
graph.add_edge(51,52) 
graph.add_edge(52,53)
graph.add_edge(53,55)
graph.add_edge(54,55)
graph.add_edge(55,56)
graph.add_edge(56,57)
graph.add_edge(57,58)
graph.add_edge(58,59)
graph.add_edge(59,38)
graph.add_edge(24,42)
graph.add_edge(20,23)
graph.add_edge(23,42)

start_id=int(input("Enter the start node:"))
end_id=int(input("Enter the end id:"))
requests=input("Enter the services:").split()


ows= OWS(graph, start_id, end_id)
route,total_distance=ows.run(start_id,end_id)
print(total_distance)

print("Optimal Route:", route)
for e in route:
	print(graph.nodes[e].services[0],"->",end="")
print("")
print("Distance - " + str(total_distance) + " meters")
