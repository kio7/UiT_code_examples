def test_anagram(dict):
    string_one = ''.join(sorted(dict.get("one")))
    string_two = ''.join(sorted(dict.get("two")))
    
    return string_one == string_two


def main():
    str1 = input("Enter a string: ").lower()
    str2 = input("Enter another string: ").lower()

    dict_of_strings = {"one": str1, "two": str2}

    print(f"The 2 strings {'are' if test_anagram(dict_of_strings) else 'are not'} Anagram.")


if __name__ == "__main__":
    main()
