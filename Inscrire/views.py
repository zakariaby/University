from django.shortcuts import render,redirect
from django.template import context
from Inscrire.models import AnneeScolaire, Etudiant,Inscription,RespoScolarite,Filiere,Enseignant,UE,Ec
from django.http import HttpResponse
from django.contrib import messages

#page d'authentification
def home(request):
	return render(request,"auth.html")

#page d'acceuil
def acceuilP(request):
	return render(request,"acceuilprincipale.html")

#formulaire de réinscription
def form_reins(request):
	return render(request,"form_reins1.html")

#Ajout Description
def ajoutDesc(request):
	return render(request,"ec/description.html")

#Ajout Présentation
def ajoutPres(request):
	return render(request,"ec/presentation.html")

#page d'acceuil du professeur
def acceuilEns(request):
	return render(request,"Enseignant/acceuil.html")

#carte Etudiant:
def carteEtu(request):
	return render(request,"RespoScolarite/carteEtu.html")


#lister les étudiants
def listeClasse(request):
	etudiants = Etudiant.objects.all()
	context ={
		'etudiants':etudiants
	}
	return render(request,"RespoScolarite/form-list-etu.html", context)

#Formulaire d'incription des présence
def presence(request):
	etudiants = Etudiant.objects.all()
	context ={
		'etudiants':etudiants
	}
	return render(request,"Enseignant/listPresence.html", context)


#######Enseignant

#lister les enseignants
def listeEns(request):
	enseignants = Enseignant.objects.all()
	context ={
		'enseignants':enseignants
	}
	return render(request,"RespoFiliere/liste-ens.html", context)

#formulaire inscription enseignant
#def form_ins_ens(request):
	#fils = Filiere.objects.all()
	#context={fils:'fils'}
	#return render(request,"RespoFiliere/form_ins_ens.html",context)

#Ajouter Enseignant
def addEns(request):
	if request.method == "POST":
		nom =request.POST['nom']
		prenom = request.POST['prenom']
		adresse =request.POST['adresse']
		email =request.POST['email']
		password =request.POST['password']
		dateEntree =request.POST['dateEntree']
		numTel =request.POST['numTel']
		filiere =request.POST['filiere']
		anneeScolaire=AnneeScolaire.objects.filter().last()
		fil =Filiere.objects.get(id=filiere)
		sm = Enseignant(nom=nom, prenom=prenom, adresse=adresse,email= email, password=password,dateEntree=dateEntree,filiere=fil, numTel=numTel)
		sm.save()
		sm.anneeScolaire.add(anneeScolaire)
		messages.info(request,"l'enregistrement est effectué avec succès")
	else:
		pass
	fils= Filiere.objects.all()
	context = {
		'fils':fils
	}
	return render(request,"RespoFiliere/form_ins_ens.html",context)

#Suppression d'un Enseignant
def deleteEns(request,idEns):
	ens = Enseignant.objects.get(id=idEns)
	ens.delete()
	messages.info(request,"la suppression est faite avec succès")
	enseignants= Enseignant.objects.all()
	context = {
		'enseignants':enseignants
	}
	return render('RespoFiliere/liste-ens',context)

#Editer un Enseignant
def editEns(request,idEns):
	ens =Enseignant.objects.get(id=idEns)
	fils = Filiere.objects.all()
	context ={
		'fils':fils,
		'ens' : ens,
	}
	return render (request, 'RespoFiliere/form_ins_ens.html',context)

#Modifier un Enseignant
def updateEns(request,idEns):
	ens =Enseignant.objects.get(id=idEns)
	ens.nom =request.POST['nom']
	ens.prenom =request.POST['prenom']
	ens.adresse =request.POST['adresse']
	ens.numTel =request.POST['numTel']
	ens.password =request.POST['password']
	ens.dateEntree =request.POST['dateEntree']
	ens.email =request.POST['email']
	ens.anneeScolaire=AnneeScolaire.objects.filter().last()
	fil = request.POST['filiere']
	fils = Filiere.objects.get(id=fil)
	ens.filiere = fils
	ens.save()
	messages.info(request,"l'enregistrement a été effectué avec succès")
	enseignants= Enseignant.objects.all()
	context = {
		'enseignants':enseignants
	}
	return render('RespoFiliere/liste-ens',context)


########FinEnseignant

##############Etudiant
#formulaire inscription étudiant
def form_ins_etu(request):
	fils = Filiere.objects.all()
	context={fils:'fils'}
	return render(request,"RespoScolarite/form-ins-etu.html", context)

#Ajouter un étudiant dans la base de données
def addEtu(request):
	if request.method == "POST":
		nomEtu =request.POST['nom']
		prenomEtu =request.POST['prenom']
		adresseEtu =request.POST['adresse']
		numTelEtu= request.POST['numTel']
		emailEtu = request.POST['email']
		passwordEtu=request.POST['password']
		dateNaissEtu = request.POST['dateNaiss']
		lieuNaissEtu = request.POST['lieuNaiss']
		dateEntreeEtu=request.POST['dateEntree']
		delegue=request.POST['delegue']
		filiere =request.POST['filiere']
		anneeScolaire=AnneeScolaire.objects.filter().last()
		fil_etu =Filiere.objects.get(id=filiere)
		etu = Etudiant(nom=nomEtu, prenom= prenomEtu, adresse=adresseEtu,dateNaiss=dateNaissEtu,lieuNaiss=lieuNaissEtu, email= emailEtu, numTel=numTelEtu,password=passwordEtu,dateEntree=dateEntreeEtu,delegue=delegue,filiere=fil_etu,respoScolarite=respoScolariteEtu)
		etu.save()
		etu.anneeScolaire.add(anneeScolaire)
		messages.info(request,"l'Etudiant est enregistré avec succès")
	fils = Filiere.objects.all()
	context={fils:'fils'}
	return render(request,"RespoScolarite/form-ins-etu.html", context)

#modifier Etudiant
def updateEtu(request, idEtu):
		etu =UE.objects.get(id=idEtu)
		etu.nom =request.POST['nom']
		etu.prenom =request.POST['prenom']
		etu.adresse =request.POST['adresse']
		etu.numTel= request.POST['numTel']
		etu.email = request.POST['email']
		etu.password=request.POST['password']
		etu.dateNaiss = request.POST['dateNaiss']
		etu.lieuNaiss = request.POST['lieuNaiss']
		etu.dateEntree=request.POST['dateEntree']
		etu.delegue=request.POST['delegue']
		etu.anneeScolaire=AnneeScolaire.objects.filter().last()
		fil = request.POST['filiere']
		fils = Filiere.objects.get(id=fil)
		etu.filiere = fils
		etu.save()
		messages.info(request,"l'Etudiant est enregistré avec succès")
		etudiants = Etudiant.objects.all()
		context={
			'etudiants':etudiants
		}	
		return render(request, 'RespoScolarite/form-list-etu.html', context)

#Suppression d'un Etudiant
def deleteEtu(request,idetu):
	etu =Etudiant.objects.get(id=idetu)
	etu.delete()
	messages.info(request,"la suppression est faite avec succès")
	return redirect('form-list-etu')

#Editer un Etudiant
def editEtu(request,idetu):
	etu =Etudiant.objects.get(id=idetu)
	context ={
		'etu':etu
	}
	return render (request, 'UE/form-ins-etu.html',context)
######fin Etudiant