# Generated by Django 3.1.7 on 2022-03-25 14:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnneeScolaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anDebut', models.IntegerField()),
                ('anFin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeEc', models.CharField(max_length=60)),
                ('nomEc', models.CharField(max_length=60)),
                ('presentation', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('objectif', models.TextField(blank=True, null=True)),
                ('competences', models.TextField(blank=True, null=True)),
                ('prerequis', models.TextField(blank=True, null=True)),
                ('contenu', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=60)),
                ('prenom', models.CharField(max_length=60)),
                ('adresse', models.CharField(max_length=60)),
                ('numTel', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('dateEntree', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'entrée de l'étudiant")),
                ('dateSortie', models.DateField(null=True)),
                ('anneeScolaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.anneescolaire')),
                ('ec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.ec')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('codePermanent', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=60)),
                ('prenom', models.CharField(blank=True, max_length=60)),
                ('adresse', models.CharField(blank=True, max_length=60)),
                ('numTel', models.CharField(blank=True, max_length=60)),
                ('email', models.EmailField(blank=True, max_length=60)),
                ('dateNaiss', models.DateField()),
                ('lieuNaiss', models.CharField(blank=True, max_length=60)),
                ('dateEntree', models.DateField(default=django.utils.timezone.now, verbose_name="Date d'entrée de l'étudiant")),
                ('dateSortie', models.DateField(null=True)),
                ('delegue', models.BooleanField(default=False)),
                ('password', models.CharField(blank=True, max_length=60)),
                ('sexe', models.CharField(blank=True, max_length=60)),
                ('nationalite', models.CharField(blank=True, max_length=60)),
                ('anneeScolaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.anneescolaire')),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomFiliere', models.CharField(max_length=60, unique=True)),
                ('anneeScolaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.anneescolaire')),
                ('cycle', models.ManyToManyField(to='Inscrire.Cycle')),
            ],
        ),
        migrations.CreateModel(
            name='Modalite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fraisInscription', models.IntegerField()),
                ('mensualite', models.IntegerField()),
                ('anneeScolaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.anneescolaire')),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numNiveau', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeIdentite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomIdentifiant', models.CharField(max_length=10)),
                ('numIdentifiant', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VolumeHoraire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeCours', models.CharField(max_length=60)),
                ('heurAttribue', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codeUE', models.CharField(max_length=60, unique=True)),
                ('nomUE', models.CharField(max_length=60, unique=True)),
                ('credit', models.IntegerField()),
                ('coefficient', models.IntegerField()),
                ('anneeScolaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.anneescolaire')),
                ('ec', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.ec')),
                ('volumeHoraire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.volumehoraire')),
            ],
        ),
        migrations.CreateModel(
            name='RespoScolarite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=60)),
                ('prenom', models.CharField(max_length=60)),
                ('adresse', models.CharField(max_length=60)),
                ('numTel', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('anneeScolaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.anneescolaire')),
            ],
        ),
        migrations.CreateModel(
            name='ModFiliere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inscrire.filiere')),
                ('modalite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inscrire.modalite')),
            ],
        ),
        migrations.AddField(
            model_name='modalite',
            name='filiere',
            field=models.ManyToManyField(through='Inscrire.ModFiliere', to='Inscrire.Filiere'),
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anneeScolaire', models.CharField(max_length=60)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inscrire.etudiant')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inscrire.filiere')),
                ('respoScolarite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inscrire.resposcolarite')),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='typeIdentite',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.typeidentite'),
        ),
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=255)),
                ('nom', models.CharField(max_length=255)),
                ('numTel', models.IntegerField()),
                ('siteWeb', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('anneeScolaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inscrire.anneescolaire')),
            ],
        ),
        migrations.CreateModel(
            name='EnsFiliere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RespoFiliere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inscrire.enseignant')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inscrire.filiere')),
            ],
        ),
        migrations.AddField(
            model_name='enseignant',
            name='filiere',
            field=models.ManyToManyField(through='Inscrire.EnsFiliere', to='Inscrire.Filiere'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='niveau',
            field=models.ManyToManyField(to='Inscrire.Niveau'),
        ),
    ]
