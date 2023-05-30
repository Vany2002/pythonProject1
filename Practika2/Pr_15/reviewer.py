from Practika2.Pr_15.mentor import Mentor
from Practika2.Pr_15.student import Student
from Practika2.Pr_15.course import Course

class Reviewer(Mentor):

    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)

    def PrintCourses(self):
        for elemement in self.GetCourses():
            print(elemement)

    def __add__(self, course: Course):
        self.AddCourse(course)

    def __sub__(self, course: Course):
        self.RemoveCourse(course)

    def __hash__(self):
        return hash((self.name, self.surname))

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}"

    def SetStudentGrade(self, student: Student, courseId: int, grade: int):
        student.SetGrade(courseId, grade)