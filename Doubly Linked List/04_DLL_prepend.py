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
    
    '''
        Adding a node to the beginning of a doubly linked list 
        - if the list is empty, head & tail -> new node 
        - for all other cases, next pointer of new node points to head node, prev pointer of head node points to new node, head is moved to the new node, increment the length, return True  
    '''
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

if __name__ == "__main__": 
    test = DoublyLinkedList(1)
    test.append(2) 
    test.append(3) 
    test.append(4) 
    test.append(5) 
    
    test.print_list() 
    
    test.prepend(0) 
    test.print_list() 
    print(test.length) 
    
    
    
    
