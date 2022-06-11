from datetime import datetime
from pickle import FALSE
from django.db import models
from django.db.models.aggregates import Max
from django.utils import timezone
import os
import datetime

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
	 
class Cycle(models.Model):
	nom =  models.CharField(max_length=10)
	niveau = models.IntegerField(null=False)


class Filiere(models.Model):
	nomFiliere =models.CharField(max_length=60,unique=True, blank=False)
	cycle = models.ManyToManyField(Cycle)
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=False)

class FilereCycle(models.Model):
	cycle=models.ForeignKey(Cycle, on_delete=models.CASCADE,null=True,blank=False)
	filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE,null=True,blank=False)

	
class Semestre(models.Model):
	numSemestre = models.IntegerField(blank=False,null=False)
	filereCycle = models.ForeignKey(FilereCycle, on_delete=models.CASCADE,null=True,blank=False)

class UE(models.Model):
	codeUE= models.CharField(max_length=60, blank=False, unique=True, null=False)
	nomUE = models.CharField(max_length=60, blank=False, unique=True, null=False)
	credit = models.IntegerField()
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=False,blank=False)
	semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE,null=False,blank=False)

class Ec(models.Model):
	codeEc = models.CharField(max_length=60, blank=False)
	nomEc = models.CharField(max_length=60, blank=False)
	description = models.TextField(null=True,blank=True)
	objectif = models.TextField(null=True,blank=True)
	competences = models.TextField(null=True,blank=True)
	prerequis = models.TextField(null=True,blank=True)
	contenu = models.TextField(null=True,blank=True)
	coefficient = models.IntegerField()
	ue = models.ForeignKey(UE, on_delete=models.CASCADE,null=False,blank=False)
	

class TypeCour(models.Model):
	cm= models.IntegerField( blank=False, unique=True)
	tp= models.IntegerField( blank=False, unique=True)
	tpe= models.IntegerField( blank=False, unique=True)
	td= models.IntegerField( blank=False, unique=True)
	ec = models.ForeignKey(Ec, on_delete=models.CASCADE)

	
class RespoFiliere(models.Model):
	nom =models.CharField(max_length=60, blank=False)
	prenom =models.CharField(max_length=60, blank=False)
	adresse=models.CharField(max_length=60, blank=False)
	numTel =models.CharField(max_length=60, blank=False)
	email =models.EmailField(max_length=60, blank=False)
	password = models.CharField(max_length=60, blank=False)
	dateEntree = models.DateTimeField(default=timezone.now, verbose_name="Date d'entrée de l'étudiant")
	dateSortie = models.DateField(null=True,blank=False)
	role =models.CharField(max_length=60)
	filiere = models.ForeignKey(Filiere,on_delete=models.CASCADE,blank=False)
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=False)
	ec = models.ForeignKey(Ec, on_delete=models.CASCADE,null=True,blank=False)

class Enseignant(models.Model):
	nom =models.CharField(max_length=60, blank=False)
	prenom =models.CharField(max_length=60, blank=False)
	adresse=models.CharField(max_length=60, blank=False)
	numTel =models.CharField(max_length=60, blank=False)
	email =models.EmailField(max_length=60, blank=False,unique=True)
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
	email =models.EmailField(max_length=60, blank=False,unique=True)
	password = models.CharField(max_length=60, blank=False)
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=True)

class Etudiant(models.Model):
	codePermanent = models.AutoField(primary_key=True)
	nom =models.CharField(max_length=60, blank=True)
	prenom =models.CharField(max_length=60, blank=True)
	adresse =models.CharField(max_length=60, blank=True)
	numTel =models.CharField(max_length=60, blank=True)
	email =models.EmailField(max_length=60,blank=True,unique=True)
	dateNaiss = models.DateField(blank=True)
	lieuNaiss =models.CharField(max_length=60,blank=True)
	dateEntree = models.DateField(default=timezone.now, verbose_name="Date d'entrée de l'étudiant",blank=False,null=True)
	dateSortie = models.DateField(blank=True,null=True)
	delegue =models.BooleanField(default=False,blank=True)
	password = models.CharField(max_length=60,blank=True)
	sexe = models.CharField(max_length=60,blank=True)
	nationalite= models.CharField(max_length=60,blank=True)
	nomIdentifiant =  models.CharField(max_length=10)
	numIdentifiant = models.IntegerField(blank=True)
	photo= models.ImageField(upload_to='images/')

class Parent(models.Model):
	nomP=models.CharField(max_length=60, blank=True)
	prenom =models.CharField(max_length=60, blank=True)
	adresse =models.CharField(max_length=60, blank=True)
	numTel =models.CharField(max_length=60, blank=True)
	email =models.EmailField(max_length=60, blank=True,unique=True)	
	etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)


class Inscription(models.Model):
	anneeScolaire = models.ForeignKey(AnneeScolaire, on_delete=models.CASCADE,null=True)
	etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
	respoScolarite = models.ForeignKey(RespoScolarite, on_delete=models.CASCADE, null=True)
	filiereCycle = models.ForeignKey(FilereCycle, on_delete=models.CASCADE,null=True)
	
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

class ExcelFileUpload(models.Model):
	Excel_file_upload =models.FileField(upload_to="excel")

