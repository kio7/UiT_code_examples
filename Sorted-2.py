def is_sorted(lis1):
    for x in lis1:
        if x == " ":
            lis1.remove(x)

    lis2 = lis1.copy()
    lis2.sort()

    if lis1 == lis2:
        return True

def main():
    lis1 = list(input("Enter a list of numbers with space bewteen them: "))
    print(f"The list is{'' if is_sorted(lis1) else ' not'} sorted")

if __name__ == "__main__":
    main()
