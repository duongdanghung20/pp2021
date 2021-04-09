#!/usr/bin/python3


import math
import numpy as np
import curses


# A class representing Student
class Student:
    # A constructor to create a Student object and store it to students[] list
    def __init__(self, engine, sid, name, dob, gpa=0):
        self.__sid = sid
        self.__name = name
        self.__dob = dob
        self.__gpa = gpa
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

    # set the gpa of self
    def set_gpa(self, gpa):
        self.__gpa = gpa

    # return the gpa of self
    def get_gpa(self):
        return self.__gpa


# A class representing Course
class Course:
    # A constructor to create a Student object and store it to courses[] list
    def __init__(self, engine, cid, name, credit):
        self.__cid = cid
        self.__name = name
        self.__credit = credit
        engine.courses.append(self)
        engine.courses_id.append(self.__cid)

    # return the cid of self
    def get_cid(self):
        return self.__cid

    # return the name of self
    def get_name(self):
        return self.__name

    # return the number of credits of self
    def get_credit(self):
        return self.__credit


# A class representing Course
class Mark:
    # A constructor to create a Mark object and store it to marks[] list
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


# Define a method to print error
def print_error(error):
    screen.addstr("\nError: " + error + ".", curses.color_pair(1) |
                  curses.A_BOLD | curses.A_UNDERLINE | curses.A_BLINK)
    screen.refresh()
    curses.napms(3000)
    screen.clear()
    screen.refresh()


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
            # number_of_students = int(input("- Enter number of students: "))
            screen.addstr("- Enter number of students: ")
            screen.refresh()
            number_of_students = int(screen.getstr().decode())
            if number_of_students < 0:
                # print("Error: number of students must be non-negative")
                print_error("number of students must be non-negative")
            else:
                break
        self.number_of_students = number_of_students

    # Function to ask user to input number of courses.
    # Print error and force the user to re-input if wrong data is given.
    def input_number_of_courses(self):
        while True:
            # number_of_courses = int(input("- Enter number of courses: "))
            screen.addstr("- Enter number of courses: ")
            screen.refresh()
            number_of_courses = int(screen.getstr().decode())
            if number_of_courses < 0:
                # print("Error: number of courses must be non-negative")
                print_error("number of courses must be non-negative")
            else:
                break
        self.number_of_courses = number_of_courses

    # Function to input a student object information. Force the user to re-input if wrong data is given
    def input_student_information(self):
        while True:
            # sid = input("- Enter student ID: ")
            screen.addstr("- Enter student ID: ")
            screen.refresh()
            sid = screen.getstr().decode()
            if len(sid) == 0 or sid is None:
                # print("Error: Student ID cannot be empty")
                print_error("Student ID cannot be empty")
            else:
                break
        if sid in self.students_id:
            # print("Error: Student ID existed")
            print_error("Student ID existed")
            curses.endwin()
            exit()
        else:
            while True:
                # name = input("- Enter student name: ")
                screen.addstr("- Enter student name: ")
                screen.refresh()
                name = screen.getstr().decode()
                if len(name) == 0 or name is None:
                    # print("Error: Student name cannot be empty")
                    print_error("Student name cannot be empty")
                else:
                    break
            while True:
                # dob = input("- Enter student date of birth: ")
                screen.addstr("- Enter student date of birth: ")
                screen.refresh()
                dob = screen.getstr().decode()
                if len(dob) == 0 or dob is None:
                    # print("Error: Student date of birth cannot be empty")
                    print_error("Student date of birth cannot be empty")
                else:
                    break
            screen.addstr(f"\nAdded student: {name}")
            Student(self, sid, name, dob)

    # Function to input a course object information. Force the user to re-input if wrong data is given
    def input_course_information(self):
        while True:
            # cid = input("- Enter course ID: ")
            screen.addstr("- Enter course ID: ")
            screen.refresh()
            cid = screen.getstr().decode()
            if len(cid) == 0 or cid is None:
                # print("Error: Course ID cannot be empty")
                print_error("Course ID cannot be empty")
            else:
                break
        if cid in self.courses_id:
            # print("Error: Course ID existed")
            print_error("Course ID existed")
            curses.endwin()
            exit()
        else:
            while True:
                # name = input("- Enter course name: ")
                screen.addstr("- Enter course name: ")
                screen.refresh()
                name = screen.getstr().decode()
                if len(name) == 0 or name is None:
                    # print("Error: Course name cannot be empty")
                    print_error("Course name cannot be empty")
                else:
                    break
            while True:
                # credit = int(input("- Enter course credits: "))
                screen.addstr("- Enter course credits: ")
                screen.refresh()
                credit = int(screen.getstr().decode())
                if credit < 0:
                    # print("Error: Course credit must be non-negative")
                    print_error("Course credit must be non-negative")
                elif credit is None:
                    # print("Error: Course credit cannot be empty")
                    print_error("Course credit cannot be empty")
                else:
                    break
            screen.addstr(f"Added course: {name}")
            Course(self, cid, name, credit)

    # Function to input a mark object information. Force the user to re-input if wrong data is given
    def input_course_mark(self, cid):
        for student in self.students:
            sid = student.get_sid()
            while True:
                # value = float(input(f"- Enter mark for {student.get_name()}: "))
                screen.addstr(f"- Enter mark for {student.get_name()}: ")
                screen.refresh()
                value = float(screen.getstr().decode())
                value = math.floor(value * 10) / 10.0
                if value < 0:
                    # print("Error: Mark must be non-negative")
                    print_error("Mark must me non-negative")
                else:
                    break
            Mark(self, sid, cid, value)

    # Ask the user for the course ID whose mark should be input, then invoke the input_course_mark() function
    def input_mark(self):
        while True:
            # cid = input("- Enter the course ID you want to input mark: ")
            screen.addstr("- Enter the course ID you want to input mark: ")
            screen.refresh()
            cid = screen.getstr().decode()
            screen.clear()
            screen.refresh()
            if cid in self.courses_id:
                if len(self.marks) > 0:
                    existed = False
                    for mark in self.marks:
                        if mark.get_cid() == cid:
                            # print("Error: You've already input mark for this course.")
                            print_error("You've already input mark for this course")
                            existed = True
                            break
                    if not existed:
                        self.input_course_mark(cid)
                else:
                    self.input_course_mark(cid)
                break
            elif len(cid) == 0 or cid is None:
                # print("Error: Course ID cannot be empty.")
                print_error("Course ID cannot be empty")
            else:
                # print("Error: There exist no course with that ID.")
                print_error("There exist no course with that ID")
                return -1

    # List all the courses
    def list_courses(self):
        # print("Courses existing:")
        screen.addstr("Courses existing:")
        screen.refresh()
        for course in self.courses:
            # print("\t\t[%s]   %-20s%d credits" % (course.get_cid(), course.get_name(), course.get_credit()))
            screen.addstr("\n\t\t[%s]   %-20s%d credits" % (course.get_cid(), course.get_name(), course.get_credit()))
            screen.refresh()

    # List all the students
    def list_students(self):
        # print("Students in class:")
        screen.addstr("Students in class:")
        screen.refresh()
        for student in self.students:
            # print("\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(), student.get_dob()))
            screen.addstr("\n\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(), student.get_dob()))
            screen.refresh()

    # List all students with their marks for a specific course
    def list_course_marks(self, cid):
        for mark in self.marks:
            if mark.get_cid() == cid:
                sid = mark.get_sid()
                for student in self.students:
                    if student.get_sid() == sid:
                        screen.addstr(f"\n\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(),
                                                                  mark.get_value()))
                        screen.refresh()

    # Ask the user for the course ID whose mark should be listed, then invoke the list_course_marks() function
    def list_marks(self):
        while True:
            # cid = input("- Enter the course ID you want to list marks: ")
            screen.addstr("- Enter the course ID you want to list marks: ")
            screen.refresh()
            cid = screen.getstr().decode()
            if len(cid) == 0 or cid is None:
                # print("Error: Course ID cannot be empty")
                print_error("Course ID cannot be empty")
            else:
                break
        if cid in self.courses_id:
            curses.curs_set(0)
            self.list_course_marks(cid)
        else:
            # print("Error: There exist no course with that ID.")
            print_error("There exist no course with that ID")
            return -1

    # A function to calculate average GPA for a specific student
    def calculate_student_gpa(self, sid):
        mark_values = np.array([])
        course_credits = np.array([])
        for mark in self.marks:
            if mark.get_sid() == sid:
                for course in self.courses:
                    if course.get_cid() == mark.get_cid():
                        mark_values = np.append(mark_values, mark.get_value())
                        course_credits = np.append(course_credits, course.get_credit())
        gpa = np.dot(mark_values, course_credits) / np.sum(course_credits)
        rounded_gpa = math.floor(gpa * 10) / 10.0
        # Add the value of attribute gpa for the student with ID specified
        for student in self.students:
            if student.get_sid() == sid:
                student.set_gpa(rounded_gpa)

    # Ask the user for the student ID whose GPA should be calculated, then invoke the calculate_student_gpa() function
    def calculate_gpa(self):
        while True:
            # sid = input("- Enter student ID that requires GPA calculating: ")
            screen.addstr("- Enter student ID that requires GPA calculating: ")
            screen.refresh()
            sid = screen.getstr().decode()
            if len(sid) == 0 or sid is None:
                # print("Error: Student ID cannot be empty")
                print_error("Student ID cannot be empty")
            elif sid not in self.students_id:
                # print("Error: Student does not exist")
                print_error("Student does not exist")
            else:
                break
        for student in self.students:
            if student.get_sid() == sid:
                self.calculate_student_gpa(sid)
                curses.curs_set(0)
                screen.addstr("\n\t\t%s's GPA:    %-20.1f" % (student.get_name(), student.get_gpa()))
                screen.refresh()
                break

    # A function to print a sorted student list by GPA descending
    def print_sorted_list(self):
        # Automatically calculate GPA for all students before printing a sorted list
        new_student_list = []
        for student in self.students:
            self.calculate_student_gpa(student.get_sid())
            new_student = (student.get_sid(), student.get_name(), student.get_gpa())
            new_student_list.append(new_student)
        # Make a copy of the student list using type numpy.array
        np_student_list = np.array(new_student_list)
        # Sort the student list in ascending order and then reverse it
        sorted_student_list = np.sort(np_student_list)[::-1]
        for student in sorted_student_list:
            screen.addstr("\t\t[%s]    %-20sGPA: %s\n" % (student[1], student[2], student[0]))
            screen.refresh()

    # A method to start the program
    def start_engine(self):

        # print("Initializing engine...\n")
        # print("--- Student Manager ---\n")

        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        num_rows, num_cols = screen.getmaxyx()

        # Make a function to print a line in the center of screen
        def print_center(message):
            # Calculate center row
            middle_row = int(num_rows / 2)

            # Calculate center column, and then adjust starting position based
            # on the length of the message
            half_length_of_message = int(len(message) / 2)
            middle_column = int(num_cols / 2)
            x_position = middle_column - half_length_of_message

            # Draw the text
            if message == "--- Student Manager ---":
                screen.addstr(middle_row, x_position, message, curses.A_BOLD)
                screen.refresh()
            else:
                screen.addstr(middle_row, x_position, message)
                screen.refresh()

        curses.curs_set(0)
        screen.refresh()
        print_center("Initializing engine")
        curses.napms(500)
        for i in range(3):
            screen.addstr(".")
            screen.refresh()
            curses.napms(500)
        screen.clear()
        screen.refresh()
        curses.napms(500)
        print_center("--- Student Manager ---")
        screen.refresh()
        curses.napms(2000)
        screen.clear()
        screen.refresh()

        # print("\n[1] Input number of student and students information")
        # print("[2] Input number of courses and courses information")
        # print("[3] Cancel\n")

        curses.curs_set(1)
        screen.addstr("[1] Input number of student and students information")
        screen.addstr("\n[2] Input number of courses and courses information")
        screen.addstr("\n[3] Cancel\n")

        # choice1 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
        screen.addstr("Select the functionality you want to proceed (by input the corresponding number): ")
        screen.refresh()
        choice1 = int(screen.getstr().decode())
        while True:
            if choice1 == 1:
                screen.clear()
                screen.refresh()
                self.input_number_of_students()
                screen.clear()
                screen.refresh()
                for i in range(self.number_of_students):
                    # print(f"Student #{i + 1}:")
                    screen.addstr(f"Student #{i + 1}:\n")
                    screen.refresh()
                    self.input_student_information()
                    screen.clear()
                    screen.refresh()
                while len(self.courses) == 0:
                    screen.addstr("[1] Input number of courses and courses information")
                    screen.addstr("\n[2] Cancel\n")
                    screen.refresh()
                    # choice2 = int(
                    #     input("Select the functionality you want to proceed (by input the corresponding number): "))
                    screen.addstr("Select the functionality you want to proceed (by input the corresponding number): ")
                    screen.refresh()
                    choice2 = int(screen.getstr().decode())
                    if choice2 == 1:
                        screen.clear()
                        screen.refresh()
                        self.input_number_of_courses()
                        screen.clear()
                        screen.refresh()
                        for i in range(self.number_of_courses):
                            # print(f"Course #{i + 1}:")
                            screen.addstr(f"Course #{i + 1}:\n")
                            screen.refresh()
                            self.input_course_information()
                            screen.clear()
                            screen.refresh()
                        break
                    elif choice2 == 2:
                        # print("Good bye!")
                        screen.addstr("Good bye!")
                        screen.refresh()
                        curses.napms(1000)
                        curses.endwin()
                        exit()
                    else:
                        # print("Error: Invalid choice.")
                        print_error("Invalid choice")
                break
            elif choice1 == 2:
                screen.clear()
                screen.refresh()
                self.input_number_of_courses()
                screen.clear()
                screen.refresh()
                for i in range(self.number_of_courses):
                    # print(f"Course #{i + 1}:")
                    screen.addstr(f"Course #{i + 1}:\n")
                    screen.refresh()
                    self.input_course_information()
                    screen.clear()
                    screen.refresh()
                while len(self.students) == 0:
                    screen.addstr("[1] Input number of students and students information")
                    screen.addstr("\n[2] Cancel\n")
                    screen.refresh()
                    # choice2 = int(
                    #     input("Select the functionality you want to proceed (by input the corresponding number): "))
                    screen.addstr("Select the functionality you want to proceed (by input the corresponding number): ")
                    screen.refresh()
                    choice2 = int(screen.getstr().decode())
                    if choice2 == 1:
                        screen.clear()
                        screen.refresh()
                        self.input_number_of_students()
                        screen.clear()
                        screen.refresh()
                        for i in range(self.number_of_students):
                            # print(f"Student #{i + 1}:")
                            screen.addstr(f"Student #{i + 1}:\n")
                            screen.refresh()
                            self.input_student_information()
                            screen.clear()
                            screen.refresh()
                        break
                    elif choice2 == 2:
                        # print("Good bye!")
                        screen.addstr("Good bye!")
                        screen.refresh()
                        curses.napms(1000)
                        curses.endwin()
                        exit()
                    else:
                        # print("Error: Invalid choice.")
                        print_error("Invalid choice")
                        break
                break
            elif choice1 == 3:
                # print("Good bye!")
                screen.addstr("Good bye!")
                screen.refresh()
                curses.napms(1000)
                curses.endwin()
                exit()
            else:
                # print("Error: Invalid choice.\n")
                print_error("Invalid choice")
                curses.endwin()
                exit()
        while len(self.marks) < len(self.students) * len(self.courses):
            screen.clear()
            screen.refresh()
            screen.addstr("[1] Input mark for a course")
            screen.addstr("\n[2] List students")
            screen.addstr("\n[3] List courses")
            screen.addstr("\n[4] Cancel\n")
            # choice3 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
            screen.addstr("Select the functionality you want to proceed (by input the corresponding number): ")
            screen.refresh()
            choice3 = int(screen.getstr().decode())
            screen.clear()
            screen.refresh()
            if choice3 == 1:
                self.input_mark()
            elif choice3 == 2:
                curses.curs_set(0)
                self.list_students()
                curses.napms(self.number_of_students * 1000)
                curses.curs_set(1)
            elif choice3 == 3:
                curses.curs_set(0)
                self.list_courses()
                curses.napms(self.number_of_courses * 1000)
                curses.curs_set(1)
            elif choice3 == 4:
                # print("Good bye!")
                screen.addstr("Good bye!")
                screen.refresh()
                curses.napms(1000)
                curses.endwin()
                exit()
            else:
                # print("Error: invalid choice.")
                print_error("Invalid choice")
        while True:
            screen.clear()
            screen.refresh()
            screen.addstr("[1] List students")
            screen.addstr("\n[2] List courses")
            screen.addstr("\n[3] Show marks of a course")
            screen.addstr("\n[4] Calculate GPA for a student")
            screen.addstr("\n[5] Print a sorted student list by GPA descending")
            screen.addstr("\n[6] Cancel\n")
            # choice4 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
            screen.addstr("Select the functionality you want to proceed (by input the corresponding number): ")
            screen.refresh()
            choice4 = int(screen.getstr().decode())
            screen.clear()
            screen.refresh()
            if choice4 == 1:
                curses.curs_set(0)
                self.list_students()
                curses.napms(self.number_of_students * 1000)
                curses.curs_set(1)
            elif choice4 == 2:
                curses.curs_set(0)
                self.list_courses()
                curses.napms(self.number_of_courses * 1000)
                curses.curs_set(1)
            elif choice4 == 3:
                self.list_marks()
                curses.napms(self.number_of_students * 1000)
                curses.curs_set(1)
            elif choice4 == 4:
                self.calculate_gpa()
                curses.napms(1000)
                curses.curs_set(1)
            elif choice4 == 5:
                curses.curs_set(0)
                self.print_sorted_list()
                curses.napms(self.number_of_students * 1000)
                curses.curs_set(1)
            elif choice4 == 6:
                # print("Good bye!")
                screen.addstr("Good bye!")
                screen.refresh()
                curses.napms(1000)
                curses.endwin()
                exit()
            else:
                # print("Error: invalid choice.")
                print_error("Invalid choice")


if __name__ == '__main__':
    screen = curses.initscr()
    e = Engine()
    e.start_engine()
