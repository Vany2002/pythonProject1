from Practika2.Pr_15.mentor import Mentor
import statistics
from typing import TypedDict


class CourseGrades(TypedDict):
    courseId: int
    grades: list[int]


class Lecturer(Mentor):

    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = {}

    def AddGrade(self, courseId: int, grade: int):
        if courseId in self.grades.keys():
            self.grades[courseId].append(grade)
        else:
            self.grades[courseId] = [grade]

    def GetGrades(self) -> dict[int, list[int]]:
        return self.grades

    def GetAverageGrade(self) -> float:
        grades = []
        for courseGrades in self.grades.values():
            grades += courseGrades
        return statistics.mean(grades)

    def __call__(self, courseId: int) -> list[int]:
        if courseId in self.grades:
            return self.grades[courseId]
        else:
            return []

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nAverage grade for lectures: {self.GetAverageGrade()}"

    def __lt__(self, other):
        return self.GetAverageGrade() < other.GetAverageGrade()

    def __gt__(self, other):
        return self.GetAverageGrade() > other.GetAverageGrade()

    def __hash__(self):
        return hash(self.name, self.surname)