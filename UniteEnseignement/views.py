from audioop import add
from time import strftime
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
fs = FileSystemStorage(location="/templates")

from xml.dom import NoModificationAllowedErr
from django.shortcuts import render,redirect
from numpy import append
from UniteEnseignement.models import *
from django.contrib import messages
from datetime import datetime
import xlwt
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
#from weasyprint import HTML
from django.http import FileResponse



#page d'authenfication
def home(request):
	return render(request,"auth.html")

#page d'acceuil
def acceuilP(request):
	return render(request,"UE/acceuilprincipale.html")
#########Responsable de filière
def acceuil(request):
	return render(request,"UE/RespoFiliere/acceuil.html")

def index(request):
	return render(request,"UE/RespoFiliere/index.html")

def index1(request):
	return render(request,"UE/RespoFiliere/index1.html")

def index2(request):
	return render(request,"UE/RespoFiliere/index2.html")

def index3(request):
	return render(request,"UE/RespoFiliere/index3.html")

def index4(request):
	return render(request,"UE/RespoFiliere/index4.html")
#########Responsable de filière

########ANNEE SCOLAIRE
def afficherFormAn(request):
	return render(request,"UE/annee/form_an.html")

def ajoutAn(request):
    if request.method == "POST":
        anDeb =request.POST['anDebut']
        anFi = request.POST['anFin']
        an = AnneeScolaire(anDebut=anDeb, anFin= anFi)
        an.save()
        messages.info(request,"Enregistrement fait avec succès")
    else:
        pass
    return render (request, 'UE/annee/form_an.html')

########ANNEE SCOLAIRE


#############EC
#formulaire d'ajout EC
def formEC(request):
	ues = UE.objects.all()
	context ={
		'ues':ues
	}
	return render(request,"UE/EC/form_ajout_ec.html",context)

#lister les EC
def listeEC(request, idue):
	ues = UE.objects.get(id=idue).ec.all()
	
	context ={
		'ues':ues,
	}
	return render(request,"UE/EC/index1.html", context)

def listerEC(request):
	ecs = Ec.objects.all()
	context ={
		'ecs':ecs
	}
	return render(request,"UE/EC/index.html", context)

#Ajout EC par le Responsable de filière
def addEC(request):
	if request.method == "POST":
		nom =request.POST['nomEC']
		code =request.POST['codeEC']
		coef = request.POST['coefficient']
		u = request.POST['ue']
		ue=UE.objects.get(id=u)
		ec = Ec(nomEc=nom, codeEc= code, coefficient=coef, ue=ue )
		ec.save()
		messages.info(request,"l'EC est enregistré avec succès")
	else:
		pass
	ues=UE.objects.all()
	context ={
		'ues':ues
	}
	return render (request, 'UE/EC/form_ajout_ec.html',context)

#Suppression d'un EC
def deleteEC(request,idec):
	ec =Ec.objects.get(id=idec)
	ec.delete()
	ecs = Ec.objects.all()
	context ={
		'ecs':ecs
	}
	messages.info(request,"la suppression est faite avec succès")
	return render(request,"UE/EC/index.html", context)

#Editer un EC
def editEC(request,idec):
	ec =Ec.objects.get(id=idec)
	context ={
		'ec':ec
	}
	return render (request, 'UE/EC/form_ajout_ec.html',context)

#Modifier un EC
def updateEc(request,idec):
	ec =Ec.objects.get(id=idec)
	ec.nomEc =request.POST['nomEC']
	ec.codeEc =request.POST['codeEC']
	ec.coefficient =request.POST['coefficient']
	ec.save()
	messages.info(request,"l'EC est enregistré avec succès")
	ecs = Ec.objects.all()
	context ={
		'ecs':ecs
	}
	return render(request,"UE/EC/index.html", context)

#############EC

#############TYPE COUR
#formulaire d'ajout type cour
def formTC(request):
	tcs = TypeCour.objects.all() 
	ecs=Ec.objects.all()
	context={
		'tcs':tcs,
		'ecs':ecs
	}
	return render(request,"UE/typeCour/form_ajout_tc.html",context)

