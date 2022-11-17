import os

file_dir = os.path.dirname(__file__)

persons = []

with open(os.path.join(file_dir, "Personer.dta"), mode="r", encoding="ISO-8859-1") as file:
    for line in file:
        persons.append(line)

temp_lis = []
for i in range(len(persons)):
    temp_lis = persons[i].strip().split(";")
    persons[i] = temp_lis

# for i in range(1, 6):
#     print(persons[-i])

# for i in range(len(persons) - 5, len(persons)):
#     print(persons[i])

# mail_number = {}
# for i in persons:
#     if i[3] in mail_number.keys():
#         mail_number[i[3]] += 1
#     else:
#         mail_number[i[3]] = 1

# print(f"Antall unike postnummer: {len(mail_number)}")

# last_names = {}
# for i in persons:
#     if i[0] in last_names.keys():
#         last_names[i[0]] += 1
#     else:
#         last_names[i[0]] = 1

# temp_lis = []
# for key, value in last_names.items():
#     temp_lis.append([value, key])

# for _ in range(10):
#     key = max(temp_lis)
#     print(f"Navn: {key[1]}, antall ganger: {key[0]}")
#     del(temp_lis[temp_lis.index(key)])





class Heap:
    def __init__(self):
        self.lst = []

    # Add a new item into the lst 
    def add(self, e):
        self.lst.append(e)  # Append to the lst
        # The index of the last node
        current_index = len(self.lst) - 1  
    
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            # Swap if the current item is greater than its parent
            if self.lst[current_index][0] > self.lst[parent_index][0]: 
                self.lst[current_index], self.lst[parent_index] = \
                    self.lst[parent_index], self.lst[current_index]
            else:
                break  # The tree is a lst now
    
            current_index = parent_index

    # Remove the root from the lst 
    def remove(self):
        if len(self.lst) == 0:
            return None
    
        removed_item = self.lst[0]
        self.lst[0] = self.lst[len(self.lst) - 1]
        self.lst.pop(len(self.lst) - 1) # Remove the last item
    
        current_index = 0
        while current_index < len(self.lst):
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
          
            # Find the maximum between two children
            if left_child_index >= len(self.lst): 
                break  # The tree is a lst
            max_index = left_child_index
            if right_child_index < len(self.lst):
                if self.lst[max_index] < self.lst[right_child_index]:
                    max_index = right_child_index
          
            # Swap if the current node is less than the maximum 
            if self.lst[current_index] < self.lst[max_index]:
                self.lst[max_index], self.lst[current_index] = \
                    self.lst[current_index], self.lst[max_index]
                current_index = max_index
            else:
                break  # The tree is a lst
    
        return removed_item


def heap_sort(lis:list):
    heap = Heap() # Create a Heap 

    # Add elements to the heap
    for v in lis:
        heap.add(v)

    # Remove elements from the heap
    for i in range(len(lis)): 
        lis[len(lis) - 1 - i] = heap.remove()

heap_sort(persons)

print(persons[0])
print(persons[20_000])
print(persons[40_000])
print(persons[60_000])
print(persons[80_000])
