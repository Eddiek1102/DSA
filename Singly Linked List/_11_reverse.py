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
        while temp != None: 
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
            pre_temp = self.head 
            while temp.next != None: 
                pre_temp = temp 
                temp = temp.next 
            self.tail = pre_temp 
            self.tail.next = None 
            self.length -= 1 
            return temp 
    
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
    
    def pop_first(self): 
        if self.length == 0: 
            return None 
        elif self.length == 1: 
            temp = self.head 
            self.head = None 
            self.tail = None 
            self.length -= 1 
            return temp 
        else: 
            temp = self.head 
            self.head = self.head.next 
            temp.next = None 
            self.length -= 1
            return temp 
        
    def get_value(self, index): 
        if index < 0 or index > self.length - 1: 
            return None 
        else: 
            temp = self.head 
            for _ in range(0, index): 
                temp = temp.next 
            return temp 
    
    def set_value(self, index, value): 
        if index < 0 or index > self.length - 1: 
            return False 
        else: 
            temp = self.head 
            for _ in range(0, index): 
                temp = temp.next
            temp.value = value 
            return True 
        
    def insert(self, index, value): 
        if index < 0 or index > self.length: 
            return False 
        elif index == 0: 
            self.prepend(value) 
            return True 
        elif index == self.length: 
            self.append(value) 
            return True 
        else: 
            new_node = Node(value) 
            temp = self.head 
            for _ in range(0, index - 1): 
                temp = temp.next 
            new_node.next = temp.next 
            temp.next = new_node 
            self.length += 1 
            return True 
    
    def remove(self, index): 
        if index < 0 or index > self.length - 1: 
            return None 
        elif index == 0: 
            removed = self.pop_first()  
            return removed 
        elif index == self.length - 1: 
            removed = self.pop()  
            return removed 
        else: 
            prev = self.head  
            for _ in range(0, index - 1): 
                prev = prev.next          
            temp = prev.next 
            prev.next = temp.next 
            temp.next = None
            self.length -= 1  
            return temp  
    
    '''
        - Reversing a linked list
            1. switch the head and tail pointers 
            2. create a right & left pointer. right points to the node after temp, left points to the node before temp 
            3. iterate through the length of the linked list 
                3a. for each iteration, set the right pointer to the node right of temp variable 
                3b. temp's next pointer switches to point to the left 
                3c. left  pointer points to temp
                3d. temp points to right pointer. 
    '''
    def reverse(self): 
        temp = self.head 
        self.head = self.tail 
        self.tail = temp 
        right = temp.next 
        left = None 
        for _ in range(0, self.length): 
            right = temp.next 
            temp.next = left 
            left = temp 
            temp = right 
        return True 
    
if __name__ == "__main__": 
    test = LinkedList(0)  
    
    test.append(1)
    test.append(2) 
    test.append(3) 
    test.print_list() 
    print("-") 
    
    test.reverse() 
    test.print_list() 
    
    
    
    
    
