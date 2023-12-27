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
            print(temp.value, end = " ") 
            temp = temp.next 
        print() 
    
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
    
    def get(self, index): 
        if index < 0 or index > self.length - 1: 
            return None 
        else: 
            temp = self.head 
            for _ in range(0, index): 
                temp = temp.next 
            return temp 
    
    '''
        - setting a different value for a node at a certain index in a linked list 
            1. set temp using the get function and  pass in index 
            2. if temp returns None, we know that the index is out of range, return False
            3. if temp returns a node, change the value of that node, return True 
    '''
    def set_value(self, index, value): 
        temp = self.get(index) 
        if temp != None: 
            temp.value = value 
            return True 
        return False 
    
if __name__ == "__main__": 
    test = LinkedList(0) 
    test.append(1) 
    test.append(2) 
    test.append(3) 
    
    test.print_list() 
    
    test.set_value(2, 999) 
    
    test.print_list() 
    
    
