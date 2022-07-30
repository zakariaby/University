from django.db import models


SEMESTER = (
    ('first_semester', 'Semestre 1'),
    ('second_semester', 'Semestre 2'),
)

PROGRAM = (
    ('mic', 'Multimedia'),
    ('tr', 'Telecom. & Reseaux'),
)


class Lecture(models.Model):
    """
        Lecture are the content of every Factulty (UE)
    """
    name = models.CharField(max_length=100, unique=True, blank=False)
    teacher = models.ForeignKey("accounts.Teacher", on_delete=models.DO_NOTHING, null=True)
    program = models.CharField(max_length=10, choices=PROGRAM, default="tr")
    credit = models.IntegerField()
    hours = models.IntegerField()
    semester = models.CharField(max_length=70, choices=SEMESTER, default="")

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{}".format(self.name)

class Faculty(models.Model): # Facutlies __repr__ UE
    '''
        Each Faculty (UE) has its name and will contains Lectures
    '''
    name = models.CharField(max_length=100, unique=True, blank=False)
    lectures = models.ManyToManyField(Lecture)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Grade(models.Model):
    student = models.ForeignKey(to="accounts.Student", on_delete=models.CASCADE, null=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.DO_NOTHING, null=True)
    mark = models.IntegerField()
    appreciation = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return "{} {} : {}".format(self.student.first_name, self.student.last_name, self.credit)

