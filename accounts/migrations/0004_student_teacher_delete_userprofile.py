# Generated by Django 4.0.5 on 2022-06-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210720_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('first_year', '1ere annee'), ('second_year', '2eme annee'), ('third_year', 'License'), ('fourth_year', 'Master 1'), ('fifth_year', 'Master 2')], default='', max_length=70)),
                ('ended_at', models.DateTimeField()),
                ('nationality', models.CharField(blank=True, max_length=60)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=60)),
                ('sexe', models.CharField(choices=[('male', 'Homme'), ('female', 'Femme')], default='', max_length=10)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('photo', models.ImageField(upload_to='images/students/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('ended_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
