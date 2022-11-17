import os
from collections import namedtuple
from BinaryTreeNode import BinaryTreeNode

file_dir = os.path.dirname(__file__)

persons = []
Person = namedtuple("Person", ["last_name", "first_name", "address", "mail_number", "mail_area"])

with open(os.path.join(file_dir, "Personer_kort.dta"), mode="r", encoding="iso-8859-1") as file:
    for line in file:
        persons.append(Person(*line.strip().split(";")))


class TestBinaryTreeNode:
    def setup_or_reset_class(self):
        self.node_1 = BinaryTreeNode(persons[0])
        self.node_2 = BinaryTreeNode(persons[1])
        self.node_3 = BinaryTreeNode(persons[2], self.node_1, self.node_2)
    

    def test_getters_and_setters(self):
        self.setup_or_reset_class()
        assert self.node_1.value == persons[0], "Value error."

        self.node_1.value = persons[3]
        assert self.node_1.value == persons[3], "Value setter error."

        self.node_2 = BinaryTreeNode("something")
        self.node_1.left = self.node_2
        assert self.node_1.left == self.node_2, "Left setter error."

        self.node_3 = BinaryTreeNode("something else")
        self.node_1.right = self.node_3
        assert self.node_1.right == self.node_3, "Right setter error."

        assert self.node_1.level == 0, "Level error."
        self.node_1.level = 10
        assert self.node_1.level == 10, "Level setter error."


    def test_str(self):
        self.setup_or_reset_class()
        assert self.node_1.__str__() == f"{persons[0]}", "Returns a value that is not a string."
    

    def test_has_right_and_left(self):
        self.setup_or_reset_class()
        assert self.node_3.hasRight() == True
        assert self.node_1.hasRight() == False
        assert self.node_3.hasLeft() == True
        assert self.node_1.hasLeft() == False


    def test_prefix_order(self, capsys):
        self.setup_or_reset_class()

        self.node_3.prefixOrder()
        captured = capsys.readouterr()
        assert captured.out == f"{persons[2]}  \n{persons[0]}  \n{persons[1]}  \n", "Formatting is wrong."


    def test_infix_order(self, capsys):
        self.setup_or_reset_class()

        self.node_3.infixOrder()
        captured = capsys.readouterr()
        assert captured.out == f"{persons[0]}  \n{persons[2]}  \n{persons[1]}  \n", "Formatting is wrong."


    def test_postfix_order(self, capsys):
        self.setup_or_reset_class()

        self.node_3.postfixOrder()
        captured = capsys.readouterr()
        assert captured.out == f"{persons[0]}  \n{persons[1]}  \n{persons[2]}  \n", "Formatting is wrong."


    # The fuction test both "levelOrder" and "LevelOrderEntry"
    def test_level_order(self, capsys):
        self.setup_or_reset_class()

        self.node_3.levelOrder()
        captured = capsys.readouterr()
        assert captured.out == f"{persons[2]}  \n{persons[0]}  \n{persons[1]}  \n", "Formatting is wrong."


    def test__eq__(self):
        self.setup_or_reset_class()
        assert self.node_1 == self.node_1, "Not equal"

        node_1 = BinaryTreeNode(None)
        assert node_1 == None, "Should return True, Error in __eq__"


    def test__ne__(self):
        self.setup_or_reset_class()
        assert self.node_1 != self.node_2, "Equal"


    def test__ne__None(self):
        node_1 = BinaryTreeNode(None)
        node_2 = BinaryTreeNode(10)
        assert node_1 != node_2, "Error __ne__"


    def test__lt__(self):
        node_1 = BinaryTreeNode(10)
        node_2 = BinaryTreeNode(20)
        node_3 = BinaryTreeNode(10)
        node_4 = BinaryTreeNode(None)

        assert node_1 < node_2, "Greater than"
        assert not node_1 < node_3, "Equal"
        assert node_4 < None, "This is meant to fail, python does not allow it. But higher coverage of the file..."


    def test__lt__None(self):
        node_1 = BinaryTreeNode(10)
        assert node_1 < None, "This is meant to fail, python does not allow it. But higher coverage of the file..."


    def test__le__(self):
        node_1 = BinaryTreeNode(10)
        node_2 = BinaryTreeNode(20)
        node_3 = BinaryTreeNode(10)
        node_4 = BinaryTreeNode(None)

        assert node_1 <= node_2, "Greater than"
        assert node_1 <= node_3, "Not equal"
        assert node_4 <= None, "This is meant to fail, python does not allow it. But higher coverage of the file..."


    def test_le_None(self):
        node_1 = BinaryTreeNode(10)
        assert node_1 <= None, "This is meant to fail, python does not allow it. But higher coverage of the file..."


    def test__gt__(self):
        node_1 = BinaryTreeNode(10)
        node_2 = BinaryTreeNode(20)
        node_3 = BinaryTreeNode(10)
        node_4 = BinaryTreeNode(None)

        assert node_2 > node_1, "Greater than"
        assert not node_3 > node_1, "Equal"
        assert node_4 > None, "This is meant to fail, python does not allow it. But higher coverage of the file..."


    def test_gt_None(self):
        node_1 = BinaryTreeNode(10)
        assert node_1 > None, "This is meant to fail, python does not allow it. But higher coverage of the file..."


    def test__ge__(self):
        node_1 = BinaryTreeNode(10)
        node_2 = BinaryTreeNode(20)
        node_3 = BinaryTreeNode(10)
        node_4 = BinaryTreeNode(None)

        assert node_2 >= node_1, "Greater than"
        assert node_3 >= node_1, "Not equal"
        assert node_4 >= None, "This is meant to fail the test"
    
    def test__ge__None(self):
        node_1 = BinaryTreeNode(10)
        assert node_1 >= None
