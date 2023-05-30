from Practika2.Pr_15.lecturer import Lecturer
from Practika2.Pr_15.reviewer import Reviewer
from Practika2.Pr_15.student import Student
from Practika2.Pr_15.course import Course
import statistics
def Flatten(list):
    return [item for sublist in list for item in sublist]


def CalcAvgGrade(gradeables, courseId: int):
    return statistics.mean(Flatten(map(lambda gradeable: gradeable(courseId), gradeables)))


# Courses
pythonCourse1 = Course(1, "Python")
pythonCourse2 = Course(1, "Python")
pythonCourse3 = Course(1, "Python")
csharpCourse = Course(2, "C#")
cppCourse = Course(3, "C++")

# Lecturers
lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.AddCourse(pythonCourse1)
pythonCourse1.SetLecturer(lecturer1)

lecturer2 = Lecturer('Ivan', 'Razin')
lecturer2.AddCourse(pythonCourse2)
pythonCourse2.SetLecturer(lecturer2)

lecturer3 = Lecturer('Denis', 'Pavlov')
lecturer3.AddCourse(pythonCourse3)
pythonCourse3.SetLecturer(lecturer3)

# Students
student1 = Student("Alex", "Petrov")

student1.AddCourse(pythonCourse1)
student1.AddCourse(pythonCourse2)
student1.AddCourse(pythonCourse3)
student1.AddCourse(csharpCourse)
student1.AddCourse(cppCourse)

student1.StartCourse(pythonCourse1.GetId())
student1.StartCourse(csharpCourse.GetId())
student1.FinishCourse(cppCourse.GetId())

student2 = Student("Dima", "Ivanov")
student2.AddCourse(pythonCourse1)
student2.StartCourse(pythonCourse1.GetId())

reviewer = Reviewer('Viktor', 'Kuznecov')
reviewer + pythonCourse1
reviewer.SetStudentGrade(student1, pythonCourse1.GetId(), 9)
reviewer.SetStudentGrade(student2, pythonCourse1.GetId(), 5)
reviewer + csharpCourse

students = [student1, student2]

print(f"Average homework grades for students within a course in {pythonCourse1.GetTitle()} {pythonCourse1.GetId()}: ",
      CalcAvgGrade(students, pythonCourse1.GetId()))

student1.RateLecturer(pythonCourse1.GetId(), 3)
student2.RateLecturer(pythonCourse1.GetId(), 7)

lecturers = [lecturer1, lecturer2, lecturer3]

print(f"The average mark for the lectures of the lecturers within the framework of the course on {pythonCourse1.GetTitle()}: ",
      CalcAvgGrade(lecturers, pythonCourse1.GetId()))

print("\nThe first student is smarter than the second" if (student1 > student2)
      else "\nThe second student is smarter than the first")

print(f"\nReviewer:\n{reviewer}")
print(f"\nLecturer1:\n{lecturer1}")
print(f"\nStudent1:\n{student1}\n")

print(f"Lecturer grades by courses: {lecturer1.GetGrades()}")
print(f"Student grades by courses: {student1.GetGrades()}")
