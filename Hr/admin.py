from django.contrib import admin
from .models import *

# Register your models here.
class AdminSite(admin.ModelAdmin):
    list_display =  ('nom','description','adresse','phone','email','actif')
admin.site.register(Site, AdminSite)

class AdminDepartement(admin.ModelAdmin):
    list_display =  ('nom','description','responsable','site')
admin.site.register(Departement, AdminDepartement)

class AdminService(admin.ModelAdmin):
    list_display =  ('nom','description','departement')
admin.site.register(Service, AdminService)

class AdminFonction(admin.ModelAdmin):
    list_display =  ('nom','categorie','service')
admin.site.register(Fonction, AdminFonction)

class AdminCategorie(admin.ModelAdmin):
    list_display =  ('nom','paterson','drc','salaireBase')
admin.site.register(Categorie, AdminCategorie)

class AdminEmploye(admin.ModelAdmin):
   list_display  = [f.name for f in Employe._meta.fields]
admin.site.register(Employe, AdminEmploye)

class AdminFamille(admin.ModelAdmin):
   list_display  = [f.name for f in Famille._meta.fields]
admin.site.register(Famille, AdminFamille)
