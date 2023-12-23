class Node: 
    #Used every time a node has to be created
    def __init__(self, value): 
        self.value = value #value
        self.next = None #pointer

class LinkedList: 
    def __init__(self, value):
        new_node = Node(value) #create first node
        self.head = new_node #initialize head pointer 
        self.tail = new_node #initialize tail pointer 
        self.length = 1 #keep track of of the length of the linked list 
    
    def append(self, value):
        #create a node, add node to end  
        pass 
    def prepend(self, value): 
        #create a node, add node to beginning 
        pass
    def insert(self, index, value): 
        #create a node, insert node at specific index 
        pass 

if __name__ == "__main__": 
    my_linked_list = LinkedList(4) #create linked list with first node value = 4 
    print(my_linked_list.head.value) #prints value of head node
    
    
    
