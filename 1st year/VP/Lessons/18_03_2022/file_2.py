class Stack(): # FILO as in First in, Last out
    def __init__(self):
        self.__lis = []
    
    def pop(self):
        return self.__lis.pop()
    
    def push(self, elem):
        self.__lis.append(elem)
    
    def peek(self):
        return self.__lis[-1]

    def __len__(self):
        return len(self.__lis)
    


class Heap:
    def __init__(self):
        self.lis = []
    
    def add(self, elem):
        self.lis.append(elem)
        current = len(self.lis) - 1
        parent = (current - 1) // 2
        while self.lis[current] > self.lis[parent] and current != 0:
            self.lis[current], self.lis[parent] = self.lis[parent], self.lis[current]
            current = parent
            parent = (current - 1) // 2

    def remove_root(self):
        self.lis[0], self.lis[-1] = self.lis[-1], self.lis[0]
        removed_item = self.lis.pop()
        current = 0
        if len(self.lis) == 0: return removed_item

        while current < len(self.lis):
            left_child = 2 * current + 1
            right_child = 2 * current + 2

            if left_child >= len(self.lis):
                break
            
            left_will_swap = False
            will_swap = False

            # Case is that only left_child and end_of_list
            if right_child == len(self.lis):
                if self.lis[current] < self.lis[left_child]:
                    left_will_swap = True
                    will_swap = True
            else:
                if self.lis[left_child] > self.lis[current]:
                    left_will_swap = True
                    will_swap = True
                    if self.lis[right_child] > self.lis[left_child]:
                        left_will_swap = False
                        will_swap = True
            
            if will_swap:
                index = left_child if left_will_swap else right_child
                self.lis[current], self.lis[index] = self.lis[index], self.lis[current]
                current = index
            else:
                break
        
        return removed_item

class PriorityQueue:
    def __init__(self):
        self.__heap = Heap()
        
    def enter_queue(self, elem):
        self.__heap.add(elem)

    def dequeue(self):
        if self.__heap:
            return self.__heap.remove_root()



def calculator_old_school():
    while True:
        num = input('Give me a number: ')
        try:
            tall = int(tall)
        except:
            print("Expected an integer")
        
        stack.push(num)
        
        if len(stack) == 1:
            num = input('Give me a number')
            try:
                tall = int(tall)
            except:
                print("Expecten an integer")

            stack.push(num)
        
        oper = input('Give me an operator, [+, -, *, /]:  ')
        if oper == '+':
            res = stack.pop() + stack.pop()
            print(res, flush = True)
            stack.push(res)
        elif oper == '-':
            res = stack.pop() - stack.pop()
            print(res, flush = True)
            stack.push(res)
        elif oper == '*':
            res = stack.pop() * stack.pop()
            print(res, flush = True)
            stack.push(res)
        elif oper == '/':
            res = stack.pop() / stack.pop()
            print(res, flush = True)
            stack.push(res)
        else:
            print("You didn't enter a operator that is accepted. You entered ", oper)





if __name__ == "__main__":
    stack = Stack()
    
    # stack.push("1")
    # stack.push("2")
    # stack.push("3")

    # print(stack.peek()) # Should get last element

    # stack.pop()
    # stack.pop()
    # print(stack.pop()) # Should get last element in current list == "1"

    # queue = PriorityQueue()

    # pasient_1 = [1, 'Pål']
    # pasient_2 = [30, 'Per']
    # pasient_3 = [20, 'Nina']
    # pasient_4 = [10, 'Jonne']

    # queue.enter_queue(pasient_1)
    # queue.enter_queue(pasient_2)
    # queue.enter_queue(pasient_3)
    # queue.enter_queue(pasient_4)

    # for _ in range(4):
    #     print(queue.dequeue())

