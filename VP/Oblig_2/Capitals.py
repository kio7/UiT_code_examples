import os

def display_capitals():
    dict_of_states = {}

    file_dir = os.path.dirname(__file__)
    with open(file = os.path.join(file_dir, "USCapitals.txt"), mode = "r") as file:
        for _ in range(50):
            file_data = file.readline()
            x = file_data.strip().split(",")
            x[0] = x[0].lower()
            x[1] = x[1][1:] # Removing a blank space before every Capital name
            temp_dict = dict([x])
            dict_of_states.update(temp_dict)

        user_input = input("Enter a Statename: ").lower()

        if user_input in dict_of_states.keys():
            print(dict_of_states.get(user_input))
        else:
            print("That state does not exist.")

if __name__ == "__main__":
    display_capitals()
