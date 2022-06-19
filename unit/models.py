from django.db import models


SEMESTER = (
    ('first_semester', 'Semestre 1'),
    ('second_semester', 'Semestre 2'),
)


class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self) -> str:
        return self.name


class Lecture(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    credit = models.IntegerField()
    hours = models.IntegerField()
    semester = models.CharField(max_length=70, choices=SEMESTER, default="")

    def __str__(self) -> str:
        return "{}".format(self.name)


class Grade(models.Model):
    student = models.ForeignKey(to="accounts.Student", on_delete=models.CASCADE, null=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.DO_NOTHING, null=True)
    mark = models.IntegerField()
    appreciation = models.TextField()
    

    def __str__(self) -> str:
        return "{} {} : {}".format(self.student.first_name, self.student.last_name, self.credit)

