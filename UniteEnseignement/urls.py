from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #########UNITE D'ENSEIGNEMENT

    path("acceuilP", views.acceuilP,name="acceuilP"),
    path("connecter", views.home,name="connecter"),
    ######ANNEE SCOLAIRE
    path("formAn", views.afficherFormAn,name="formAn"),
    path("ajoutAn", views.ajoutAn,name="ajoutAn"),
    #######ANNEE SCOLAIRE
    #######EC
    path("formEC", views.formEC,name="formEC"),
    path("ajoutEC", views.addEC,name="ajoutEC"),
    path("deleteEC/<int:idec>", views.deleteEC,name="deleteEC"),
    path("editEC/<int:idec>", views.editEC,name="editEC"),
    path("updateEC/<int:idec>", views.updateEc,name="updateEC"),
    path("listeEC/<int:idue>", views.listeEC,name="listeEC"),
    path("listerEC", views.listerEC,name="listerEC"),
    #######EC
    #######TYPE COUR
    path("formTC", views.formTC,name="formTC"),
    path("ajoutTC", views.addTC,name="ajoutTC"),
    path("deleteTC/<int:idtc>", views.deleteTC,name="deleteTC"),
    path("editTC/<int:idtc>", views.editTC,name="editTC"),
    path("updateTC/<int:idtc>", views.updateTC,name="updateTC"),
    path("listeTC", views.listeTC,name="listeTC"),
    #######TYPE COUR
    ############UE
    path("formUE", views.formUE,name="formUE"),
    path("ajoutUE", views.addUE,name="ajoutUE"),
    path("deleteUE/<int:idue>", views.deleteUE,name="deleteUE"),
    path("editUE/<int:idue>", views.editUE,name="editUE"),
    path("updateUE/<int:idue>", views.updateUE,name="updateUE"),
    path("listeUE", views.listeUE,name="listeUE"),
    path("listerUE/<int:idue>", views.listerUE,name="listerUE"),
    path("listUE/<int:idsm>", views.listUE,name="listUE"),
    ############UE
    ############Semestre
    path("formSM", views.formSM,name="formSM"),
    path("ajoutSM", views.addSM,name="ajoutSM"),
    path("deleteSM/<int:idsm>", views.deleteSM,name="deleteSM"),
    path("editSM/<int:idsm>", views.editSM,name="editSM"),
    path("updateSM/<int:idsm>", views.updateSM,name="updateSM"),
    path("listeSM", views.listeSM,name="listeSM"),
    
    ############Semestre

    ############Niveau
    path("formNiv", views.formNiv,name="formNiv"),
    path("ajoutNiv", views.addNiv,name="ajoutNiv"),
    path("deleteNiv/<int:idsm>", views.deleteNiv,name="deleteNiv"),
    path("editNiv/<int:idsm>", views.editNiv,name="editNiv"),
    path("updateNiv/<int:idsm>", views.updateNiv,name="updateNiv"),
    path("listeNiv", views.listeNiv,name="listeNiv"),
    ############Niveau


    ############Filiere
    path("formFil", views.formFil,name="formFil"),
    path("ajoutFil", views.addFil,name="ajoutFil"),
    path("deleteFil/<int:idFil>", views.deleteFil,name="deleteFil"),
    path("editFil/<int:idFil>", views.editFil,name="editFil"),
    path("updateFil/<int:idFil>", views.updateFil,name="updateFil"),
    path("listeFil", views.listeFil,name="listeFil"),
    path("niveau/<int:idFil>", views.niveau,name="niveau"),
    path("classic/<int:idFil>", views.lasses,name="classic"),
    ############Filiere 
       
    ############Cycle
    path("formCyc", views.formCyc,name="formCyc"),
    path("ajoutCyc", views.addCyc,name="ajoutCyc"),
    path("deleteCyc/<int:idcyc>", views.deleteFil,name="deleteCyc"),
    path("editCyc/<int:idcyc>", views.editFil,name="editCyc"),
    path("updateCyc/<int:idcyc>", views.updateFil,name="updateCyc"),
    path("listeCyc", views.listeCyc,name="listeCyc"),
    ############Cycle 

    #########RespoFilière
    path("index", views.index,name="index"),
    path("index1", views.index1,name="index1"),
    path("index2", views.index2,name="index2"),
    path("index3", views.index3,name="index3"),
    path("index4", views.index4,name="index4"),
    path("acceuil", views.acceuil,name="acceuil"),
    #########RespoFilière

    #########UNITE D'ENSEIGNEMENT


    ####INSCRIPTION
    #path("IacceuilP", views.acceuilP,name="IacceuilP"),
    #path("Iconnecter", views.home,name="Iconnecter"),

    #etudiant
    path("ajoutEtu", views.addEtu,name="ajoutEtu"),
    path("voirEtu", views.voirEtu,name="voirEtu"),
    #path("IupdateEtu/<int:idetu>", views.updateEtu,name="IupdateEtu"),
    path("Iform", views.form_etu,name="Iform"),
    path("IformReins", views.formVerif,name="IformReins"),
    path("IlisteEtu", views.listeEtu,name="IlisteEtu"),
    #path("Ipresent", views.presence,name="Ipresent"),
    path("IcarteEtu", views.carteEtu,name="IcarteEtu"),
    path("affCarte/<int:idetu>", views.affCarte,name="affCarte"),
    path('export_excel_etu', views.export_excel_etu, name='export_excel_etu'),
    path('export_pdf_etu', views.export_pdf_etu, name='export_pdf_etu'),

    #Enseignant
    #path("IacceuilEns", views.acceuilEns,name="IacceuilEns"),
    path("IformEns", views.form_ins_ens,name="IformEns"),
    path("IajoutEns", views.addEns,name="IajoutEns"),
    #path("Idesc", views.ajoutDesc,name="Idesc"),
    #path("Ipres", views.ajoutPres,name="Ipres"),
    path("IlisteEns", views.listeEns,name="IlisteEns"),
    path("IupdateEns/<int:idEns>", views.updateEns,name="IupdateEns"),
    path('export/excel', views.export_users_xls, name='export_excel'),
    
    #Responsable de Scolarite
    path("acceuilRes", views.form_etu,name="acceuilRes"),
    #path("IlisteClasse", views.listeClasse,name="IlisteClasse"),

    #UE
    #path("IlisteUE", views.listeUE,name="listeUE"),

    #EC
    #path("IlisteUE", views.listeEC,name="listeUE"),

    #######INSCRIPTION
]
    