#lister les type cour
def listeTC(request):
	tcs = TypeCour.objects.all()
	context ={
		'tcs':tcs
	}
	return render(request,"UE/typeCour/index.html", context)

#Ajout type cour par le Responsable de filière
def addTC(request):
	if request.method == "POST":
		cm =request.POST['cm']
		tp =request.POST['tp']
		tpe =request.POST['tpe']
		td =request.POST['td']
		ec = request.POST['ec']
		ecs =Ec.objects.get(id=ec)
		tcs = TypeCour(cm=cm,tp=tp,tpe=tpe,td=td, ec = ecs )
		tcs.save()
		messages.info(request,"Enregistrement effectué avec succès")
		
	else:
		pass
	ecs=Ec.objects.all()
	context={
		'ecs':ecs
	}
	return render (request, 'UE/typeCour/form_ajout_tc.html',context)

#Suppression type cour
def deleteTC(request,idtc):
	tc =TypeCour.objects.get(id=idtc)
	tc.delete()
	messages.info(request,"la suppression est faite avec succès")
	return redirect('listeTC')

#Editer type cour
def editTC(request,idtc):
	tc =TypeCour.objects.get(id=idtc)
	ecs=Ec.objects.all()
	context ={
		'tc':tc,
		'ecs':ecs
	}
	return render (request, 'UE/typeCour/form_ajout_tc.html',context)

#Modifier un type cour
def updateTC(request,idtc):
	tc =TypeCour.objects.get(id=idtc)
	tc.cm =request.POST['cm']
	tc.tp =request.POST['tp']
	tc.tpe =request.POST['tpe']
	tc.td =request.POST['td']
	tc.volHor =request.POST['volumeHoraire']
	ec = request.POST['ec']
	ecs = Ec.objects.get(id=ec)
	tc.ec = ecs
	tc.save()
	messages.info(request,"La modification a été bien effectuée ")
	return redirect('listeTC')

#############TYPE COUR

#UE UE UE UE
#Ajout UE
def listeUE(request):
	ues = UE.objects.all()
	sms = Semestre.objects.all()
	context ={
		'ues':ues,
		'sms':sms
	}
	return render(request,"UE/UE/index.html", context)

def listUEparSM(request, idsm):
	ues = UE.Objects.filter(sm = idsm)
	sms = Semestre.objects.filter(id=idsm)
	context ={
		'ues':ues,
		'sms':sms,
	}
	return render(request,"UE/UE/index copy.html", context)

def listerUE(request,idue):
	ues = UE.objects.filter(id=idue)
	sms = Semestre.objects.filter(ue__id=idue)
	ecs= Ec.objects.filter(ue__id=idue)
	vl=0
	vlt=0
	for ec in ecs:
		tcs = TypeCour.objects.filter(ec = ec)
		for tc in tcs:
			vl=vl + tc.cm + tc.tp + tc.td + tc.tpe
		vlt +=vl
		context ={
			'ues':ues,
			'sms':sms,
			'ecs':ecs,
			'tcs':tcs,
			'vl':vl,
			'vlt':vlt,
		}
	return render(request,"UE/UE/index1.html", context)

def listUE(request,idsm):
	sms = Semestre.objects.get(id=idsm).ue.all()
	s= Semestre.objects.get(id=idsm)
	context ={
		'sms':sms,
		's':s
	}
	return render(request,"UE/UE/index2.html", context)

def addUE(request):
	if request.method == "POST":
		nom =request.POST['nomUE']
		code =request.POST['codeUE']
		credit =request.POST['credit']
		semestre = request.POST['semestre']
		sm=Semestre.objects.get(id=semestre)
		an =AnneeScolaire.objects.filter().last()
		ue = UE(nomUE=nom, codeUE= code, credit=credit,anneeScolaire=an, semestre=sm )
		ue.save()
	else:
		pass
	ues = UE.objects.all()
	sms = Semestre.objects.all()
	context ={
		'ues':ues,
		'sms':sms
	}
	return render(request,"UE/UE/form_ajout_ue.html",context)

#Suppression d'un UE
def deleteUE(request,idue):
	ue =UE.objects.get(id=idue)
	ue.delete()
	messages.info(request,"la suppression est faite avec succès")
	return redirect('listeUE')

