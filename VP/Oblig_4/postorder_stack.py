class Stack(): # FILO as in First in, Last out
    def __init__(self):
        self.__lis = []
    
    def pop(self):
        return self.__lis.pop()
    
    def push(self, elem):
        if isinstance(elem, list):
            for i in elem:
                self.__lis.append(i)
        else:
            self.__lis.append(elem)
    
    def peek(self):
        return self.__lis[-1]

    def left_child(self, index):
        if len(self.__lis) > (2 * index) + 1:
            if self.__lis[(2 * index) + 1] == None:
                return None
            return self.__lis[(2 * index) + 1]

    def right_child(self, index):
        if len(self.__lis) > (2 * index) + 2:
            if self.__lis[(2 * index) + 2] == None:
                return None
            return self.__lis[(2 * index) + 2]
    
    def index(self, elm):
        return self.__lis.index(elm)
    
    def remove(self, elm):
        self.__lis.pop(self.__lis.index(elm))
    
    def replace_with_None(self, elm):
        self.__lis[self.__lis.index(elm)] = None
        

    def __len__(self):
        return len(self.__lis)


def post_order(elem):
    original = elem.copy()
    stack_2 = Stack()
    stack_2.push(elem[0])

    stack_1 = Stack()
    stack_1.push(elem)

    current = None
    tag = 0


    while len(original) > len(stack_2):
        if current != stack_2.peek(): #
            previous = current
            current = stack_2.peek()
        else:
            current = previous
        if tag:
            current = elem[int((index / 2) - 1)]
            tag = 0
        
        if stack_1.right_child(elem.index(current)):
            stack_2.push(elem[(2 * elem.index(current)) + 2])

        elif stack_1.left_child(elem.index(current)):
            stack_2.push(elem[(2 * elem.index(current)) + 1])

        else:
            to_be_removed = stack_2.peek()
            if to_be_removed in elem:
                stack_1.remove(to_be_removed)
                del elem[elem.index(to_be_removed)]
            else:
                index = elem.index(current)
                stack_1.replace_with_None(current)
                tag = 1

    for _ in range(len(stack_2)):
        print(stack_2.pop())


if __name__ == '__main__':
    elements = ["Emma", "Isak", "Anders", 'Helge', '1', '2', 10]
    post_order(elements)

    # Post order should be: Helge, 1, Isak, 2, 10, Anders, Emma

    # Stack Oder: Emma, Anders, 10, 2, Isak, 1, Helge
