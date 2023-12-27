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
    
    '''
        - Retrieving a node at a certain index in a linked list 
            1. Check to see if index being passed in is out of range. 
                1a. If index is out of range, return None 
            2. If index is in range, set a temp variable to head node 
                2a. iterate through from 0 to index
                2b. increment node each interation 
                2c. return the node 
    '''
    def get(self, index): 
        if index < 0 or index > self.length - 1: 
            return None 
        else: 
            temp = self.head 
            for _ in range(0, index): 
                temp = temp.next 
            return temp 
    
if __name__ == "__main__": 
    test = LinkedList(0) 
    test.append(1) 
    test.append(2) 
    test.append(3) 
    
    zero_index = test.get(0) 
    second_index = test.get(2) 
    out_of_range = test.get(7) 
    
    print(zero_index.value, end= " ") 
    print(second_index.value) 
    print(out_of_range) 
