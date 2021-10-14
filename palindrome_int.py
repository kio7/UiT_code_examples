# Return the reveral of an integer, e.g. reverse(456) retruns 654
def reverse(number):
    reverse_num = 0

    while(number > 0):
        remainder = number % 10
        reverse_num = (reverse_num * 10) + remainder
        number = number // 10
    
    return reverse_num

# Return true if number is palindrome
def is_palindrome(number):
    reverse_num = 0
    original_num = number

    while(number > 0):
        remainder = number % 10
        reverse_num = (reverse_num * 10) + remainder
        number = number // 10

    if reverse_num == original_num:
        return True

def main():
    reverse_num = reverse(int(input("Enter an Integer: ")))
    # Revert input into originaly entered number
    original_num = reverse(reverse_num)

    if is_palindrome(reverse_num) == True:
        print(f"The number {original_num} is a palindrome.")
    else:
        print(f"The number {original_num} is not a palindrome.")

if __name__ == "__main__":
    main()
