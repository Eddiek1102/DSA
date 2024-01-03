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
        while temp != None: 
            print(temp.value, end = " ") 
            temp = temp.next 
        print() 
        
if __name__ == "__main__": 
    test = DoublyLinkedList(1) 
    test.print_list()
