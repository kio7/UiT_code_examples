class Node:
    def __init__(self, e) -> None:
        self.elm = e
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self, item) -> None:
        self.list = Node(item)
        self.head = self.list
        self.tail = self.list
        self.size = 1
    
    def __getitem__(self, idx):
        if idx < 0 or idx > self.size:
            raise IndexError
        
        if idx == 1:
            return self.head.elm
    
        current = self.head
        for _ in range(idx):
            current = current.next

        return current.elm
            
    def __setitem__(self, idx, item):
        if idx < 0 or idx > self.size:
            raise IndexError

        if idx == 1:
            self.head.elm = item

        current = self.head
        for _ in range(idx):
            current = current.next
        
        current.elm = item

    def __add__(self, list):
        if isinstance(list, MyLinkedList):
            new_lis = MyLinkedList(self.head.elm)

            for i in self:
                if i != self.head.elm:
                    new_lis.append(i)

            for i in list:
                new_lis.append(i)
            
            return new_lis

        else: # Exception handling would be nice here...
            return False


    def __delitem__(self, idx):
        if idx < 0 or idx > self.size:
            raise IndexError

        current = self.head
        for _ in range(idx):
            current = current.next

        if current.prev is not None:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next is not None:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        self.size -= 1


    def __eq__(self, list):
        if isinstance(list, MyLinkedList):
            if len(self) == len(list):
                for i in range(self.size):
                    if self[i] != list[i]:
                        return False
                return True
            return False
        return False


    def __iter__(self):
        ptr = self.head
        while ptr:
            yield ptr.elm
            ptr = ptr.next

    def __len__(self):
        return self.size
    
    def __contains__(self, item):
        crt = self.head
        if crt.elm == item:
            return True
        for _ in range(self.size - 1):
            crt = crt.next
            if crt.elm == item:
                return True
        return False

    def __str__(self):
        end_str = '['
        current = self.head
        for _ in range(self.size):
            end_str += str(repr(current.elm)) + ', '
            current = current.next
        return end_str[:-2] + ']'


    def append(self, item):
        node = Node(item)
        previous = self.tail
        previous.next = node
        node.prev = previous
        self.tail = node
        self.size += 1


    def insert(self, idx, item):
        if idx < 0 or idx > self.size + 1:
            raise IndexError

        else:
            if idx == self.size + 1:
                self.append(item)
            
            elif idx == 0:
                node = Node(item)
                old_head = self.head
                old_head.prev = node
                node.next = old_head
                self.head = node
                self.size += 1
            
            elif idx > self.size / 2: # Over halfway
                node = Node(item)
                next = self.tail

                for _ in range((self.size - idx) - 1):
                    next = next.prev
                previous = next.prev

                previous.next = node
                node.prev = previous
                node.next = next
                next.prev = node

                self.size += 1

            else: # Before halfway
                node = Node(item)
                previous = self.head

                for _ in range(idx - 1):
                    previous = previous.next
                next = previous.next

                previous.next = node
                node.prev = previous
                node.next = next
                next.prev = node

                self.size += 1




if __name__ == '__main__':
    lis = MyLinkedList(10)
    lis.append(20)
    lis.append(30)
    lis.append(40)

    lis_2 = MyLinkedList(10)
    lis_2.append(20)
    lis_2.append(30)
    lis_2.append(40)


    print(lis_2)
    print(lis_2)
