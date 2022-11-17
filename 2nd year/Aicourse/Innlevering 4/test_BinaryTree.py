import os
from collections import namedtuple
from BinaryTree import BinaryTree
from BinaryTreeNode import BinaryTreeNode

file_dir = os.path.dirname(__file__)

persons = []
Person = namedtuple("Person", ["last_name", "first_name", "address", "mail_number", "mail_area"])

with open(os.path.join(file_dir, "Personer_kort.dta"), mode="r", encoding="iso-8859-1") as file:
    for line in file:
        persons.append(Person(*line.strip().split(";")))


class TestBinaryTree:
    def setup_or_reset_class(self):
        self.tree  = BinaryTree()
        self.tree.insert(None, None, persons[0])
        self.tree.insert(None, None, persons[1])
        self.tree.insert(None, None, persons[2])
        self.tree.insert(None, None, persons[3])
        self.tree.insert(None, None, persons[4])
        self.tree.insert(None, None, persons[5])
        self.tree.insert(None, None, persons[6])
        self.tree.insert(None, None, persons[7])
        self.tree.insert(None, None, persons[8])
        self.tree.insert(None, None, persons[9])
        

    def test_init__(self):
        tree = BinaryTree()
        assert isinstance(tree, BinaryTree) == True
        tree = BinaryTree(BinaryTreeNode("Something"))
        assert isinstance(tree, BinaryTree) == True

    def test_find_left_most_and_min(self):
        tree = BinaryTree()
        tree.insert(value="2")
        tree.insert(value="1")
        tree.insert(value="3")

        assert tree.findLeftMost(tree._root) == BinaryTreeNode("1"), "Error, Tree has been setup incorrectly"
        assert tree.findMin() == BinaryTreeNode("1"), "Error, Tree has been setup incorrectly"

    def test_find_right_most(self):
        self.setup_or_reset_class()
        assert self.tree._root.right.right.right == self.tree.findRightMost(self.tree._root), "Error, Tree has been setup incorrectly"

    def test_find_max(self):
        self.setup_or_reset_class()
        assert self.tree._root.right.right.right == self.tree.findMax(), "Error, Tree has been setup incorrectly"

    def test_find(self):
        self.setup_or_reset_class()
        assert self.tree.find(persons[2]) == self.tree._root.left, "find function did not locate the correct node."
        assert self.tree.find(persons[1]) == self.tree._root.right, "find function did not locate the correct node."
        tree = BinaryTree()
        assert tree.find(None) == None

    def test__getnodes(self):
        self.setup_or_reset_class()
        assert 5, 6 == self.tree._getnodes(5, 6)
        assert self.tree._root, self.tree._root.right == self.tree._getnodes(self.tree._root.left, self.tree._root.right, self.tree._root.right)

    def test__getnodes_2(self):
        self.setup_or_reset_class()
        assert self.tree._getnodes(BinaryTreeNode("something"), BinaryTreeNode("something else"))
        
    def test__getnodes_key_inconsistency(self):
        self.setup_or_reset_class()
        assert self.tree._getnodes(None, BinaryTreeNode(5), 7)

    def test__getnodes_exception_1(self):
        self.setup_or_reset_class()
        assert self.tree._getnodes(self.tree._root, None)

    # There is a problem with reaching following exception: "Attempt to insert an Node..." see error message.
    def test__getnodes_exception_2(self):
        self.setup_or_reset_class()
        self.tree._root.value = None
        assert self.tree._getnodes(treenode = self.tree._root), "Coding mistake in BinaryTreeNode.__eq__"
    
    def test_insert(self):
        tree = BinaryTree()
        tree.insert(value=2)
        assert isinstance(tree.insert(value=1), BinaryTreeNode) == True
        assert isinstance(tree.insert(value=3), BinaryTreeNode) == True
        assert isinstance(tree.insert(value=0), BinaryTreeNode) == True
        assert isinstance(tree.insert(value=4), BinaryTreeNode) == True

    def test_insert_2(self):
        tree = BinaryTree()
        tree.insert(value="2")
        assert tree.insert(current=tree._root, value="2"), "Exception: 'Duplicate key: x'"

    def test_insert_3(self):
        tree = BinaryTree()
        node = BinaryTreeNode("test")
        assert tree.insert(current=node, value="test")

    def test_del_min(self):
        self.setup_or_reset_class()
        
        assert self.tree.deleteMin()
        tree = BinaryTree()
        tree.insert(value="30")
        tree.insert(value="20")
        tree.insert(value="25")
        assert tree.deleteMin()
        tree_2 = BinaryTree()
        tree_2.insert(value="30")
        assert tree_2.deleteMin() == None


    def test_del_max(self):
        self.setup_or_reset_class()

        assert self.tree.deleteMax()
        tree = BinaryTree()
        tree.insert(value="30")
        tree.insert(value="40")
        tree.insert(value="35")
        assert tree.deleteMax()


    def test_del(self):
        self.setup_or_reset_class()

        assert self.tree.delete(persons[0])
        assert self.tree.delete(persons[2])
        assert self.tree.delete(persons[5])
        assert self.tree.delete(persons[9])
        assert self.tree.delete(persons[8])
        

        tree = BinaryTree()
        tree.insert(value="1")
        assert tree.delete("1")

        tree.insert(value="1")
        tree.insert(value="2")
        assert tree.delete("1")

        tree = BinaryTree()
        tree.insert(value="30")
        tree.insert(value="40")
        tree.insert(value="25")
        tree.insert(value="35")
        assert tree.delete("40")
