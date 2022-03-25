class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def head(self):
        return self.__head
    
    @property
    def tail(self):
        return self.__tail

    @property
    def size(self):
        return self.__size

    @head.setter
    def head(self, value):
        self.__head = value
    
    @tail.setter
    def tail(self, value):
        self.__tail = value

    @size.setter
    def size(self, value):
        self.__size = value


    def get_first(self):
        if self.size == 0:
            return None
        else:
            return self.head.element
    

    def get_last(self):
        if self.size == 0:
            return None
        else:
            return self.tail.element


    def add_first(self, e):
        new_node = Node(e)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

        if self.tail == None:
            self.tail = self.head


    def add_last(self, e):
        new_node = Node(e)
    
        if self.tail == None:
            self.head = self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    
        self.size += 1
    
    def add(self, e): # Same as add_last
        self.add_last(e)


    def insert(self, index, e):
        if index == 0:
            self.add_first(e)

        elif index >= self.size:
            self.add_last(e)

        else:
            current = self.head

            for i in range(index - 1):
                current = current.next

            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.size += 1


    def remove_first(self):
        if self.size == 0:
            return None

        else:
            temp = self.head
            self.head = self.head.next 
            self.size -= 1 
            if self.head == None: 
                self.tail = None

            return temp.element 

    
    def remove_last(self):
        if self.size == 0:
            return None

        elif self.size == 1:
            temp = self.head
            self.head = self.tail = None 
            self.size = 0
            return temp.element

        else:
            current = self.head
        
            for i in range(self.size - 2):
                current = current.next
        
            temp = self.tail
            self.tail = current
            self.tail.next = None
            self.size -= 1

            return temp.element


    def remove_at(self, index):
        if index < 0 or index >= self.size:
            return None

        elif index == 0:
            return self.remove_first() # Remove first

        elif index == self.size - 1:
            return self.remove_last() # Remove last

        else:
            previous = self.head
    
            for i in range(index - 1):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.size -= 1
            return current.element
    

    def is_empty(self):
        return self.size == 0
    

    def get_size(self):
        return self.size


    def __str__(self):
        result = "["
        if self.size != 0:
            current = self.head
            for i in range(self.size):
                result += str(current.element)
                current = current.next
                if current != None:
                    result += ", " # Separate two elements with a comma

        result += "]" # Insert the closing ] in the string

        return result

        
    # From here is where the task begins.
    def clear(self):
        if self.size == 0:
            return None
        
        if self.size == 1:
            self.head.element = None
    
        current = self.head
        for _ in range(self.size):
            current.element = None
            previous = current
            current = current.next
            previous.next = None

        self.head = self.tail = None
        self.size = 0
    

    # Return true if this list contains the element 
    def contains(self, elem):
        if self.size == 0:
            return None

        elif self.size == 1:
            return True if self.head.element == elem else False

        current = self.head

        for _ in range(self.size - 1):
            if current.element == elem:
                return True

            current = current.next
        
        return False        


    # Remove the element and return true if the element is in the list 
    def remove(self, elem):
        if self.size == 0:
            return None
        
        elif self.size == 1:
            if elem == self.head.element:
                self.head = None
                self.size = 0
                return True
        
        previous = self.head

        if previous.element == elem:
            self.head = previous.next
            previous.next = None
            self.size -= 1
            return True
        
        for _ in range(self.size - 1):
            current = previous.next
            if current.element == elem:
                previous.next = current.next
                current.next = None
                self.size -= 1
                return True

            current = current.next


    # Return the element from this list at the specified index 
    def get(self, index):
        if index < 0 or index >= self.size:
            return None # Out of range

        current = self.head

        if index == 0:
            return current.element

        for _ in range(index):
            current = current.next

        return current.element


    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def index_of(self, elem):
        count = -1
        current = self.head

        for _ in range(self.size):
            if current.element == elem:
                count += 1
                break
            current = current.next
            count += 1

        return count


    # Return the index of the last matching element in this list
    # Return -1 if no match. 
    def last_index_of(self, elem):
        lis = []
        current = self.head
        for _ in range(self.size):
            lis.append(current.element)
            current = current.next
        
        if elem in lis:
            for count, i in enumerate(lis):
                if i == elem:
                    if count == self.size - 1:
                        return count
                    if i not in lis[count:]:
                        return count
        return -1
                
                
    # Replace the element at the specified position in this list with the specified element.
    def set(self, index, elem):
        if index < 0 or index >= self.size:
            return None
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        current.element = elem


    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.head)
    

# The Node class
class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

# Linked list iterator
class LinkedListIterator: 
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element

if __name__ == "__main__":
    lis = LinkedList()
    lis.add_first("Helge")
    lis.add("Konrad")
    lis.add("Marthe")
    lis.add("Anders")
    lis.add("Helge")


    print(lis.contains("Helge"))

    print(lis)
    print(lis.remove("Helge"))
    print(lis)

    print(lis.get(2))

    print(lis.index_of("Anders"))

    lis.add_first("Helge")
    print(lis)
    print(lis.last_index_of("Helge"))

    lis.set(0, "No") # Index as in list index, first element is 0 ect.
    print(lis)

    lis.clear()
    print(lis)
    