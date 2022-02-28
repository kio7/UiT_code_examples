from random import randint

def eq2text(list):
    string = ""
    list = [str(i) for i in list]
    for count, elem in enumerate(list):
        if count == 0:
            if elem == "1":
                string += f"x "

            elif elem == "-1":
                string += f"-x "

            else:
                string += f"{elem}x "

        if count == 1:
            if int(elem) > 0:
                string += f"+ {elem} = "
            else:
                string += f"{elem[0]} {elem[1]} = "
    
        if count == 2:
            if int(elem) > 0:
                if elem == "1":
                    string += f"x "
                else:
                    string += f"{elem}x "
            else:
                if elem == "-1":
                    string += f"-x "
                else:
                    string += f"{elem[0]} {elem[1]}x "
    
        if count == 3:
            if int(elem) > 0:
                string += f"+ {elem}"
            else:
                string += f"{elem[0]} {elem[1]}"

    return string


def ok(list):
    if 0 in list:
        return False
    elif list[0] == list[2]:
        return False
    elif list[1] == list[3]:
        return False
    else:
        return True


def make_n_eqs(n):
    list_of_eqs = []
    count = 0
    helper = 1
    while True:
        temp = [randint(-9, 9), randint(-9, 9), randint(-9, 9), randint(-9, 9)]
        if ok(temp) and count < n and temp not in list_of_eqs:
            if list_of_eqs:
                copy_list = list_of_eqs.copy()
                copy_list = sorted(copy_list)
                temp_sorted = sorted(temp)
                if temp_sorted in copy_list:
                    helper = 0
            if helper:
                list_of_eqs.append(temp)
                count += 1
                helper = 1

        elif count == n:
            break
    
    return list_of_eqs
    
    
def make_tests(students, n):
    dict_of_tests = {}

    for elem in students:
        dict_of_tests[elem] = make_n_eqs(n)

    return dict_of_tests


def ask_questions(D):
    while True:
        name  = input("Enter your name: ")
        if name in D.keys():
            break

    alphabeth = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print("Please solve these equations:")
    questions = D.get(name)
    for elem in questions:
        print(f"{alphabeth[questions.index(elem)]})  ", end = '')
        print(eq2text(elem))
        answer = float(input("x = "))
        elem.append(answer)
    D[name] = questions

    return D


def main():
    tests = make_tests(["Ola", "Kari", "Fredrik"], 5)
    ask_questions(tests)
    print(tests)

if __name__ == "__main__":
    main()
    