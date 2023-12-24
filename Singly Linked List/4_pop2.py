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
    
    def append(self, value): 
        new_node = Node(value) 
        if self.length == 0: 
            self.head = new_node 
            self.tail = new_node 
        else: 
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1 
        return True 

    def pop(self): 
        if self.length == 0: #if the list is already empty 
            return None 
        elif self.length == 1: #if the list only has one node 
            temp = self.head 
            self.head = None 
            self.tail = None 
            self.length -= 1 
            return temp 
        else: #if the list has 2 or more nodes 
            temp = self.head 
            pre_temp = self.head 
            while temp.next != None: 
                pre = temp 
                temp = temp.next 
            self.tail = pre 
            self.tail.next = None 
            self.length -= 1 
            return temp 

if __name__ == "__main__": 
    my_list = LinkedList("Hello World") 
    my_list.append("Hello People") 
    my_list.append("I hate Georgia Tech") 
    
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
    
    print(my_list.length) 
    my_list.append("Does this work?") 
    my_list.print_list() 
