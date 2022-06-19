from django.db import models
from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_delete, post_save

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

CONDUCTS = [
    ("good", "Bonne"),
    ("bad", "Mauvaise"),
    ("yellow_flag", "Rectifiable"),
    ("red_flag", "Insupportable"),
]


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="teacher")
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    faculty = models.ForeignKey(to="unit.Faculty", on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=60, blank=False)
    available = models.BooleanField(default=True)
    count_available = models.IntegerField(default=0)
    email = models.EmailField(max_length=60, blank=False, unique=True)
    conduct = models.CharField(max_length=20, choices=CONDUCTS, default="")
    ended_at = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Tc: {} {}'.format(self.first_name, self.last_name)


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="student")
    faculty = models.ForeignKey(to="unit.Faculty", on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=70, choices=LEVEL, default="")
    ended_at = models.DateTimeField()
    nationality = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=60, blank=False)
    sexe = models.CharField(max_length=10, choices=GENDER, default="")
    email = models.EmailField(max_length=60, blank=False, unique=True)
    photo = models.ImageField(upload_to='images/students/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'St: {} {}'.format(self.first_name, self.last_name)


# @receiver(post_save, sender=User)
# def create_default_userprofile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_default_userprofile(sender, instance, **kwargs):
#     instance.shop_user_related.save()
