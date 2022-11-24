class MyNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def met(node):
    ret_str = ''
    if node.left != None:
        ret_str += met(node.left)
    if node.right != None:
        ret_str += met(node.right)
    ret_str += str(node.value) + ', '
    return ret_str

node_5 = MyNode(32)
node_4 = MyNode(18)
node_3 = MyNode(12)
node_1 = MyNode(8, node_3)
node_2 = MyNode(21, node_4, node_5)
root = MyNode(15, node_1, node_2)



x = met(root)
print(x)
