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
    
    #pop item off of linked list 
    def pop(self): 
        if self.head == None: #check if linked list is empty 
            return None 
        temp = self.head #set temp to head of linked list 
        pre = self.head #set pre to head of linked list (this will iterate one node behind temp)
        while temp.next != None: 
            pre = temp 
            temp = temp.next 
        self.tail = pre 
        self.tail.next = None 
        self.length -= 1 
        if self.length == 0: #this is what happens when the linked list originally has one node  
            self.head = None 
            self.tail = None 
        return temp 
        
    def print_list(self): 
        temp = self.head 
        while temp != None: 
            print(temp.value, end = " ")
            temp = temp.next 

if __name__ == "__main__": 
    my_list = LinkedList(1) 
    my_list.append(2) 
    my_list.append(3) 
    
    my_list.print_list() 
    print() 
    
    my_list.pop() 
    my_list.print_list()
    print() 
    
    my_list.pop() 
    my_list.print_list() 
    print() 
    
    my_list.pop()
    my_list.print_list() 
    print() 
    
    my_list.pop() 
    my_list.print_list() 
