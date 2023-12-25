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
    
    def append(self, value): 
        new_node = Node(value) 
        if self.head == None: 
            self.head = new_node 
            self.tail = new_node 
        else: 
            self.tail.next = new_node 
            self.tail = new_node 
        self.length += 1 
        return True 
    
    '''
        - Popping last node off of linked list 
            1. Check if linked list is empty
                1a. return None (if list is empty) 
            2. initialize 2 temporary variables to the head of the linked list. 
            3. iterate through the linked list using both variables (one traveling one set ahead of the other) 
            4. once the variable that's ahead points to None, you know you've reached the last node. 
            5. set the new tail to be the second temp variable. this variable should now point to None. 
            6. return the first variable (temp). 

        ! If the linked list only has one element to begin with 
            7. set the head and tail to None 

            8. decrement the length of the linked list
            9. return the first variable (the one that was popped off) 
    '''
    def pop(self): 
        if self.head == None: #check if linked list is empty 
            return None 
        temp = self.head #set temp to head of linked list 
        pre = self.head #set pre to head of linked list (this will iterate one node behind temp)
        while temp.next != None: 
            pre = temp 
            temp = temp.next 
        self.tail = pre 
        self.tail.next = None 
        self.length -= 1 
        if self.length == 0: #this is what happens when the linked list originally has one node  
            self.head = None 
            self.tail = None 
        return temp 
        
    def print_list(self): 
        temp = self.head 
        while temp != None: 
            print(temp.value, end = " ")
            temp = temp.next 

if __name__ == "__main__": 
    my_list = LinkedList(1) 
    my_list.append(2) 
    my_list.append(3) 
    
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
    print() 
    
    my_list.pop() 
    my_list.print_list() 
