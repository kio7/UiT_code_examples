def Convert(string):
    lis1 = list(string.split(" "))
    return lis1
    
def distinct_list(string):
    lis1 = []
    lis2 = []
    str1 = ""
    space = " "

    # Add all elements in string to lis1
    lis1 = Convert(string)
    # For all elements in lis1, if elem is not found in lis2 then add.
    for elem in lis1[:]:
        if elem not in lis2[:]:
            lis2.append(elem)
    
    # Create a string from lis2
    for x in lis2:
        str1 += x + space
    
    return str1


def main():
    print(distinct_list(input("Enter random numbers with a space between each number: ")))

if __name__ == "__main__":
    main()
