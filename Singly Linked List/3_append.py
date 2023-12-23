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
    
    #appending a node to linked list 
    def append(self, value): 
        new_node = Node(value) 
        if self.head == None: # if list is empty 
            self.head = new_node 
            self.tail = new_node 
        else: 
            self.tail.next = new_node # tail pointer should now point to new node
            self.tail = new_node # the new node becomes the new tail node 
        self.length += 1 #increment the length of list 
        return True 
    
    def print_list(self): 
        temp = self.head 
        while temp != None: 
            print(temp.value) 
            temp = temp.next 

if __name__ == "__main__": 
    my_linked_list = LinkedList(1)
    my_linked_list.append(2) 
    my_linked_list.append(3) 
    my_linked_list.append(4) 
    my_linked_list.append(5) 
    
    my_linked_list.print_list() 
    
        
