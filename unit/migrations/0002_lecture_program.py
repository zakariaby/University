# Generated by Django 4.0.5 on 2022-07-30 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='program',
            field=models.CharField(choices=[('mic', 'Multimedia'), ('tr', 'Telecom. & Reseaux')], default='tr', max_length=10),
        ),
    ]
