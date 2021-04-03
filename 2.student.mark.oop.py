#!/usr/bin/python3

# Constructor to create a class representing Student and store it to students[] list
class Student:
    def __init__(self, engine, sid, name, dob):
        self.__sid = sid
        self.__name = name
        self.__dob = dob
        engine.students.append(self)
        engine.students_id.append(self.__sid)

    # return the sid of self
    def get_sid(self):
        return self.__sid

    # return the name of self
    def get_name(self):
        return self.__name

    # return the dob of self
    def get_dob(self):
        return self.__dob


# Constructor to create a class representing Course and store it to courses[] list
class Course:
    def __init__(self, engine, cid, name):
        self.__cid = cid
        self.__name = name
        engine.courses.append(self)
        engine.courses_id.append(self.__cid)

    # return the cid of self
    def get_cid(self):
        return self.__cid

    # return the name of self
    def get_name(self):
        return self.__name


# Constructor to create a class representing Mark and store it to marks[] list
class Mark:
    def __init__(self, engine, sid, cid, value):
        self.__sid = sid
        self.__cid = cid
        self.__value = value
        engine.marks.append(self)

    def get_sid(self):
        return self.__sid

    def get_cid(self):
        return self.__cid

    def get_value(self):
        return self.__value


class Engine:
    # List students to store student objects
    students = []
    # List students_id to store students id, so that we can fetch id more easily afterwards
    students_id = []
    # List courses to store course objects
    courses = []
    # List courses_id to store courses id
    courses_id = []
    # List marks to store mark objects that are the marks of courses and students
    marks = []

    number_of_students = None
    number_of_courses = None

    # Function to ask user to input number of student.
    # Print error and force the user to re-input if wrong data is given.
    def input_number_of_students(self):
        while True:
            number_of_students = int(input("- Enter number of students: "))
            if number_of_students < 0:
                print("Error: number of students must be non-negative")
            else:
                break
        self.number_of_students = number_of_students

    # Function to ask user to input number of courses.
    # Print error and force the user to re-input if wrong data is given.
    def input_number_of_courses(self):
        while True:
            number_of_courses = int(input("Enter number of courses: "))
            if number_of_courses < 0:
                print("Error: number of courses must be non-negative")
            else:
                break
        self.number_of_courses = number_of_courses

    # Function to input a student object information. Force the user to re-input if wrong data is given
    def input_student_information(self):
        while True:
            sid = input("- Enter student ID: ")
            if len(sid) == 0 or sid is None:
                print("Error: Student ID cannot be empty")
            else:
                break
        if sid in self.students_id:
            print("Error: Student ID existed")
            exit()
        else:
            while True:
                name = input("- Enter student name: ")
                if len(name) == 0 or name is None:
                    print("Error: Student name cannot be empty")
                else:
                    break
            while True:
                dob = input("- Enter student date of birth: ")
                if len(dob) == 0 or dob is None:
                    print("Error: Student date of birth cannot be empty")
                else:
                    break
            print(f"Added student: {name}")
            Student(self, sid, name, dob)

    # Function to input a course object information. Force the user to re-input if wrong data is given
    def input_course_information(self):
        while True:
            cid = input("- Enter course ID: ")
            if len(cid) == 0 or cid is None:
                print("Error: Course ID cannot be empty")
            else:
                break
        if cid in self.courses_id:
            print("Error: Course ID existed")
            exit()
        else:
            while True:
                name = input("- Enter course name: ")
                if len(name) == 0 or name is None:
                    print("Error: Course name cannot be empty")
                else:
                    break
            print(f"Added course: {name}")
            Course(self, cid, name)

    # Function to input a mark object information. Force the user to re-input if wrong data is given
    def input_course_mark(self, cid):
        for student in self.students:
            sid = student.get_sid()
            while True:
                value = float(input(f"- Enter mark for {student.get_name()}: "))
                if value < 0:
                    print("Error: Mark must be non-negative")
                else:
                    break
            Mark(self, sid, cid, value)

    # Ask the user for the course ID whose mark should be input, then invoke the input_course_mark() function
    def input_mark(self):
        while True:
            cid = input("- Enter the course ID you want to input mark: ")
            if cid in self.courses_id:
                if len(self.marks) > 0:
                    existed = False
                    for mark in self.marks:
                        if mark.get_cid() == cid:
                            print("Error: You've already input mark for this course.")
                            existed = True
                            break
                    if not existed:
                        self.input_course_mark(cid)
                else:
                    self.input_course_mark(cid)
                break
            elif len(cid) == 0 or cid is None:
                print("Error: Course ID cannot be empty.")
            else:
                print("Error: There exist no course with that ID.")
                return -1

    # List all the courses
    def list_courses(self):
        print("Courses existing:")
        for course in self.courses:
            print("\t\t[%s]   %-20s" % (course.get_cid(), course.get_name()))

    # List all the students
    def list_students(self):
        print("Students in class:")
        for student in self.students:
            # print(f"[{student['id']}] {student['name']}")
            print("\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(), student.get_dob()))

    # List all students with their marks for a specific course
    def list_course_marks(self, cid):
        for mark in self.marks:
            if mark.get_cid() == cid:
                sid = mark.get_sid()
                for student in self.students:
                    if student.get_sid() == sid:
                        print(f"\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(), mark.get_value()))

    # Ask the user for the course ID whose mark should be listed, then invoke the list_course_marks() function
    def list_marks(self):
        while True:
            cid = input("- Enter the course ID you want to list marks: ")
            if len(cid) == 0 or cid is None:
                print("Error: Course ID cannot be empty")
            else:
                break
        if cid in self.courses_id:
            self.list_course_marks(cid)
        else:
            print("Error: There exist no course with that ID.")
            return -1

    # A method to start the program
    def start_engine(self):
        print("Initializing engine...\n")
        print("--- Student Manager ---\n")
        print("\n[1] Input number of student and students information")
        print("[2] Input number of courses and courses information")
        print("[3] Cancel\n")
        choice1 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
        while True:
            if choice1 == 1:
                self.input_number_of_students()
                for i in range(self.number_of_students):
                    print(f"Student #{i + 1}:")
                    self.input_student_information()
                while len(self.courses) == 0:
                    print("\n[1] Input number of courses and courses information")
                    print("[2] Cancel\n")
                    choice2 = int(
                        input("Select the functionality you want to proceed (by input the corresponding number): "))
                    if choice2 == 1:
                        self.input_number_of_courses()
                        for i in range(self.number_of_courses):
                            print(f"Course #{i + 1}:")
                            self.input_course_information()
                        break
                    elif choice2 == 2:
                        print("Good bye!")
                        exit()
                    else:
                        print("Error: Invalid choice.")
                break
            elif choice1 == 2:
                self.input_number_of_courses()
                for i in range(self.number_of_courses):
                    print(f"Course #{i + 1}:")
                    self.input_course_information()
                while len(self.students) == 0:
                    print("\n[1] Input number of students and students information")
                    print("[2] Cancel\n")
                    choice2 = int(
                        input("Select the functionality you want to proceed (by input the corresponding number): "))
                    if choice2 == 1:
                        self.input_number_of_students()
                        for i in range(self.number_of_students):
                            print(f"Student #{i + 1}:")
                            self.input_student_information()
                        break
                    elif choice2 == 2:
                        print("Good bye!")
                        exit()
                    else:
                        print("Error: Invalid choice.")
                        break
                break
            elif choice1 == 3:
                print("Good bye!")
                exit()
            else:
                print("Error: Invalid choice.\n")
                exit()
        while len(self.marks) < len(self.students) * len(self.courses):
            print("\n[1] Input mark for a course")
            print("[2] List students")
            print("[3] List courses")
            print("[4] Cancel\n")
            choice3 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
            if choice3 == 1:
                self.input_mark()
            elif choice3 == 2:
                self.list_students()
            elif choice3 == 3:
                self.list_courses()
            elif choice3 == 4:
                print("Good bye!")
                exit()
            else:
                print("Error: invalid choice.")
        while True:
            print("\n[1] List students")
            print("[2] List courses")
            print("[3] Show marks of a course")
            print("[4] Cancel\n")
            choice3 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
            if choice3 == 1:
                self.list_students()
            elif choice3 == 2:
                self.list_courses()
            elif choice3 == 3:
                self.list_marks()
            elif choice3 == 4:
                print("Good bye!")
                exit()
            else:
                print("Error: invalid choice.")


if __name__ == '__main__':
    e = Engine()
    e.start_engine()
