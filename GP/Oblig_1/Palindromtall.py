num = (input(f"Enter a 3 digit Integer: "))
x = num
reverse_num = num[::-1]

if(x == reverse_num):
    print(f"The number is palindrome.")
else:
    print(f"Not a palindrome.")