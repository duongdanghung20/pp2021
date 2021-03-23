students = []
students_id = []
courses = []
courses_id = []
marks = []


def input_number_of_students():
    number_of_students = int(input("Enter number of students: "))
    if number_of_students < 0:
        print("Error: number of students must be non-negative")
        return -1
    else:
        return number_of_students


def input_number_of_courses():
    number_of_courses = int(input("Enter number of courses: "))
    if number_of_courses < 0:
        print("Error: number of students must be non-negative")
        return -1
    else:
        return number_of_courses


def student(sid, name, dob):
    this_student = {
        "id": sid,
        "name": name,
        "dob": dob
    }
    students.append(this_student)
    students_id.append(sid)


def course(cid, name):
    this_course = {
        "id": cid,
        "name": name
    }
    courses.append(this_course)
    courses_id.append(cid)


def mark(sid, cid, value):
    this_mark = {
        "sid": sid,
        "cid": cid,
        "value": value
    }
    marks.append(this_mark)


def input_student_information():
    sid = input("Enter student ID: ")
    if sid in students_id:
        print("Error: Student ID existed")
    else:
        name = input("Enter student name: ")
        dob = input("Enter date of birth: ")
        student(sid, name, dob)


def input_course_information():
    cid = input("Enter course ID: ")
    if cid in courses_id:
        print("Error: Course ID existed")
    else:
        name = input("Enter course name: ")
        course(cid, name)


def input_course_mark(cid):
    for student in students:
        sid = student['id']
        value = float(input(f"- Enter mark for {student['name']}: "))
        if value < 0:
            print("Error: Mark must be non-negative")
        else:
            mark(sid, cid, value)


def input_mark():
    cid = input("Enter the course ID you want to input mark: ")
    if cid in courses_id:
        input_course_mark(cid)
    else:
        print("Error: there exist no course with that ID.")
        return -1


def list_courses():
    print("Courses existing:")
    for course in courses:
        print(f"[{course['id']}] {course['name']}")


def list_students():
    print("Students in class:")
    for student in students:
        # print(f"[{student['id']}] {student['name']}")
        print("%-20s%-20s" % (student['id'], student['name']))


def list_course_marks(cid):
    for mark in marks:
        if mark['cid'] == cid:
            sid = mark['sid']
            for student in students:
                if student['id'] == sid:
                    print(f"{student['name']}: {mark['value']}")


def list_marks():
    cid = input("Enter the course ID you want to list marks: ")
    list_course_marks(cid)


def start_engine():
    print("Initializing engine...\n")
    print("--- Student Manager ---\n")
    print("[1] Input number of student in the class")
    print("[2] Input number of courses")
    print("[3] Cancel")
    choice1 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))

    if choice1 == 1:
        number_of_students = input_number_of_students()
        print("[1] Input number of courses")
        print("[2] Cancel")
        choice2 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))



        if choice2 == 1:
            number_of_courses = input_number_of_courses()
            print("[1] Input students' information")
            print("[2] Input courses' information")
            print("[3] Cancel")
            choice3 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))


            if choice3 == 1:
                for i in range (number_of_students):
                    input_student_information()
                list_students()
                print("[1] Input courses' information")
                print("[2] Cancel")
                choice4 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))


                if choice4 == 1:
                    for i in range (number_of_courses):
                        input_course_information()
                    list_courses()
                    print("[1] Input marks for a course")
                    print("[2] List students")
                    print("[3] List courses")
                    print("[4] Cancel")


                elif choice4 == 2:
                    print("Good bye!")
                    exit()


                else:
                    print("Error: invalid choice.")
                    exit()


            elif choice3 == 2:
                for i in range (number_of_courses):
                    input_course_information()
                list_courses()


            elif choice3 == 3:
                print("Good bye!")
                exit()


        elif choice2 == 2:
            print("Good bye!")
            exit()


        else:
            print("Error: invalid choice.")
            exit()





    elif choice1 == 2:
        input_number_of_courses()
        print("[1] Input number of students")
        print("[2] Cancel")
        choice2 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
        if choice2 == 1:
            input_number_of_students()
        elif choice2 == 2:
            print("Good bye!")
            exit()

    elif choice1 == 3:
        print("Good bye!")
        exit()

    else:
        print("Error: invalid choice.")
        exit()

    list_courses()
    input_mark()
    list_marks()


start_engine()
