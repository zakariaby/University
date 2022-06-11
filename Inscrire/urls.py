from django.urls import path
from . import views

urlpatterns = [
    path("IacceuilP", views.acceuilP,name="IacceuilP"),
    path("Iconnecter", views.home,name="Iconnecter"),

    #etudiant
    path("IajoutEtu", views.addEtu,name="IajoutEtu"),
    path("IupdateEtu/<int:idetu>", views.updateEtu,name="IupdateEtu"),
    #path("Iform", views.form_ins_etu,name="Iform"),
    path("Ipresent", views.presence,name="Ipresent"),
    path("IcarteEtu", views.carteEtu,name="IcarteEtu"),

    #Enseignant
    #path("IacceuilEns", views.acceuilEns,name="IacceuilEns"),
    #path("IformEns", views.form_ins_ens,name="IformEns"),
    #path("IajoutEns", views.addEns,name="IajoutEns"),
    #path("Idesc", views.ajoutDesc,name="Idesc"),
    #path("Ipres", views.ajoutPres,name="Ipres"),
    #path("IlisteEns", views.listeEns,name="IlisteEns"),
    #path("IupdateEns/<int:idEns>", views.updateEns,name="IupdateEns"),
    
    #Responsable de Scolarite
     #path("IacceuilRes", views.form_ins_etu,name="IacceuilRes"),
    #path("IformReins", views.form_reins,name="IformReins"),
    path("IlisteClasse", views.listeClasse,name="IlisteClasse"),

    #UE
    #path("IlisteUE", views.listeUE,name="listeUE"),

    #EC
    #path("IlisteUE", views.listeEC,name="listeUE"),

] 
