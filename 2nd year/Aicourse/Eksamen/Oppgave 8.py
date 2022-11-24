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


def populate_node_dict(node, nodedict):
    nodedict[node.value] = node
    if node.left:
        populate_node_dict(node.left, nodedict)
    if node.right:
        populate_node_dict(node.right, nodedict)


nodedict = {}
nodes = [15, 8, 23, 3, 13, 19, 27, 1, 5, 11, 14, 17, 25]
bst = BinarySearchTree(Node(nodes[0]))
for i in nodes[1:]:
    bst.insert(i)

populate_node_dict(bst.root, nodedict)


parent = nodedict[15] # Get the parent node of node 8
parent.left.value = nodedict[11].value # Replace the value of the node with value 8 with 11
nodedict[13].left = None # remove the node from the BST

parent = nodedict[23] # Get the parent node of node 19
parent.left = parent.left.left # Since 17 is a leaf node, replace 19 with 17 and 19 will be collected by the garbage collector

parent = nodedict[27] # Get the parent node of node 25
parent.left = None # Since 25 is a leaf node it can be deleted with no other changes.


print(nodedict[15])