#Editer un UE
def editUE(request,idue):
	ue =UE.objects.get(id=idue)
	context ={
		'ue':ue
	}
	return render (request, 'UE/UE/form_ajout_ue.html',context)

#Modifier un UE
def updateUE(request,idue):
	ue =UE.objects.get(id=idue)
	ue.nom =request.POST['nomUE']
	ue.code =request.POST['codeUE']
	ue.coefficient =request.POST['coefficient']
	ue.credit =request.POST['credit']
	ec = request.POST['ec']
	ecs = UE.objects.get(id=ec)
	ue.ec = ecs
	ue.save()
	messages.info(request,"l'UE est enregistré avec succès")
	return redirect('listeUE')

#formulaire d'ajout UE
def formUE(request):
	ues = UE.objects.all()
	sms = Semestre.objects.all()
	context ={
		'ues':ues,
		'sms':sms,
	}
	return render(request,"UE/UE/form_ajout_ue.html",context)

########## Fin UE	

###########SEMESTRE
#Ajout Semestre
def addSM(request):
	if request.method == "POST":
		num =request.POST['numSemestre']
		filcy = request.POST['filiereCycle']
		cyc = FilereCycle.objects.get(id=filcy)
		sm = Semestre(numSemestre=num, filereCycle=cyc)
		
		sm.save()
	else:
		pass
	cycs = FilereCycle.objects.all()
	context ={
		'cycs':cycs
	}
	return render(request,"UE/Semestre/form_ajout_sm.html",context)

#Suppression d'un Semestre
def deleteSM(request,idsm):
	sm =Semestre.objects.get(id=idsm)
	sm.delete()
	messages.info(request,"la suppression est faite avec succès")
	return redirect('listeSM')

#Editer un Semestre
def editSM(request,idsm):
	sm =Semestre.objects.get(id=idsm)
	cycs = FilereCycle.objects.all()
	context ={
		'sm':sm,
		'cycs':cycs
	}
	return render (request, 'UE/Semestre/form_ajout_sm.html',context)


#formulaire d'ajout Semestre
def formSM(request):
	cycs=FilereCycle.objects.all()
	context = {
		'cycs':cycs
	}
	return render(request,"UE/Semestre/form_ajout_sm.html",context)

#lister les Semestre
def listeSM(request):
	sms = Semestre.objects.all()
	context ={
		'sms':sms
	}
	return render(request,"UE/Semestre/index.html", context)
#modifier une semestre
def updateSM(request,idsm):
	sm =TypeCour.objects.get(id=idsm)
	sm.numSemestre =request.POST['numSemestre']
	sm.filiereCycle = request.POST['filiereCycle']
	sm.save()
	sms=Semestre.objects.all()
	context = {
		'sms':sms,
	}
	return render(request,"UE/Semestre/index.html", context)
########## Fin SEMESTRE	


#############Niveau
#formulaire d'ajout Niveau
def formNiv(request):
	nivs =Niveau.objects.all()
	context ={
		'nivs':nivs
	}
	return render(request,"UE/Niveau/form_ajout_niv.html",context)

#lister les Niveau
def listeNiv(request):
	nivs = Niveau.objects.all()
	context ={
		'nivs':nivs
	}
	return render(request,"Niveau/index.html", context)

#Ajout Niveau par le Responsable de filière
def addNiv(request):
	if request.method == "POST":
		num =request.POST['numNiveau']
		niv = Niveau(numNiveau= num )
		niv.save()
		messages.info(request,"l'enregistrement a été effectué avec succès")
	else:
		pass
	return render (request, 'UE/Niveau/form_ajout_niv.html')

#Suppression d'un Niveau
def deleteNiv(request,idec):
	niv =Niveau.objects.get(id=idec)
	niv.delete()
	messages.info(request,"la suppression est faite avec succès")
	return redirect('listeNiv')

#Editer un Niveau
def editNiv(request,idNiv):
	niv =Niveau.objects.get(id=idNiv)
	context ={
		'niv':niv
	}
	return render (request, 'UE/Niveau/form_ajout_niv.html',context)

#Modifier un Niveau
def updateNiv(request,idNiv):
	niv =Ec.objects.get(id=idNiv)
	niv.numNiv =request.POST['numNiveau']
	niv.save()
	messages.info(request,"l'enregistrement a été effectué avec succès")
	return redirect('listeNiv')

