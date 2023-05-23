from Practika2.Pr_15.Pr_15_Task_1 import Lecturer, Reviewer, Student

course1 = 'Russian'
course2 = 'Psychology'


reviewer1 = Reviewer('Anton', 'Alex')
reviewer2 = Reviewer('Lida', 'Viktor')

lecturer1 = Lecturer('Marina', 'Dasha')
lecturer2 = Lecturer('Dima', 'Kirill')

student1 = Student('Misha', 'Ivan')
student2 = Student('Peter', 'Bob')

student1.add_course(course1)
student2.add_course(course2)
lecturer1.add_course(course1)
lecturer2.add_course(course2)


student1.rate_lecture(lecturer1, course1, 4)
student1.rate_lecture(lecturer2, course2, 5)
student2.rate_lecture(lecturer1, course2, 4)
student2.rate_lecture(lecturer2, course1, 3)

student1.add_course(course2)
student1.add_course(course1)
student2.add_course(course2)
student2.add_course(course1)
student1.grades = {course2: [5, 4], course1: [4]}
student2.grades = {course2: [4, 3], course1: [5]}

print(reviewer1)
print(reviewer2)

print(lecturer1)
print(lecturer2)

print(student1)
print(student2)


def avg_grade_hw(students_list, course_name):
    grades = []
    for student in students_list:
        if course_name in student.grades:
            grades.extend(student.grades[course_name])
    if grades:
        return sum(grades) / len(grades)
    else:
        return 0


print(avg_grade_hw([student1, student2], course2))
print(avg_grade_hw([student1, student2], course1))


def avg_grade_lecturers(lecturers_list, course_name):
    grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.courses:
            grades.extend(lecturer.grades)
    if len(grades) != 0:
        return sum(grades) / len(grades)
    else:
        return 0
