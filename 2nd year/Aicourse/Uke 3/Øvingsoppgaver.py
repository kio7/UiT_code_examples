"""Oppgave 1"""
# class Fib_iter:
#     def __init__(self, limit):
#         self.limit = limit
#         self.f1 = 0
#         self.f2 = 1

#     def __next__(self):
#         current = self.f1
#         if current > self.limit:
#             raise StopIteration
        
#         self.f1, self.f2 = self.f2, self.f1 + self.f2
#         return current

#     def __iter__(self):
#         return self


# max_limit = 1_000
# iterator = Fib_iter(max_limit)
# lis = []
# for i in iterator:
#     lis.append(i)

# print(lis)


"""Oppgave 2"""

# def fib_gen():
#     limit = 1_000
#     f1 = 0
#     f2 = 1
#     current = f1
    
#     while current < limit:
#         f1, f2 = f2, f1 + f2
#         yield current
#         current = f1

# val = []
# for i in fib_gen():
#     val.append(i)

# print(val)


"""Oppgave 3"""

class NewInt(int):
    def __init__(self, elm) -> None:
        self.elm = elm

    def is_fibonacci(self):
        f1 = 0
        f2 = 1
        current = f1
        lis = []
        while current <= self.elm:
            f1, f2 = f2, f1 + f2
            lis.append(current)
            current = f1

        if self.elm in lis:
            return True
        return False


# lis = []
# for i in range(1000):
#     lis.append(NewInt(i))

# lis = [x for x in lis if x.is_fibonacci() == True]

# print(lis)


"""Oppgave 4"""

# import time

# int_lis = []
# for i in range(100_000):
#     int_lis.append(NewInt(i))

# start_1 = time.perf_counter_ns()
# lis = [x for x in int_lis if x.is_fibonacci() == True]
# end_1 = time.perf_counter_ns()
# print(end_1 - start_1)

# fib_set = set(int_lis)

# start = time.perf_counter_ns()
# check_lis = [x for x in lis if x in fib_set]
# end = time.perf_counter_ns()

# print(end - start)


""" Øvingsoppgaver Uke 3 """

""" Oppgave 1 """
class Node:
    def __init__(self, e) -> None:
        self.elm = e
        self.next = None
        self.prev = None

""" Oppgave 2 """
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

""" Oppgave 3 """
class Stack(MyLinkedList):
    def __init__(self, item) -> None:
        super().__init__(item)
    
    def push(self, data):
        self.append(data)

    def top(self):
        return self.tail.elm

    def peek(self):
        return self.tail.elm

    def pop(self):
        temp = self.tail.elm
        del self[self.size - 1]
        return temp


if __name__ == '__main__':
    stack = Stack(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)

    for _ in range(len(stack)):
        print(stack.pop())
