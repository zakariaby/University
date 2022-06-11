from multiprocessing import set_executable
from django.db import models
from django.forms import ModelForm,Textarea
from django.utils import timezone

# Create your models here.
class AnneeScolaire(models.Model):
	anDebut = models.IntegerField()
	anFin =models.IntegerField()

class Etablissement(models.Model):
	matricule = models.CharField(max_length=255)
	nom = models.CharField(max_length=255)
	numTel = models.IntegerField()
	siteWeb = models.CharField(max_length=255)
	logo = models.ImageField(null=True, blank=True)
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=True)

class Niveau(models.Model):
	numNiveau = models.IntegerField()

class Cycle (models.Model):
	nom =  models.CharField(max_length=10)
	niveau = models.ManyToManyField(Niveau)

class Filiere(models.Model):
	nomFiliere =models.CharField(max_length=60,unique=True, blank=False)
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=True)
	cycle = models.ManyToManyField(Cycle)

class VolumeHoraire(models.Model):
	typeCours = models.CharField(max_length=60, blank=False)
	heurAttribue = models.IntegerField()



class Ec(models.Model):
	codeEc = models.CharField(max_length=60, blank=False)
	nomEc = models.CharField(max_length=60, blank=False)
	presentation = models.TextField(null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	objectif = models.TextField(null=True,blank=True)
	competences = models.TextField(null=True,blank=True)
	prerequis = models.TextField(null=True,blank=True)
	contenu = models.TextField(null=True,blank=True)

class UE(models.Model):
	codeUE= models.CharField(max_length=60, blank=False, unique=True)
	nomUE = models.CharField(max_length=60, blank=False, unique=True)
	credit = models.IntegerField()
	coefficient = models.IntegerField()
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=True,blank=False)
	volumeHoraire = models.ForeignKey(VolumeHoraire, on_delete=models.CASCADE,null=True,blank=False)
	ec = models.ForeignKey(Ec, on_delete=models.CASCADE,null=True,blank=False)
	


class Enseignant(models.Model):
	nom =models.CharField(max_length=60, blank=False)
	prenom =models.CharField(max_length=60, blank=False)
	adresse=models.CharField(max_length=60, blank=False)
	numTel =models.CharField(max_length=60, blank=False)
	email =models.EmailField(max_length=60, blank=False)
	password = models.CharField(max_length=60, blank=False)
	dateEntree = models.DateTimeField(default=timezone.now, verbose_name="Date d'entrée de l'étudiant")
	dateSortie = models.DateField(null=True,blank=False)
	filiere = models.ManyToManyField(Filiere, through='EnsFiliere',blank=False)
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=True)
	ec = models.ForeignKey(Ec, on_delete=models.CASCADE,null=True,blank=False)
	
class RespoScolarite(models.Model):
	nom =models.CharField(max_length=60, blank=False)
	prenom =models.CharField(max_length=60, blank=False)
	adresse =models.CharField(max_length=60, blank=False)
	numTel =models.CharField(max_length=60, blank=False)
	email =models.EmailField(max_length=60, blank=False)
	password = models.CharField(max_length=60, blank=False)
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=True)

class TypeIdentite(models.Model):
	nomIdentifiant =  models.CharField(max_length=10)
	numIdentifiant = models.IntegerField()

class Etudiant(models.Model):
	codePermanent = models.AutoField(primary_key=True)
	nom =models.CharField(max_length=60, blank=True)
	prenom =models.CharField(max_length=60, blank=True)
	adresse =models.CharField(max_length=60, blank=True)
	numTel =models.CharField(max_length=60, blank=True)
	email =models.EmailField(max_length=60, blank=True)
	dateNaiss = models.DateField()
	lieuNaiss =models.CharField(max_length=60, blank=True)
	dateEntree = models.DateField(default=timezone.now, verbose_name="Date d'entrée de l'étudiant")
	dateSortie = models.DateField(null=True)
	delegue =models.BooleanField(default=False)
	password = models.CharField(max_length=60, blank=True)
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=True)
	sexe = models.CharField(max_length=60, blank=True)
	nationalite= models.CharField(max_length=60, blank=True)
	typeIdentite = models.OneToOneField(TypeIdentite, on_delete=models.CASCADE,blank=True,null=True)

class Inscription(models.Model):
	anneeScolaire = models.CharField(max_length=60, blank=False)
	etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
	respoScolarite = models.ForeignKey(RespoScolarite, on_delete=models.CASCADE)
	filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

class EnsFiliere(models.Model):
	RespoFiliere = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
	filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)


class Modalite(models.Model):
	fraisInscription = models.IntegerField()
	mensualite = models.IntegerField()
	filiere = models.ManyToManyField(Filiere, through='ModFiliere')
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=True)

class ModFiliere(models.Model):
	modalite = models.ForeignKey(Modalite, on_delete=models.CASCADE)
	filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

