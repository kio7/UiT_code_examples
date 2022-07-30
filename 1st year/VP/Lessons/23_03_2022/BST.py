class TreeNode:
    def __init__(self, object):
        self.__element = object
        self.__right = None
        self.__left = None

    @property
    def element(self):
        return self.__element
    
    @property
    def left(self):
        return self.__left
        
    @property
    def right(self):
        return self.__right
    
    @element.setter
    def element(self, value):
        self.__element = value

    @left.setter
    def left(self, value):
        self.__left = value

    @right.setter
    def right(self, value):
        self.__right = value


class BinarySearchTree:
    def __init__(self):
        self.__root = None
        self.__length = 0
    
    @property
    def root(self):
        return self.__root
    
    @root.setter
    def root(self, value):
        self.__root = value
   
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, value):
        self.__length = value
    

    def insert(self, object):
        node = TreeNode(object)
        if self.root == None:
            self.root = node
            self.length += 1

        else:
            current = self.root
            while current != None:
                parent = current
                if object < current.element:
                    current = current.left

                elif object > current.element:
                    current = current.right

                else:
                    return False
            
            if object < parent.element:
                parent.left = node

            else:
                parent.right = node
            
            self.length += 1

    def search(self, object):
        current = self.root
        path = []

        while current != None:
            if object < current.element:
                path.append(current.element)
                current = current.left

            elif object > current.element:
                path.append(current.element)
                current = current.right

            else:
                path.append(current.element)
                return True, path
        return False, path


    def __len__(self):
        return self.length


if __name__ == '__main__':
    bst = BinarySearchTree()
    lis = [15, 10, 20, 17, 25, 8, 12, 9, 13]
    for i in lis:
        bst.insert(i)
    
    print(bst.search(13))
    