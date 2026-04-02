import networkx as nx

def build_eco_route(start_node, end_node, eco_priority=0.5):
    # graph
    G = nx.Graph()
    
    # Road segments: (source, destination, distance, carbon_index)
    G.add_edge('Home', 'Main_Road', distance=5, carbon=2.0)
    G.add_edge('Main_Road', 'Office', distance=10, carbon=2.5)
    G.add_edge('Home', 'Park_Path', distance=8, carbon=0.5) # Longer but green
    G.add_edge('Park_Path', 'Office', distance=12, carbon=0.5)

    # weighting logic 
    for u, v, data in G.edges(data=True):
        # weight = Distance balanced with Carbon Index 
        data['final_weight'] = data['distance'] * (1 + (data['carbon'] * eco_priority))

    # 3. dijkstra
    path = nx.dijkstra_path(G, start_node, end_node, weight='final_weight')
    return path

# testing 
if __name__ == "__main__":
    print("Fastest Route (Priority 0):", build_eco_route('Home', 'Office', 0))
    print("Eco Route (Priority 1):", build_eco_route('Home', 'Office', 1))