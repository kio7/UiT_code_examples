def test_anagram(str1, str2):
    dict_str1 = {}
    dict_str2 = {}
    
    for x in range(len(str1)):
        dict_str1[str1[x]] = dict_str1.get(str1[x], 0) + 1

    for i in range(len(str2)):
        dict_str2[str2[i]] = dict_str2.get(str2[i], 0) + 1

    return dict_str1 == dict_str2


def main():
    str1 = input("Enter a string: ").lower()
    str2 = input("Enter another string: ").lower()

    print(f"The 2 strings {'are' if test_anagram(str1, str2) else 'are not'} Anagram.")


if __name__ == "__main__":
    main()
