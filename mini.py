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
        user_input = str(input("Console: ")).lower()
        if "help".startswith(user_input):
            print('''help - show this statement
available - show available courses
register - register for an available course
my - show your courses
exit - exit console
''')
        elif "available".startswith(user_input):
            list(available)
        elif "register".startswith(user_input) and len(registered) < 3:
            list(available)
            while 1:
                try:
                    course_num = int(input("Course number: "))
                    break
                except:
                    print("Please type a number")
        elif "my".startswith(user_input):
            list(registered)
        elif "exit".startswith(user_input):
            break

course_list = []

console(course_list)