#############Niveau

#############Filiere
#formulaire d'ajout Filiere
def formFil(request):
	cycs = Cycle.objects.all()
	sms= Semestre.objects.all()
	context ={
		'cycs':cycs,
		'sms':sms
	}
	return render(request,"UE/Filiere/form_ajout_fil.html",context)

#lister les Filieres pour le responsable de filière
def listeFil(request):
	fils = Filiere.objects.all()
	context ={
		'fils':fils
	}
	return render(request,"UE/Filiere/index.html", context)

#lister les Filieres pour le responsable de scolarité
def niveau(request,idFil):
	fils = FilereCycle.objects.filter(filiere=idFil)
	context ={
		'fils':fils
	}
	return render(request,"Inscrire/RespoFiliere/listeNiv.html", context)

#afficher les différent niveau de chaque filière
def lasses(request,idFil):
	fils=Etudiant.objects.all()
	
	return render(request,"Inscrire/RespoScolarite/listeClasse.html", {fils:'fils'})

#Ajout Filiere par le Responsable de filière
def addFil(request):
	if request.method == "POST":
		nom =request.POST['nomFiliere']
		cycle =request.POST.getlist('cycle')
		anneeScolaire=AnneeScolaire.objects.filter().last()
		fil = Filiere(nomFiliere=nom, anneeScolaire=anneeScolaire )
		fil.save()
		for cyc in cycle:
			cycs =Cycle.objects.get(id=cyc)
			fil.cycle.add(cycs)
			fili=Filiere.objects.filter().last()
			filcyc=FilereCycle(cycle=cycs,filiere=fili)
			filcyc.save()
		messages.info(request,"l'enregistrement a été effectué avec succès")
	else:
		pass
	cycs =Cycle.objects.all()
	context ={
		'cycs':cycs,
	}
	return render(request,"UE/Filiere/form_ajout_fil.html",context)

#Suppression d'un Filiere
def deleteFil(request,idFil):
	fil =Filiere.objects.get(id=idFil)
	fil.delete()
	messages.info(request,"la suppression est faite avec succès")
	return redirect('listeFil')

#Editer un Filiere
def editFil(request,idFil):
	fil =Filiere.objects.get(id=idFil)
	cycs = Cycle.objects.all()
	context ={
		'fil':fil,
		'cycs' : cycs,
	}
	return render (request, 'UE/Filiere/form_ajout_fil.html',context)

#Modifier un Filiere
def updateFil(request,idFil):
	fil =Filiere.objects.get(id=idFil)
	fil.nomFiliere =request.POST['nomFiliere']
	cyc = request.POST['cycle']
	cycs = Cycle.objects.get(id=cyc)
	fil.cycle = cycs
	fil.save()
	messages.info(request,"l'enregistrement a été effectué avec succès")
	cycs = Cycle.objects.all()
	context ={
		'cycs':cycs,
	}
	return render(request,"UE/Filiere/index.html",context)

#############Filiere


#############Cycle
#formulaire d'ajout Cycle
def formCyc(request):
	return render(request,"UE/Cycle/form_ajout_cyc.html")

#lister les Cycle
def listeCyc(request):
	cycs = FilereCycle.objects.all()
	context ={
		'cycs':cycs,
	}
	return render(request,"UE/Cycle/index.html", context)

#Ajout Filiere par le Responsable de filière
def addCyc(request):
	if request.method == "POST":
		nom =request.POST['nom']
		niv =request.POST['niveau']
		cyc = Cycle(nom=nom, niveau=niv)
		cyc.save()
		c =Cycle.objects.filter().last()
		#for n in niv:
			#niveau =Niveau.objects.get(id=n)
			#ajout dans la table d'association créée
			#cn = CycleNiveau(cycle= c, niveau=niveau)
			#cn.save()
			#Ajout dans la table d'association par défaut
			#cyc.niveau.add(niveau)
		
		#messages.info(request,"l'enregistrement a été effectué avec succès")
	else:
		pass
	return render(request,"UE/Cycle/form_ajout_cyc.html")

