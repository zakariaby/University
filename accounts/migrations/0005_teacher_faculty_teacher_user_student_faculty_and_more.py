# Generated by Django 4.0.5 on 2022-06-19 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_student_teacher_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unit.facutly'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unit.facutly'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
