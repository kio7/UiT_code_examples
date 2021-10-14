from time import sleep

# Convert element to ASCII value
def convert_elem_to_ASCII(elem):
    code = ord(elem)
    return code

# Convert strint to list
def convert_str_to_list(string):
    lis1 = list(string)
    return lis1

# Sort a list of characters based on the ASCII value
def sort(lis1):
    lis2 = []
    
    while len(lis1) > 0:
        lis2.append(min(lis1))
        lis1.remove(min(lis1))
    
    return lis2

# Convert and sort before checking if it's an Anagram.
def is_anagram(s1, s2):
    new_lis1 = []
    new_lis2 = []
    lis1 = convert_str_to_list(s1)
    lis2 = convert_str_to_list(s2)

    # While lis1 is not empty, add ASCII value of index 0 to new_list and remove index 1
    while len(lis1) > 0:
        new_lis1.append(convert_elem_to_ASCII(lis1[0]))
        lis1.pop(0)

    while len(lis2) > 0:
        new_lis2.append(convert_elem_to_ASCII(lis2[0]))
        lis2.pop(0)

    lis1 = sort(new_lis1)
    lis2 = sort(new_lis2)

    if lis1 == lis2:
        return True

def main():
    s1 = input("Enter the first string: ").lower()
    s2 = input("Enter the second string: ").lower()
    answer = is_anagram(s1, s2)
    
    if answer == True:
        print(f"{s1} and {s2} are Anagram.")

if __name__ == "__main__":
    main()