class Node: 
    def __init__(self, value): 
        self.value = value 
        self.next = None
        self.prev = None 
    
class DoublyLinkedList: 
    def __init__(self, value): 
        new_node = Node(value) 
        self.head = new_node 
        self.tail = new_node 
        self.length = 1 
    
    def print_list(self): 
        temp = self.head 
        while temp: 
            print(temp.value, end = " ")
            temp = temp.next 
        print() 
    
    def append(self, value): 
        new_node = Node(value) 
        if self.length == 0: 
            self.head = new_node 
            self.tail = new_node 
        else: 
            new_node.prev = self.tail
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1 
        return True 
    
    def pop(self): 
        if self.length == 0: 
            return None 
        elif self.length == 1: 
            temp = self.head 
            self.head = None 
            self.tail = None 
            self.length -= 1 
            return temp 
        else: 
            temp = self.tail 
            self.tail = self.tail.prev 
            self.tail.next = None 
            temp.prev = None 
            self.length -= 1 
            return temp 
    
    def prepend(self, value): 
        new_node = Node(value) 
        if self.length == 0: 
            self.head = new_node 
            self.tail = new_node 
        else: 
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
        self.length += 1 
        return True 
    
    def pop_first(self): 
        if self.length == 0: 
            return None 
        temp = self.head 
        if self.length == 1: 
            self.head = None 
            self.tail = None 
        else: 
            self.head = self.head.next 
            self.head.prev = None 
            temp.next = None 
        self.length -= 1 
        return temp  
    
    def get_value(self, index): 
        if index < 0 or index >= self.length: 
            return None 
        if index < self.length / 2: 
            temp = self.head 
            for _ in range(index): 
                temp = temp.next 
        else: 
            temp = self.tail 
            for _ in range(self.length - 1, index, -1): 
                temp = temp.prev 
        return temp 
    
    '''
        Change value of a node at a certain index 
    '''
    def set_value(self, index, value): 
        temp = self.get_value(index) 
        if temp: 
            temp.value = value 
            return True 
        return False 
                

if __name__ == "__main__": 
    test = DoublyLinkedList(1) 
    test.append(2) 
    test.append(3) 
    test.print_list()
    
    test.set_value(0, 9)
    test.print_list()    
