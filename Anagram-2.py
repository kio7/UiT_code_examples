def is_anagram(lis1, lis2):
    if list(lis1).sort() == list(lis2).sort(): return True

def main():
    lis1, lis2 = input("Enter a string: ").lower(), input("Enter another string: ").lower()
    print(f"Is{'' if is_anagram(lis1, lis2) else ' not'} Anagram.")
    
if __name__ == "__main__":
    main()
