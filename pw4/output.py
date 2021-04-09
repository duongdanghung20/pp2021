# import main
import curses
import numpy as np
import math


# Define a method to print error
def print_error(error):
    screen.addstr("\nError: " + error + ".", curses.color_pair(1) |
                  curses.A_BOLD | curses.A_UNDERLINE | curses.A_BLINK)
    screen.refresh()
    curses.napms(3000)
    screen.clear()
    screen.refresh()


class Output:
    def __init__(self, scr):
        self.__screen = scr

    # List all the courses
    def list_courses(self, engine):
        # print("Courses existing:")
        self.__screen.addstr("Courses existing:")
        self.__screen.refresh()
        for course in engine.courses:
            # print("\t\t[%s]   %-20s%d credits" % (course.get_cid(), course.get_name(), course.get_credit()))
            self.__screen.addstr(
                "\n\t\t[%s]   %-20s%d credits" % (course.get_cid(), course.get_name(), course.get_credit()))
            self.__screen.refresh()

    # List all the students
    def list_students(self, engine):
        # print("Students in class:")
        self.__screen.addstr("Students in class:")
        self.__screen.refresh()
        for student in engine.students:
            # print("\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(), student.get_dob()))
            self.__screen.addstr("\n\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(), student.get_dob()))
            self.__screen.refresh()

    # List all students with their marks for a specific course
    def list_course_marks(self, engine, cid):
        for mark in engine.marks:
            if mark.get_cid() == cid:
                sid = mark.get_sid()
                for student in engine.students:
                    if student.get_sid() == sid:
                        self.__screen.addstr(f"\n\t\t[%s]    %-20s%s" % (student.get_sid(), student.get_name(),
                                                                         mark.get_value()))
                        self.__screen.refresh()

    # Ask the user for the course ID whose mark should be listed, then invoke the list_course_marks() function
    def list_marks(self, engine):
        while True:
            # cid = input("- Enter the course ID you want to list marks: ")
            self.__screen.addstr("- Enter the course ID you want to list marks: ")
            self.__screen.refresh()
            cid = self.__screen.getstr().decode()
            if len(cid) == 0 or cid is None:
                # print("Error: Course ID cannot be empty")
                print_error("Course ID cannot be empty")
            else:
                break
        if cid in engine.courses_id:
            curses.curs_set(0)
            self.list_course_marks(engine, cid)
        else:
            # print("Error: There exist no course with that ID.")
            print_error("There exist no course with that ID")
            return -1

    # A function to calculate average GPA for a specific student
    def calculate_student_gpa(self, engine, sid):
        mark_values = np.array([])
        course_credits = np.array([])
        for mark in engine.marks:
            if mark.get_sid() == sid:
                for course in engine.courses:
                    if course.get_cid() == mark.get_cid():
                        mark_values = np.append(mark_values, mark.get_value())
                        course_credits = np.append(course_credits, course.get_credit())
        gpa = np.dot(mark_values, course_credits) / np.sum(course_credits)
        rounded_gpa = math.floor(gpa * 10) / 10.0
        # Add the value of attribute gpa for the student with ID specified
        for student in engine.students:
            if student.get_sid() == sid:
                student.set_gpa(rounded_gpa)

    # Ask the user for the student ID whose GPA should be calculated, then invoke the calculate_student_gpa() function
    def calculate_gpa(self, engine):
        while True:
            # sid = input("- Enter student ID that requires GPA calculating: ")
            self.__screen.addstr("- Enter student ID that requires GPA calculating: ")
            self.__screen.refresh()
            sid = self.__screen.getstr().decode()
            if len(sid) == 0 or sid is None:
                # print("Error: Student ID cannot be empty")
                print_error("Student ID cannot be empty")
            elif sid not in engine.students_id:
                # print("Error: Student does not exist")
                print_error("Student does not exist")
            else:
                break
        for student in engine.students:
            if student.get_sid() == sid:
                self.calculate_student_gpa(engine, sid)
                curses.curs_set(0)
                self.__screen.addstr("\n\t\t%s's GPA:    %-20.1f" % (student.get_name(), student.get_gpa()))
                self.__screen.refresh()
                break

    # A function to print a sorted student list by GPA descending
    def print_sorted_list(self, engine):
        # Automatically calculate GPA for all students before printing a sorted list
        new_student_list = []
        for student in engine.students:
            self.calculate_student_gpa(engine, student.get_sid())
            new_student = (student.get_sid(), student.get_name(), student.get_gpa())
            new_student_list.append(new_student)
        # Make a copy of the student list using type numpy.array
        np_student_list = np.array(new_student_list)
        # Sort the student list in ascending order and then reverse it
        sorted_student_list = np.sort(np_student_list)[::-1]
        for student in sorted_student_list:
            self.__screen.addstr("\t\t[%s]    %-20sGPA: %s\n" % (student[1], student[2], student[0]))
            self.__screen.refresh()
