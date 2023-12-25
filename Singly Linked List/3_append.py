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
        - Appending node to linked list 
            1. create new node
            2. check if the linked list is empty 
                2a. set the head and tails to the new node
            3. for other conditions, set the next pointer of the last (tail) variable to the new node. 
            4. set the tail to the new node 
            5. increment the length and return True 
     '''
    def append(self, value): 
        new_node = Node(value) 
        if self.head == None: 
            self.head = new_node 
            self.tail = new_node 
        else: 
            self.tail.next = new_node  
            self.tail = new_node  
        self.length += 1  
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
    
        
