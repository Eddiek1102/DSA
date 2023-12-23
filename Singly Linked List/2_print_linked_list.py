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

    #print contents of linked list 
    def print_list(self): 
        temp = self.head #start at head node
        while temp != None: #check if node's next pointer is pointing to None
            print(temp.value) #print value of current node 
            temp = temp.next #iterate to next node 

if __name__ == "__main__": 
    my_linked_list = LinkedList("Hello World") 
    my_linked_list.print_list() #prints "Hello World" 
