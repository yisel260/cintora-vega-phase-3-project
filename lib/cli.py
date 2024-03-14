from helpers import (
    exit_program,
    get_student_data
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_student_data()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. I want to see student information")
    print("2. I want to add a student")
    print("3. I want to remove a student")
    print("4. I want to explore student groups")
   

if __name__ == "__main__":
    main()