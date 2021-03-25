# List students to store students
students = []
# List students_id to store students id, so that we can fetch id more easily afterwards
students_id = []
# List courses to store courses
courses = []
# List courses_id to store courses id
courses_id = []
# List marks to store mark of courses and students
marks = []
marks_cid = []


def input_number_of_students():
    while True:
        number_of_students = int(input("- Enter number of students: "))
        if number_of_students < 0:
            print("Error: number of students must be non-negative")
        else:
            break
    return number_of_students


def input_number_of_courses():
    while True:
        number_of_courses = int(input("Enter number of courses: "))
        if number_of_courses < 0:
            print("Error: number of courses must be non-negative")
        else:
            break
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
    while True:
        sid = input("- Enter student ID: ")
        if len(sid) == 0 or sid is None:
            print("Error: Student ID cannot be empty")
        else:
            break
    if sid in students_id:
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
        student(sid, name, dob)


def input_course_information():
    while True:
        cid = input("- Enter course ID: ")
        if len(cid) == 0 or cid is None:
            print("Error: Course ID cannot be empty")
        else:
            break
    if cid in courses_id:
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
        course(cid, name)


def input_course_mark(cid):
    for student in students:
        sid = student['id']
        while True:
            value = float(input(f"- Enter mark for {student['name']}: "))
            if value < 0:
                print("Error: Mark must be non-negative")
            else:
                break
        mark(sid, cid, value)


def input_mark():
    while True:
        cid = input("- Enter the course ID you want to input mark: ")
        if cid in courses_id:
            if len(marks) > 0:
                existed = False
                for mark in marks:
                    if mark['cid'] == cid:
                        print("Error: You've already input mark for this course.")
                        existed = True
                        break
                if not existed:
                    input_course_mark(cid)
            else:
                input_course_mark(cid)
            break
        elif len(cid) == 0 or cid is None:
            print("Error: Course ID cannot be empty.")
        else:
            print("Error: there exist no course with that ID.")
            return -1


def list_courses():
    print("Courses existing:")
    for course in courses:
        print("\t\t[%s]   %-20s" % (course['id'], course['name']))


def list_students():
    print("Students in class:")
    for student in students:
        # print(f"[{student['id']}] {student['name']}")
        print("\t\t[%s]    %-20s%s" % (student['id'], student['name'], student['dob']))


def list_course_marks(cid):
    for mark in marks:
        if mark['cid'] == cid:
            sid = mark['sid']
            for student in students:
                if student['id'] == sid:
                    print(f"{student['name']}\t\t|\t\t{mark['value']}")


def list_marks():
    while True:
        cid = input("- Enter the course ID you want to list marks: ")
        if len(cid) == 0 or cid is None:
            print("Error: Course ID cannot be empty")
        else:
            break
    list_course_marks(cid)


def start_engine():
    print("Initializing engine...\n")
    print("--- Student Manager ---\n")
    print("\n[1] Input number of student and students information")
    print("[2] Input number of courses and courses information")
    print("[3] Cancel\n")
    choice1 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
    while True:
        if choice1 == 1:
            number_of_students = input_number_of_students()
            for i in range(number_of_students):
                print(f"Student #{i+1}:")
                input_student_information()
            while len(courses) == 0:
                print("\n[1] Input number of courses and courses information")
                print("[2] Cancel\n")
                choice2 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
                if choice2 == 1:
                    number_of_courses = input_number_of_courses()
                    for i in range(number_of_courses):
                        print(f"Course #{i + 1}:")
                        input_course_information()
                    break
                elif choice2 == 2:
                    print("Good bye!")
                    exit()
                else:
                    print("Error: Invalid choice.")
            break
        elif choice1 == 2:
            number_of_courses = input_number_of_courses()
            for i in range(number_of_courses):
                print(f"Course #{i+1}:")
                input_course_information()
            while len(students) == 0:
                print("\n[1] Input number of students and students information")
                print("[2] Cancel\n")
                choice2 = int(
                    input("Select the functionality you want to proceed (by input the corresponding number): "))
                if choice2 == 1:
                    number_of_students = input_number_of_students()
                    for i in range(number_of_students):
                        print(f"Student #{i + 1}:")
                        input_student_information()
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
    while len(marks) < len(students)*len(courses):
        print("\n[1] Input mark for a course")
        print("[2] List students")
        print("[3] List courses")
        print("[4] Cancel\n")
        choice3 = int(input("Select the functionality you want to proceed (by input the corresponding number): "))
        if choice3 == 1:
            input_mark()
        elif choice3 == 2:
            list_students()
        elif choice3 == 3:
            list_courses()
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
            list_students()
        elif choice3 == 2:
            list_courses()
        elif choice3 == 3:
            list_marks()
        elif choice3 == 4:
            print("Good bye!")
            exit()
        else:
            print("Error: invalid choice.")


start_engine()
