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
        this function prints the values of all the nodes in the linked list. 
        a temproary variable 'temp' is set to the head of the linked list. 
        a while loop checks it the temporary variable is set to None (reached end of the list?) 
        iterates through the list and prints the values of each node and then moves the temporary variable to the next node in the list. 
    '''
    def print_list(self): 
        temp = self.head  
        while temp != None:  
            print(temp.value)  
            temp = temp.next 

if __name__ == "__main__": 
    my_linked_list = LinkedList("Hello World") 
    my_linked_list.print_list() 
