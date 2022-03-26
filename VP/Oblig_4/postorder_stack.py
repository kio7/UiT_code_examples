# Made in collaberation with Anders Karkskås and Jørgen Nordås

class Stack:
    def __init__(self):
        self.__elements = []

    # Return true if the stack is empty
    def is_empty(self):
        return len(self.__elements) == 0
    
    # Returns the element at the top of the stack 
    # without removing it from the stack.
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__elements[-1]

    # Stores an element into the top of the stack
    def push(self, value):    
        self.__elements.append(value)

    # Removes the element at the top of the stack and returns it
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.__elements.pop() 
    
    # Return the size of the stack
    def __len__(self):
        return len(self.__elements)


class Node:
    def __init__(self, e):
        self.element = e
        self.left = None  # Point to the left node, default None
        self.right = None # Point to the right node, default None


# Gotten from 'https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/'
def postorderIterative(root):
 
    # return if the tree is empty
    if root is None:
        return
 
    # create an empty stack and push the root node
    stack = Stack()
    stack.push(root)
 
    # create another stack to store postorder traversal
    out = Stack()
 
    # loop till stack is empty
    while stack:
 
        # pop a node from the stack and push the data into the output stack
        current = stack.pop()
        out.push(current.element)
 
        # push the left and right child of the popped node into the stack
        if current.left:
            stack.push(current.left)
 
        if current.right:
            stack.push(current.right)
 
    # print postorder traversal
    while out:
        print(out.pop(), end=' ')


if __name__ == '__main__':
    
    ''' Given test tree:
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    '''

    # Test Tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    postorderIterative(root)
    # Print of this tree should be 4, 2, 7, 8, 5, 6, 3, 1
