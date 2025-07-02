class Graphs:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()    
    
    def __repr__(self):
        str_graph = ""
        
        for key, value in self.adj_list.items():
            str_graph += f"{key} -> {value}\n"
            
        return str_graph
    
    def dfs(self):
        pass
    
    def bfs(self):
        pass
    
    def add_node(self):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node already exists in the graph.")
        
    def add_edge(self, source_node, destination_node, weighted=None):
        if source_node not in self.adj_list:
            self.add_node(source_node)
            
        if destination_node not in self.adj_list:
            self.add_node(destination_node)
            
        if weighted is not None:
            self.adj_list[source_node].add((destination_node, weighted))
            if self.directed:
                self.adj_list[destination_node].add((source_node, weighted))
        else:
            self.adj_list[source_node].add(destination_node)
            if self.directed:
                self.adj_list[destination_node].add(source_node)
        
        def obtain_neighbors(self, node):
        
        def adj_matrix(self):
            pass
    
    if __name__ == "__main__":
        graph.obj = Graphs()
        print("Graph object created:", graph.obj)