#Suppression d'une Cycle
def deleteCyc(request,idCyc):
	cyc =Cycle.objects.get(id=idCyc)
	cyc.delete()
	messages.info(request,"la suppression est faite avec succès")
	return redirect('listeCyc')

#Editer un Cycle
def editCyc(request,idCyc):
	cyc = Cycle.objects.get(id=idCyc)
	context ={
		'cyc' : cyc,
	}
	return render (request, 'UE/Cycle/form_ajout_cyc.html',context)

#Modifier une Cycle
def updateCyc(request,idCyc):
	cyc =Cycle.objects.get(id=idCyc)
	cyc.nom =request.POST['nom']
	cyc.niveau = request.POST['niveau']
	cyc.save()
	return render(request,"UE/Cycle/index.html")

#############Cycle
##############FIN UNITE D'ENSEIGNANT

################DEBUT INSCRIPTION
##############Etudiant
#carte Etudiant
def carteEtu(request):
	return render(request,"Inscrire/RespoScolarite/carteEtu.html")

#formulaire inscription étudiant
def form_etu(request):
	fils =FilereCycle.objects.all()
	context={
		'fils':fils,
		
	}
	return render(request,"Inscrire/RespoScolarite/form-ins-etu.html", context)

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
		filiere =request.POST['filereCycle']
		nomP =request.POST['nomP']
		prenomP =request.POST['prenomP']
		adresseP =request.POST['adresseP']
		numTelP= request.POST['numTelP']
		emailP = request.POST['emailP']
		nomI = request.POST['nomIdentifiant']
		numI= request.POST['numIdentifiant']
		sexe=request.POST['sexe']
		nationalite = request.POST['nationalite']
		anneeScolaire=AnneeScolaire.objects.filter().last()
		photo=request.FILES['photo']
		etu = Etudiant(nom=nomEtu, prenom= prenomEtu, adresse=adresseEtu,sexe=sexe,nationalite= nationalite,dateNaiss=dateNaissEtu, lieuNaiss=lieuNaissEtu, email= emailEtu, numTel=numTelEtu,password=passwordEtu,photo=photo, nomIdentifiant=nomI, numIdentifiant=numI)
		etu.save()
		etudiant=Etudiant.objects.filter().last()
		parent = Parent(nomP=nomP, prenom= prenomP, adresse=adresseP,email=emailP,numTel=numTelP,etudiant=etudiant)
		parent.save()
		fil= FilereCycle.objects.get(id= filiere)
		ins= Inscription(filiereCycle=fil,etudiant=etudiant,anneeScolaire=anneeScolaire)
		ins.save()
		messages.info(request,"l'Etudiant est enregistré avec succès")
		
	fils = FilereCycle.objects.all()
	context={
		'fils':fils,
	}
	return render(request,"Inscrire/RespoScolarite/form-ins-etu.html", context)

#afficher la réinscription
def voirEtu(request):
	if request.method == "POST":
		codePer = request.POST['codePermanent']
		etudiant =Etudiant.objects.get(codePermanent=codePer)
		filieres = FilereCycle.objects.all()
		code= Etudiant.objects.all()
	context={
		etudiant: 'etudiant',
		filieres: 'filieres',
		code:'code'
		}
	return render(request, 'Inscrire/RespoScolarite/formAfficheEtu.html', context)


#Réinscription
def formVerif(request):
	return render(request, 'Inscrire/RespoScolarite/form-verif-etu.html')


#modifier Etudiant
def updateEtu(request, idEtu):
		etu =Etudiant.objects.get(id=idEtu)
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
		fil = request.POST['filiereCycle']
		fils = FilereCycle.objects.get(id=fil)
		etu.filiere = fils
		etu.save()
		messages.info(request,"l'Etudiant est enregistré avec succès")
		etudiants = Etudiant.objects.all()
		context={
			'etudiants':etudiants
		}	
		return render(request, 'Incrire/RespoScolarite/form-list-etu.html', context)

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
	return render (request, 'Incrire/RespoScolarite/form-ins-etu.html',context)


def listeEtu(request):
	etudiants = Etudiant.objects.all()
	context ={
		'etudiants':etudiants
	}
	return render(request,"Inscrire/RespoScolarite/liste-etu.html", context)


