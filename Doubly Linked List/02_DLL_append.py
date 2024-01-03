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

    '''
        Appending new node to a doubly linked list 
        - Need to make sure that the prev pointer of the new node is pointing to the tail node. 
        - The next pointer of the tail node should point to the node being appended. 
        - If the list is empty, the node being appended is the first & last node of the list (head, tail -> new node). 
    '''
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

if __name__ == "__main__": 
    test = DoublyLinkedList(1)
    test.append(2) 
    test.append(3) 
    test.append(4) 
    test.append(5) 
    
    test.print_list()
    
    
