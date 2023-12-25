class Node: 
    '''
        this class exists to create new nodes. 
        initilizes the value of the new node to the value being passed in to the constructor. 
        node's next pointer -> None.
    '''
    def __init__(self, value): 
        self.value = value  
        self.next = None  

class LinkedList: 
    '''
        create a new node using the Node class. 
        head and tail points to the new node since it's the first and only node in the linked list. 
        length of linked list is 1 since there is only one node in the linked list
    '''
    def __init__(self, value):
        new_node = Node(value)  
        self.head = new_node  
        self.tail = new_node  
        self.length = 1 
    
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
    
    
    