def affCarte(request,idetu): 
	etudiant =Etudiant.objects.get(codePermanent=idetu)
	context ={
		'etudiant':etudiant
	}
	return render(request,"Inscrire/RespoScolarite/CarteEtu.html", context)

####Exporter sous format excel
def export_excel_etu(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="classes.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Etudiants') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Prénom', 'Nom', 'Date de Naissance', 'Lieu de Naissance', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Etudiant.objects.all().values_list('prenom', 'nom', 'dateNaiss', 'lieuNaiss')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

#####Générer la liste des étudiants inscrits en pdf
#def export_pdf_etu(request):
#	etudiants = Etudiant.objects.all()
#   html_string = render_to_string('core/pdf_inscrits.html', {'etudiants': etudiants})
#
#    html = HTML(string=html_string)
#    html.write_pdf(target='/images/les_inscrits.pdf')

#    fs = FileSystemStorage('/images')
#   with fs.open('les_inscrits.pdf') as pdf:
#        response = HttpResponse(pdf, content_type='application/pdf')
#        response['Content-Disposition'] = 'attachment; filename="les_inscrits.pdf"'
#        return response

#    return response
def export_pdf_etu(request):
	# création d'un byte stream buffer
	buffer = io.BytesIO()
	#créer un canvas
	c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
	#Créer un Objet Text
	textObj= c.beginText()
	textObj.setTextOrigin(inch, inch)
	textObj.setFont('Helvetica', 14)

	etudiants= Etudiant.objects.all()
	
	#Ajout des lignes dans le text
	lignes =[]
	
	for etudiant in etudiants:
		lignes.append(etudiant.prenom)
		lignes.append(etudiant.nom)
		lignes.append(str(etudiant.dateNaiss))
		lignes.append(etudiant.lieuNaiss)
		lignes.append(etudiant.numTel)
		lignes.append(" ")

	for ligne in lignes:
		textObj.textLine(ligne)


	c.drawText(textObj)
	c.showPage()
	c.save()
	buffer.seek(0)

	return FileResponse(buffer, as_attachment=True, filename='Liste_des_inscrits.pdf')
######fin Etudiant

#######Enseignant

#lister les enseignants
def listeEns(request):
	enseignants = Enseignant.objects.all()
	context ={
		'enseignants':enseignants
	}
	return render(request,"Inscrire/RespoFiliere/liste-ens.html", context)

#formulaire inscription enseignant
def form_ins_ens(request):
	ens = Enseignant.objects.all()
	context={ens:'ens'}
	return render(request,"Inscrire/RespoFiliere/form_ins_ens.html",context)

#Ajouter Enseignant
def addEns(request):
	if request.method == "POST":
		nom =request.POST['nom']
		prenom = request.POST['prenom']
		adresse =request.POST['adresse']
		email =request.POST['email']
		password =request.POST['password']
		passe =request.POST['passe']
		numTel =request.POST['numTel']
		#filiere =request.POST['filiere']
		anneeScolaire=AnneeScolaire.objects.filter().last()
		dateEntree=datetime.now()
		#fil =Filiere.objects.get(id=filiere)
		if passe==password:
			sm = Enseignant(nom=nom, prenom=prenom, adresse=adresse,email= email, password=password,dateEntree=dateEntree, numTel=numTel)
			sm.save()
			#sm.anneeScolaire.add(anneeScolaire)
			messages.info(request,"l'enregistrement est effectué avec succès")
		else:
			mot = "mots de passe incorrect. Veuillez remplir de nouveau les champs.Merci! "	
			fils= Filiere.objects.all()
			context = {
				'fils':fils,
				'mot':mot
			}
			return render(request,"Inscrire/RespoFiliere/form_ins_ens.html",context)

	else:
		pass
	fils= Filiere.objects.all()
	context = {
		'fils':fils
	}
	return render(request,"Inscrire/RespoFiliere/form_ins_ens.html",context)

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

####Exporter sous format excel
def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Prénom', 'Nom', 'Adresse', 'Email', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Enseignant.objects.all().values_list('prenom', 'nom', 'adresse', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

########FinEnseignant



			
		

###########FIN INSCRIPTION
