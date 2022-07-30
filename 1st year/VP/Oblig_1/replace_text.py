import os

# Filen som har blitt opprettet for å teste denne er: "test.txt"

def replace_text(filename, old_string, new_string):
    file_dir = os.path.dirname(__file__)    
    with open(os.path.join(file_dir, filename), "r") as file:
        file_data = file.read()

    file_data = file_data.replace(old_string, new_string)
    
    with open(os.path.join(file_dir, filename), "w") as file:
        file.write(file_data)


def main():
    filename = input("Enter a filename: ")
    old_string = input("Enter the old string to be replaced: ")
    new_string = input("Enter the new string to replase the old string: ")

    
    replace_text(filename, old_string, new_string)


if __name__ == "__main__":
    main()
