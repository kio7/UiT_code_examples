"""
Dijkstra
"""
from queue import PriorityQueue
def dijkstra(graph:dict, take_off:str, arrival:str):
    # Psuedo code: find the shortest distance and print the path.
    
    q = PriorityQueue()
    current = '' # Variable for the planet we're visiting
    visited = []
    my_graph = {} # To not change the input graph i make my own with distances set to inf
    my_graph[take_off] = [0.0, ''] # Starting planet needs distance 0 and 2nd value is 'coming from'
    path = [arrival]

    current = take_off # Starting position aquired.
    for key in graph.keys():
        if key not in my_graph.keys():
            my_graph[key] = [float('inf'), '']


    while current != arrival:
        looking_at:dict = graph[current]
        visited.append(current)

        for key, value in looking_at.items():
            if key in visited: continue
            q.put((value, key))

        for key, value in looking_at.items():
            if my_graph[key][0] > (my_graph[current][0] + value): 
                my_graph[key] = [my_graph[current][0] + value, current]

        current = q.get()[1]
    
    # Make path in reverse from target to start.
    current = arrival
    
    while path[-1] != take_off:
        current = my_graph[current][1]
        path.append(current)


    path.reverse()
    print(f"Distance: {my_graph[arrival][0]}, Path: {path}")

"""
Iterator, Fibonacci tallene mellom 0 og limit
"""
class Fib:
    def __init__(self, limit):
        self.limit = limit
        self.f1 = 0
        self.f2 = 1

    def __next__(self):
        current = self.f1
        if current > self.limit:
            raise StopIteration
        
        self.f1, self.f2 = self.f2, self.f1 + self.f2
        return current

    def __iter__(self):
        return self

def run_fib():
    max_limit = 1_000
    iterator = Fib(max_limit)
    lis = []
    for i in iterator:
        lis.append(i)

    print(lis)

"""
Heap og heapsort
"""
class Heap:
    def __init__(self):
        self.lst = []

    # Add a new item into the lst 
    def add(self, e):
        self.lst.append(e)  # Append to the lst
        # The index of the last node
        current_index = len(self.lst) - 1  
    
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            # Swap if the current item is greater than its parent
            if self.lst[current_index][0] > self.lst[parent_index][0]: 
                self.lst[current_index], self.lst[parent_index] = \
                    self.lst[parent_index], self.lst[current_index]
            else:
                break  # The tree is a lst now
    
            current_index = parent_index

    # Remove the root from the lst 
    def remove(self):
        if len(self.lst) == 0:
            return None
    
        removed_item = self.lst[0]
        self.lst[0] = self.lst[len(self.lst) - 1]
        self.lst.pop(len(self.lst) - 1) # Remove the last item
    
        current_index = 0
        while current_index < len(self.lst):
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
          
            # Find the maximum between two children
            if left_child_index >= len(self.lst): 
                break  # The tree is a lst
            max_index = left_child_index
            if right_child_index < len(self.lst):
                if self.lst[max_index] < self.lst[right_child_index]:
                    max_index = right_child_index
          
            # Swap if the current node is less than the maximum 
            if self.lst[current_index] < self.lst[max_index]:
                self.lst[max_index], self.lst[current_index] = \
                    self.lst[current_index], self.lst[max_index]
                current_index = max_index
            else:
                break  # The tree is a lst
    
        return removed_item


def heap_sort(lis:list):
    heap = Heap() # Create a Heap 

    # Add elements to the heap
    for v in lis:
        heap.add(v)

    # Remove elements from the heap
    for i in range(len(lis)): 
        lis[len(lis) - 1 - i] = heap.remove()

"""
Binary Search Tree, med bruk av klassen Node.
"""
from binarytree import Node
import warnings
from copy import deepcopy
class BinarySearchTree:
    def __init__(self, root = None) -> None:
        """ Initialize binary search tree

        # Inputs:
        root:    (optional) An instance of Node which is the root of the tree

        # Notes:
        If a root is supplied, validate that the tree meets the requirements
        of a search tree. If not, raise ValueError.
        """

        if root:
            if isinstance(root, Node): # less errors for wrong input
                if root.is_bst:
                    self.root = root
                else:
                    raise ValueError('Input does not meet the requirements of a BST')
            else:
                raise ValueError('Input is not a of the type Node')
        else:
            self.root = None


    def insert(self, value, node:Node = None) -> None:
        """ Insert a new node into the tree 

        # Inputs:
        value:    Value of new node

        # Notes:
        The method should issue a warning if the value already exists in the tree.
        See https://docs.python.org/3/library/warnings.html#warnings.warn
        In the case of duplicate values, leave the tree unchanged.
        """

        if self.root is None:
            self.root = Node(value)
            return

        if node is None:
            node = self.root

        if node.value == value:
            warnings.warn("Tried adding a duplicate value, tree is unchanged")
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert(value, node.right)


    def find(self, value) -> Node:
        """ Find node with given value, return node

        # Inputs:
        value:    Value of node to be found

        # Returns:
        node:     Node object containing given value

        # Notes:
        - The function should raise a KeyError if the value
        is not found in the tree.
        """

        node = self.root
        if value not in node.values:
            raise KeyError('Value is not in BST')

        while True: # Find node
            if value > node.value:
                if node.right:
                    node = node.right

            elif value < node.value:
                if node.left:
                    node = node.left

            elif value == node.value:
                return node


    def delete(self, value) -> Node:
        """ Delete node with given value

        # Inputs:
        value:    Value of node to be deleted

        # Notes:
        This function should handle a number of "regular" cases:
        - Deleting a leaf node
        - Deleting a node with one child
        - Deleting a node with two childen
          (the node should be replaced with its inorder successor)

        It should also handle the following "edge cases":
        - Value not found in tree (raise KeyError)
        - Deleting the root node
        - Calling delete on an empty tree (raise KeyError)
        """

        if self.root == 0:
            raise KeyError("Empty tree")

        if value not in self.root.values:
            raise KeyError("Value not found")

        node = self.find(value)
        node_to_return = deepcopy(node)

        # Regular case, deleting leaf node
        if node.left is None and node.right is None:
            # Find parent
            parent = self.root

            while True:
                if node.value > parent.value and parent.right != node:
                    parent = parent.right
                elif node.value < parent.value and parent.left != node:
                    parent = parent.left
                else:
                    break

            if parent.left == node:
                parent.left = None
            elif parent.right == node:
                parent.right = None
            return node_to_return
    

        # Use inorder
        next = self.root.inorder
        for i in next:
            if i == node:
                next = next[next.index(i) + 1]
                break

        next_parent = node
        while True:
            if next.value > next_parent.value and next_parent.right != next:
                next_parent = next_parent.right
            elif next.value < next_parent.value and next_parent.left != next:
                next_parent = next_parent.left
            else:
                break

        if next == next_parent.left:
            if next_parent.left.right:
                next_parent.left, node.value = next_parent.left.right, next.val
            else:
                next_parent.left, node.value = None, next.val

        elif next == next_parent.right:
            if next_parent.right.right:
                next_parent.right, node.value = next_parent.right.right, next.val
            else:
                next_parent.right, node.value = None, next.val

        return node_to_return


    def level(self, value) -> int:
        """ Return level of node with given value

        # Inputs:
        value:    Value of node 

        # Returns:
        level     The level of the node with the given value.
                  The root node has level 0, its children have level 1, etc.
        """

        nodes = self.root.levels
        for i in nodes:
            temp = [elm.value for elm in i]
            if value in temp:
                return nodes.index(i)


"""
Linked list, med maaange dunder methods.
"""
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


"""

"""
