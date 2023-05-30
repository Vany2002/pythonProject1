class Course:
    def __init__(self, id: int, title: str, lecturer=None):
        self.id = id
        self.title = title
        self.lecturer = lecturer

    def GetId(self) -> int:
        return self.id

    def SetLecturer(self, lecturer):
        self.lecturer = lecturer

    def GetLecturer(self):
        return self.lecturer

    def GetTitle(self) -> str:
        return self.title

    def __str__(self):
        return f"Course: {self.title}\nLecturer:\n{self.lecturer}"

    def __hash__(self):
        return hash((self.title, self.lecturer))