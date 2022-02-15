import os
from tkinter.font import BOLD

def main():
    dir_name = os.path.dirname(__file__)
    
    with open(os.path.join(dir_name, "file_1.txt"), "r") as file:
        file_1 = file.read()
        
    with open(os.path.join(dir_name, "file_2.txt"), "r") as file:
        file_2 = file.read()
    
    file_1 = file_1.split(" ")
    file_2 = file_2.split(" ")
    file_1_and_2 = []
    for x in file_1:
        file_1_and_2.append(x)
    for x in file_2:
        file_1_and_2.append(x)

    file_1_set = set(file_1)
    file_2_set = set(file_2)
    file_1_and_2_set = set(file_1_and_2)

    list_for_unique_in_file_1 = []
    list_for_unique_in_file_2 = []

    for i in file_1_set:
        if i not in file_2_set:
            list_for_unique_in_file_1.append(i)
    
    for i in file_2_set:
        if i not in file_1_set:
            list_for_unique_in_file_2.append(i)
    
    print(f"Amount of unique words total: {len(list_for_unique_in_file_1) + len(list_for_unique_in_file_2)}")

    print_line(40)
    print("All unique words in both files below:")
    for elem in list_for_unique_in_file_1:
        print(elem, end = "  ")
    for elem in list_for_unique_in_file_2:
        print(elem, end = "  ")

    print_line(40)
    print("Unique words in file_1 and file_2:")
    for i in  file_1_set:
        print(i, end = "  ")
    for i in file_2_set:
        print(i, end = "  ")

    print_line(40)
    print("Unique words that are only in file_1:")
    for i in file_1_set:
        if i not in file_2_set:
            print(i, end = "  ")

    print_line(40)
    print("Unique words that are only in file_2:")
    for i in file_2_set:
        if i not in file_1_set:
            print(i, end = "  ")

    print("Unique words in both files combined:")
    for elem in file_1_and_2_set:
        print(elem, end = "  ")
    
    print_line(40)


def print_line(amount):
    print('')
    print("=" * amount)


if __name__ == "__main__":
    main()
