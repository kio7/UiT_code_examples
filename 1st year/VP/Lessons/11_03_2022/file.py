class Heap:
    def __init__(self):
        self.lis = []
    
    def add(self, element):
        self.lis.append(element)
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


def heap_sort(lis):
    heap = Heap()
    for item in lis:
        heap.add(item)
    
    for i in range(len(lis) -1, -1, -1):
        lis[i] = heap.remove_root()

    return lis


if __name__ == "__main__":
    lis = [0, 4, 2, 4, 9, 50]
    print(heap_sort(lis))