class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None 

class LinkedList: 
    def __init__(self, value): 
        new_node = Node(value) 
        self.next = None 
        self.head = new_node 
        self.tail = new_node 
        self.length = 1
    
    def print_list(self): 
        temp = self.head 
        while (temp != None): 
            print(temp.value) 
            temp = temp.next 
    
    '''
    - prepending node the beginning of a linked list
    create the new node. 
    if the linked list is empty, set the head and tail to point to the new node.
    if the linked list is not empty, new node -> head, head -> new node 
    increment the length of the linked list
    return True 
    '''
    def prepend(self, value): 
        new_node = Node(value) 
        if (self.length == 0): 
            self.head = new_node 
            self.tail = new_node 
        else: 
            new_node.next = self.head 
            self.head = new_node 
        self.length += 1 
        return True 

if __name__ == "__main__": 
    test = LinkedList("world") 
    test.prepend("hello")
    test.print_list()  
    
