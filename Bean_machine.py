def bean_machine(slots, balls):
    from random import randint

    dic_of_slots = {}
    lis_of_01, temp_lis = [], []
    index = 0

    
#   Create list of 0 and 1 "50/50" then add list into a storage list
    for i in range(0,balls):
        for i in range(0, slots):
            temp_lis.append(randint(0,1))
        lis_of_01.append(temp_lis)
        temp_lis = []


#   Create all possible slots
    for i in range(0,slots):
        dic_of_slots[i] = 0


#   Add balls in correct slot
    index = 0
    for x in range(0,balls):
        position = sum(lis_of_01[index])
        index += 1
        
        if position-1 in dic_of_slots.keys():
            dic_of_slots[position-1] += 1

    return(dic_of_slots, lis_of_01)
    

#   First print the "directions", then the answer.
def print_answer(dic, lis_of_01):
    lis_of_str = []
    index = 0
    temp_str = ""
    

    for i in lis_of_01:
        for elem in lis_of_01[index]:
            if elem == 0:
                temp_str += "L"
            if elem == 1:
                temp_str += "R"
                
        index += 1
        lis_of_str.append(temp_str)
        temp_str = ""
    
    
    answer = input("Do you want to print LR's? Yes/No: ").lower()
    if answer == "yes":
        for i in lis_of_str:
            print(i)

    print("="*30)

    maximum = max(dic)
    index = maximum

    for i in range(0,maximum):
        for value in dic.values():
            if value >= index:
                print("|0", end='')
            else:
                print("| ", end ='')

        print('|')
        index -= 1

    for values in dic.values():
        print(f'|{values}', end = '')
    print('|')
                

def main():
    num_of_balls = int(input("Enter a number of balls to drop: "))
    num_of_slots = int(input("Enter a number of slots: "))

    dic, lis = bean_machine(num_of_slots, num_of_balls)
    
    print_answer(dic, lis)

if __name__ == "__main__":
    main()
