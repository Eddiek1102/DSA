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
    
    def prepend(self, value): 
        new_node = Node(value) 
        if self.length == 0: 
            self.head = new_node 
            self.tail = new_node 
        else: 
            new_node.next = self.head 
            self.head = new_node 
        self.length += 1 
        return True 
    
    def pop(self): 
        if self.length == 0: 
            return None 
        elif self.length == 1: 
            temp = self.head 
            self.head = None 
            self.tail = None 
            self.length = 0 
            return temp 
        else: 
            temp = self.head 
            pre_temp = temp 
            while (temp.next != None): 
                pre_temp = temp 
                temp = temp.next 
            self.tail = pre_temp 
            self.tail.next = None 
            self.length -= 1 
            return temp
    '''
        - Popping off the first node of a linked list 
            1. if the length of the linked list is 0, return None 
            2. if the length of the linked list is 1...
                2a. set a temp variable to the head node 
                2b. set head and tail pointers to None
                2c. decrement length, return the temp variable being popped off
            3. if the length of the linked is 2 or greater... 
                3a. set a temp variable to the head node
                3b. move the head pointer the point at the next node 
                3c. decrement the length of the linked list, return temp variable being popped 
    '''
    def pop_first(self): 
        if self.length == 0: 
            return None 
        elif self.length == 1: 
            temp = self.head 
            self.head = None 
            self.tail = None 
            self.length = 0 
            return temp 
        else: 
            temp = self.head 
            self.head = self.head.next 
            self.length -= 1 
            return temp 
    
if __name__ == "__main__": 
    test = LinkedList(1)
    test.append(2)
    test.append(3) 
    
    test.print_list()
    print("-")
    
    first_element = test.pop_first() 
    print(first_element.value) 
    print("-")
    
    last_element = test.pop() 
    print(last_element.value) 
    print('-')
    
    test.print_list() 
    print("-") 
    
    test.prepend(999)
    test.print_list() 
    print("-")
