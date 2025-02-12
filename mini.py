'''
1. Display the list of available courses.
2. Allow a student to register for courses, with a maximum limit of three courses.
3. Display the courses a student has registered for.
4. Allow the student to exit the system.
Each task will be implemented using separate functions to improve code modularity and
readability.
.
'''

def list(courses):
    for i in range(len(courses)):
        print(str(i) + ": " + courses[i]);
    print("")

def register(l):
    pass


def console(available):
    registered = ["one course"]
    while 1:
        user_input = str(input("Console: "))
        if user_input in "help":
            print("heres some helpful information")
        elif user_input in "available":
            list(available)
        elif user_input in "register" and len(registered) < 3:
            list(available)
            while 1:
                try:
                    course_num = int(input("Course number: "))
                    break
                except:
                    print("Please type a number")
        elif user_input in "my":
            list(registered)
        elif user_input in "exit":
            break

course_list = []

console(course_list)
