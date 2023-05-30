from Practika2.Pr_15.course import Course
from enum import Enum
import statistics


class CourseProgess(Enum):
    NotStarted = 0
    Finished = 1
    InProgess = 2


class CourseState:
    def __init__(self, course: Course):
        self.course = course
        self.progress = CourseProgess.NotStarted

    def GetProgress(self):
        return self.progress

    def StartCourse(self):
        self.courseProgess = CourseProgess.InProgess

    def FinishCourse(self):
        self.courseProgess = CourseProgess.Finished

    def GetCourse(self) -> Course:
        return self.course


class Student:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses: dict[int, CourseState] = {}
        self.grades = {}

    def AddCourse(self, course: Course):
        self.courses[course.GetId()] = CourseState(course)

    def StartCourse(self, courseId: int):
        self.courses[courseId].StartCourse()

    def FinishCourse(self, courseId: int):
        self.courses[courseId].FinishCourse()

    def SetGrade(self, courseId: int, grade: int):
        self.grades[courseId] = grade

    def RateLecturer(self, courseId: int, grade: int):
        self.courses[courseId].GetCourse(
        ).GetLecturer().AddGrade(courseId, grade)

    def GetName(self) -> str:
        return self.name

    def GetSurname(self) -> str:
        return self.surname

    def GetFinishedCourses(self) -> list[CourseState]:
        return list(filter(lambda c: c.GetProgress() == CourseProgess.Finished, self.courses))

    def GetCoursesInProgress(self) -> list[CourseState]:
        return list(filter(lambda c: c.GetProgress() == CourseProgess.InProgess, self.courses))

    def GetGrades(self) -> list[int]:
        return self.grades

    def __call__(self, courseId: int) -> list[int]:
        if courseId in self.courses:
            return [self.grades[courseId]]
        else:
            return []

    def GetAverageGrade(self) -> float:
        return statistics.mean(self.grades.values())

    def GetCourseTitlesByCourseProgress(self, courseProgess: CourseProgess) -> str:
        return ", ".join(list(
            map(lambda c: c.GetTitle(),
                filter(lambda c: c.GetProgress() == courseProgess,
                       self.courses.values()))))

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nAverage grade for lectures: {self.GetAverageGrade()}\nCourses in progress: {self.GetCourseTitlesByCourseProgress(CourseProgess.InProgess)} \nCompleted courses: {self.GetCourseTitlesByCourseProgress(CourseProgess.Finished)}"

    def __lt__(self, otherStudent):
        return self.GetAverageGrade() < otherStudent.GetAverageGrade()

    def __gt__(self, otherStudent):
        return self.GetAverageGrade() > otherStudent.GetAverageGrade()

    def __hash__(self):
        return hash((self.name, self.surname))