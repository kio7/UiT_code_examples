class Node:
    def __init__(self, element):
        self.element = element
        self.next = None
    

class Linked_list:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    def add_first(self, element):
        node = Node(element)
        if self.__head == None:
            self.__head = self.__tail = node
        else:
            next = self.__head
            self.__head = node
            node.next = next
        
        self.__length += 1


    def add_last(self, element):
        node = Node(element)
        if self.__head == None:
            self.__head = self.__tail = node
        else:
            old_tail = self.__tail
            self.__tail = node
            old_tail.next = node
        
        self.__length += 1


    def insert(self, element, index):
        if index >= self.__length or index < 0:
            raise RuntimeError("Out of bounds, current index or current lenght was" + self.__length + "tried to access with index" + index)
        if index == 0 or self.__length == 0:
            self.add_first(element)
        elif index == self.__length:
            self.add_last(element)
        else:
            node = Node(element)

        current = self.__head
        for i in range(index-1):
            current = current.next
        
        next = current.next
        current.next = node
        node.next = next

        self.__length += 1

    def remove_first(self):
        if self.__length == 0:
            return None
        
        to_remove = self.__head
        self.__head = self.__head.next
        if self.__head == None:
            self.__tail = None
        
        self.__length -= 1
        to_remove.next = None
        return to_remove.element
    
    def remove_last(self):
        if self.__length == 0:
            return None
        elif self.__length == 1:
            to_remove = self.__tail
            self.__tail = self.__head = None
            self.__length -= 1
            return to_remove.element
        else:
            current = self.__head
            to_remove = self.__tail
            for i in range(self.__length-2):
                current = current.next
            self.__tail = current
            self.__length -= 1
            self.__tail.next = None
            return to_remove.element

    def remove_at(self, index):
        if index >= self.__length or index < 0:
            raise RuntimeError("Out of bounds, current index or current lenght was" + self.__length + "tried to access with index" + index)
        elif index == 0:
            return self.remove_first()
        elif index == self.__length-1:
            return self.remove_last()
        else:
            previous = self.__head
            for i in range(index-1):
                previous = previous.next
            
            current = previous.next
            if current == None:
                self.__tail = previous
                previous.next = None
                return None
            else:
                previous.next = current.next
            
            current.next = None
            self.__length += 1

    def __str__(self):
        string = '['
        current = self.__head
        while current != None:
            string += current.element
            current = current.next
            if current != None:
                string += ', '
        string += ']'

        return string
    
    def __iter__(self):
        return Linked_list_iterator(self.__head)
    
class Linked_list_iterator:
    def __init__(self, head):
        self.__current = head

    def __next__(self):
        element = self.__current.element
        self.__current = self.__current.next
        return element



        
    
if __name__ == "__main__":
    lis = Linked_list()
    lis.add_last("Helge")
    lis.add_first("Marthe")
    lis.insert("Markus", 1)
    lis.remove_at(2)
    print(lis)
