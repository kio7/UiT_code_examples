def is_consecituve_four(values):
    for x in values:
        if x == " ":
            values.remove(x)
    
    for y in values[:-3]:
        position = values.index(y)
        
        if y == values[position] and y == values[position+1] and y == values[position+2] and y == values[position+3]:
            return True

def main():
    user_input = list(input("Enter integers separated by spaces from one line: "))
    print(f"The series has{'' if is_consecituve_four(user_input) else ' no'} consecutive fours")

if __name__ == "__main__":
    main()
    