# Class Dpenendency

class Dependency:
    def __init__(self, node):
        
        # attributes
        self.nodes = [node]

    def add_independent_nodes(self, node):
        """
        Adds independent node to dependency graph
        """
        self.nodes.append(node)
    def independent_nodes(self):
        return self.nodes
