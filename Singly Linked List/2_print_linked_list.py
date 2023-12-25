class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None 
    
class LinkedList: 
    def __init__(self, value): 
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1 

    '''
        - Printint values of nodes in linked list
            1. set a temporary variable to the first node in the linked list (head). 
            2. iterate through the nodes
                2a. print the values of each node 
                2b. set the temporary variable to the next node in the linked list. 
    '''
    def print_list(self): 
        temp = self.head  
        while temp != None:  
            print(temp.value)  
            temp = temp.next 

if __name__ == "__main__": 
    my_linked_list = LinkedList("Hello World") 
    my_linked_list.print_list() 
