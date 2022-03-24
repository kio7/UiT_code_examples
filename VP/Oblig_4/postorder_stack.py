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
            return self.__lis[(2 * index) + 1]

    def right_child(self, index):
        if len(self.__lis) > (2 * index) + 2:
            return self.__lis[(2 * index) + 2]
    
    def index(self, elm):
        return self.__lis.index(elm)
        

    def __len__(self):
        return len(self.__lis)


if __name__ == '__main__':
    stack = Stack()
    stack.push(["Emma", "Isak", "Anders", 'Helge', '1', '2', 10])

    visited = []
    for i in range(len(stack)):
        visited.append(stack.pop())

    print(visited)