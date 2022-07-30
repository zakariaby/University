from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

from unit.models import PROGRAM

# Create your models here.

GENDER = [
    ("male", 'Homme'),
    ("female", 'Femme')
]

LEVEL = [
    ('first_year', '1ere annee'),
    ('second_year', '2eme annee'),
    ('third_year', 'License'),
    ('fourth_year', 'Master 1'),
    ('fifth_year', 'Master 2'),
]

TEACHER_STATUS = [
    ("full_time", "Permanent"),
    ("part_time", "Non Permanent")
]

PROGRAM = [
    ("mic", 'Multimedia'),
    ("tr", 'Telecom. & Reseaux')
]

class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="teacher")
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=60, blank=False)
    available = models.BooleanField(default=True)
    sexe = models.CharField(max_length=10, choices=GENDER, default="")
    status = models.CharField(max_length=100, choices=TEACHER_STATUS, default="")
    nationality = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=60, blank=False, unique=True)
    ended_at = models.DateTimeField()
    photo = models.ImageField(upload_to="images/teachers/", default='teacher.png')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Tc: {} {}'.format(self.first_name, self.last_name)


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="student")
    program = models.CharField(max_length=100, choices=PROGRAM, default="")
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=70, choices=LEVEL, default="")
    ended_at = models.DateTimeField()
    nationality = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=60, blank=False)
    sexe = models.CharField(max_length=10, choices=GENDER, default="")
    email = models.EmailField(max_length=60, blank=False, unique=True)
    photo = models.ImageField(upload_to='images/students/', default='student.png')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'St: {} {}'.format(self.first_name, self.last_name)


class Staff(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="staff")
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=60, blank=False)
    available = models.BooleanField(default=True)
    sexe = models.CharField(max_length=10, choices=GENDER, default="")
    nationality = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=60, blank=False, unique=True)
    position = models.CharField(max_length=100)
    ended_at = models.DateTimeField()
    photo = models.ImageField(upload_to="images/staff/", default='staff.png')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Tc: {} {}'.format(self.first_name, self.last_name)

