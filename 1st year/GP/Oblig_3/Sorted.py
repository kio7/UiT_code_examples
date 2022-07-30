def is_sorted(lis1):
#    lis2 = sorted(lis1)
#
#    if lis1 == lis2:
#        return True

    # Sort lis1
    original = lis1.copy()
    lis2 = []

    while len(lis1) > 0:
        lis2.append(min(lis1))
        lis1.remove(min(lis1))
        
    if original == lis2: 
        return True

def convert(string):
    lis1 = list(string.split(" "))
    return lis1


def main():
    
    lis1 = input("Enter a list of numbers with space between them: ")
    lis1 = convert(lis1)
    answer = is_sorted(lis1)
    
    print("="*25)
    if answer == True:
        print("The list is already sorted!")
    
    else:
        print("The list is not sorted.")
    print("="*25)

if __name__ == "__main__":
    main()
