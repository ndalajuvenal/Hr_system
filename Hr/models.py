from django.db import models
from django.urls import reverse
from enum import Enum

class Site(models.Model):
     nom = models.CharField(max_length=250, blank=False, null=False, default="xx")
     description= models.CharField(max_length=250, blank=True, null=True)
     adresse = models.CharField(max_length=250, blank=True, null=True)
     phone=models.CharField(max_length=170, blank=True, null=True)
     email=models.CharField(max_length=170, blank=True, null=True)
     actif = models.BooleanField(default=True)
     class Meta:
        db_table = "site"    
       
     def __str__(self):
         return self.nom
 
    
class Departement(models.Model):
     nom = models.CharField(max_length=250, blank=True, null=True)
     description= models.CharField(max_length=250, blank=True, null=True)
     responsable = models.CharField(max_length=250, blank=True, null=True)
     site= models.ForeignKey(Site, on_delete=models.CASCADE)
     class Meta:
        db_table = "departement"    
       
     def __str__(self):
         return self.nom    
     
    
     
class Categorie(models.Model):
     nom = models.CharField(max_length=250, blank=True, null=True)
     paterson= models.CharField(max_length=250, blank=True, null=True)
     drc = models.CharField(max_length=250, blank=True, null=True)
     salaireBase = models.DecimalField(max_digits=1000,decimal_places=2)
     class Meta:
        db_table = "categorie"    
       
     def __str__(self):
         return self.nom   

class Service(models.Model):
     nom = models.CharField(max_length=250, blank=True, null=True)
     description= models.CharField(max_length=250, blank=True, null=True)
     departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
     class Meta:
        db_table = "service"    
       
     def __str__(self):
         return self.nom      

class Fonction(models.Model):
     nom = models.CharField(max_length=250, blank=True, null=True)
     categorie= models.ForeignKey(Categorie, on_delete=models.CASCADE)
     service = models.ForeignKey(Service, on_delete=models.CASCADE)
     class Meta:
        db_table = "fonction"    
       
     def __str__(self):
         return self.nom 

class GenreChoice(Enum):
    M="Masculin"
    F="Féminin"
    
class CivilChoice(Enum):
    M="Marié"
    C="Célibataire"
    
class StatutChoice(Enum):
    En="Enfant"
    EP="Epoux(se)"  
    PA="Père"
    MA="Mère" 
    PE="Beau Père"
    ME="Belle Mère"       

class Employe(models.Model):
    prenom = models.CharField(max_length=70, blank=True, null=True)
    matricule= models.CharField(max_length=70, blank=False, null=False)
    fonction = models.ForeignKey(Fonction, on_delete=models.DO_NOTHING)
    nom_postnom = models.CharField(max_length=70, blank=False, null=False)
    adresse= models.CharField(max_length=170, blank=True, null=True)
    birthday=models.DateField(blank=False, null=False)
    engagement=models.DateField(blank=False, null=False)
    phone=models.CharField(max_length=170,blank=True, null=True)
    photo = models.ImageField(blank=True, null=True, upload_to='photo/',default='photo/default.png')
    genre = models.CharField(verbose_name="sexe", max_length=1, choices=[(tag.name,tag.value) for tag in GenreChoice])
    actif = models.BooleanField(default=True)
    class Meta:
        db_table = "Employe"

    def __str__(self):
        return self.matricule
    
    def nomComplet(self):
        return self.prenom + " " +self.nom_postnom
    def Calcul_age(self):
        import datetime
        from datetime import date, timedelta
        age = (date.today() - self.birthday) // timedelta(days=365.2425)
        return age
    
    def anciennete(self):
        return self.prenom + " " +self.nom_postnom
    
    def get_absolute_url(self):
        return reverse("MembreFiche", kwargs={"pk": self.pk})
    

class Famille(models.Model):
     prenom = models.CharField(max_length=250, blank=True, null=True)
     employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
     nom_postnom = models.CharField(max_length=70, blank=False, null=False)
     statut = models.CharField(verbose_name="statut", max_length=2, choices=[(tag.name,tag.value) for tag in StatutChoice])
     genre = models.CharField(verbose_name="sexe", max_length=1, choices=[(tag.name,tag.value) for tag in GenreChoice])
     birthday=models.DateField(blank=False, null=False, default = '01/01/2000')
     class Meta:
        db_table = "famille"    
       
     def __str__(self):
         return self.nom_postnom 
     
     def nomComplet(self):
        return self.prenom + " " +self.nom_postnom
     
     def Calcul_age(self):
        import datetime
        from datetime import date, timedelta
        age = (date.today() - self.birthday) // timedelta(days=365.2425)
        return age
     

class Conge(models.Model):
    matricule = models.OneToOneField(Employe, on_delete=models.CASCADE)
    debut=models.DateField(blank=False, null=False)
    duree=models.IntegerField(blank=False, null=False)
    class Meta:
        db_table = "conge"

    def __str__(self):
        return self.nom_postnom
        
        


 
      
     

    
                  