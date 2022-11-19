# Class Node

class Node:
    def __init__(self, literal):
        
        # attributes
        self.literal = literal
        self.next = []
        self.previous = []
    
    def add_next(self, next_node):
        """
        Adds a node to the next nodes list.
        """
        self.next.append(next_node)
    
    def add_previous(self, previous_node):
        """
        Adds a node to the previous nodes list.
        """
        self.previous.append(previous_node)