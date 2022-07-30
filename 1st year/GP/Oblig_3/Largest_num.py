def locate_largest(a):
    lis1, lis2 = [], []
    largest, b = 0.0, a

    # Get the rows and put them in a multi list
    for i in range(a):
        lis1 = input("Enter a row:  ")
        lis1 = [float(x) for x in lis1.split(" ")]
        a -= 1
        lis2.append(lis1)

    # Find the largest number within the multidimentional-list, save the list and the num
    for x in lis2:
        num = max(x)
        if num > largest:
            largest = num
            lis1 = x
        
    # Find and save the index of the list that contains the largest num
    lis2.append([])
    position = lis2.index(lis1)
    lis2[b].append(position)

    # Find and save the index of the largest num in the list
    position = lis1.index(largest)
    lis2[b].append(position)

    # Return the index of both the list and the num itself.
    return tuple(lis2[-1])

def main():
    number_of_rows = int(input("Enter the number of rows in the list: "))
    
    print(f"The location of the largest element is at {locate_largest(number_of_rows)}")

if __name__ == "__main__":
    main()
