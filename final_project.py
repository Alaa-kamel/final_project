import uuid

# TODO 1 Enter your name and submission date
#Name :alaa
#Delivery Date :26_6_2023

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = str(uuid.uuid4())
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    total_students = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = str(uuid.uuid4())
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_students += 1

    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course ID: {course.course_id}")
            print(f"Course Name: {course.course_name}")
            print(f"Course Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list) if self.courses_list else 0.0


students = []

while True:
    try:
        selection = int(input("1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4. Get Student Average\n"
                              "5. Add Course to Student with Mark\n"
                              "6. Exit\n"))

        if selection == 1:
            student_number = input("Enter Student Number: ")
            if any(student.student_number == student_number for student in students):
                print("Student Number already exists.")
                continue

            student_name = input("Enter Student Name: ")
            while True:
                try:
                    student_age = int(input("Enter Student Age: "))
                    break
                except ValueError:
                    print("Invalid Value")

            student = Student(student_name, student_age, student_number)
            students.append(student)
            print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number: ")
            found_student = None
            for student in students:
                if student.student_number == student_number:
                    found_student = student
                    break

            if found_student:
                students.remove(found_student)
                print("Student Deleted Successfully")
            else:
                print("Student Not Exist")

        elif selection == 3:
            student_number = input("Enter Student Number: ")
            found_student = None
            for student in students:
                if student.student_number == student_number:
                    found_student = student
                    break

            if found_student:
                print("Student Details:")
                print(found_student.get_student_details())
            else:
                print("Student Not Exist")

        elif selection == 4:
            student_number = input("Enter Student Number: ")
            found_student = None
            for student in students:
                if student.student_number == student_number:
                    found_student = student
                    break

            if found_student:
                average = found_student.get_student_average()
                print(f"Student Average: {average}")
            else:
                print("Student Not Exist")

        elif selection == 5:
            student_number = input("Enter Student Number: ")
            found_student = None
            for student in students:
                if student.student_number == student_number:
                    found_student = student
                    break

            if found_student:
                course_name = input("Enter Course Name: ")
                while True:
                    try:
                        course_mark = float(input("Enter Course Mark: "))
                        break
                    except ValueError:
                        print("Invalid Value")

                found_student.enroll_course(course_name, course_mark)
                print("Course Added Successfully")
            else:
                print("Student Not Exist")

        elif selection == 6:
            break

        else:
            print("Invalid selection. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")
