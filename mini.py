'''
1. Display the list of available courses.
2. Allow a student to register for courses, with a maximum limit of three courses.
3. Display the courses a student has registered for.
4. Allow the student to exit the system.
Each task will be implemented using separate functions to improve code modularity and
readability.
.
'''

class course():
    def __init__(self, name, cn, creds):
        self.name = name
        self.cn = cn
        self.creds = creds

    def disp(self):
        print(f"{self.cn} - {self.name} ; credits: {self.creds}")

    def __str__(self):
        return f"{self.cn} - {self.name} ; credits: {self.creds}"

#lists courses
def list_courses(courses):
    for course in courses:
        course.disp()

#register a course from available to registered
def register(available, registered):
    if len(registered) >= 3:
        print("You are already registered for 3 courses")
        return
    
    list_courses(available)
    while True:
        try:
            course_num = int(input("Enter the course number to register: "))
            break
        except ValueError:
            print("Please type a number")
    
#Specify by specific course number 
    course = next((course for course in available if course.cn == course_num), None)
    
    if course is None:
        print("Invalid course number")
        return
        
    if course in registered:
        print("You are already registered for this course")
        return
    
    registered.append(course)
    print(f"Registered for {course.name}")


#console help statement
def help_statement():
    print('''To show help statement, type [help]
To show available courses, type [available]
To register for available courses, type [register]
To show your registered courses, type [my]
To exit console, type [exit]
''')

#console runs continuously until exited
def console(available):
    registered = []
    help_statement()
    while 1:
        user_input = str(input("Console: ")).lower()
        if "help".startswith(user_input):
            help_statement()
        elif "available".startswith(user_input):
            list(available)
        elif "register".startswith(user_input) and len(registered) < 3:
            register(available, registered)
        elif "my".startswith(user_input):
            list(registered)
        elif "exit".startswith(user_input):
            break

course_list = [course("Computing fundamentals", 2140, 4), course("Physics 2", 1155, 4), course("Seminar for Engineers", 1001, 1)]

console(course_list)
