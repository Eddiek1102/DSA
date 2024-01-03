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
    
    '''
        Popping a node off doubly linked list
        - if the length is zero, there's nothing to pop. return None 
        - if the length is exactly 1, store the one node in a temp variable. disconnect head and tail pointers. decrement length and return the temp variable. 
        - for all other lengths, store the tail node in a temp variable. 
    '''
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

if __name__ == "__main__": 
    test = DoublyLinkedList(1)
    test.append(2) 
    test.append(3) 
    test.append(4) 
    test.append(5) 
    
    test.print_list() 
    
    popped = test.pop() 
    test.print_list() 
    popped = test.pop() 
    test.print_list()
    popped = test.pop() 
    test.print_list()
    popped = test.pop() 
    test.print_list()
    popped = test.pop() 
    test.print_list()
    popped = test.pop() 
    test.print_list()
    
    
    
    
