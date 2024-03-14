def exit_program():
    print("Goodbye!")
    exit()

def get_student_data():
        pick_a_class()
        choice = input("> ")
        print(choice)
        print("I am printing all the data on the student using a get request that includes choice as class so that user only get students in that class")

def pick_a_class():
    print("Please choose a class :")
    print("list of classes")
