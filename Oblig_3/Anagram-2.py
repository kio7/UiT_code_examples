def is_anagram(str1, str2):
    lis1, lis2 = [], []

    for elem in str1:
        lis1.append(elem)
    for elem in str2:
        lis2.append(elem)
        
    lis1 = sorted(lis1)
    lis2 = sorted(lis2)

    if lis1 == lis2:
        return True
    else:
        return False

def main():
    str1, str2 = input("Enter a string: ").lower(), input("Enter another string: ").lower()
    print(f"Is{'' if is_anagram(str1, str2) else ' not'} Anagram.")
    
if __name__ == "__main__":
    main()
