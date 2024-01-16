from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *

class SiteForm(forms.ModelForm):
      class Meta:
        model = Site
        fields = '__all__'
        widgets = {
                'nom':forms.TextInput(attrs={
                    'class':'form-control input name','autocomplete': 'off','placeholder':'denommination', 'required':'true'
               }),
                'description':forms.TextInput(attrs={
                   'class':'form-control input description','autocomplete': 'off','placeholder':'description', 'required':'true'
               }),
                   'adresse':forms.TextInput(attrs={
                    'class':'form-control input adresse','autocomplete': 'off','placeholder':'adresse', 'required':'true'
               }),
                'phone':forms.TextInput(attrs={
                   'class':'form-control input phone','autocomplete': 'off','placeholder':'phone', 'required':'true','type':'number'
               }),
                   'email':forms.TextInput(attrs={
                    'class':'form-control input email','autocomplete': 'off','placeholder':'email', 'required':'true','type':'email'
               }),
                'actif':forms.CheckboxInput(attrs={
                  
               }),

        }
      
      
      def __init__(self, *args, **kwargs):
        super(SiteForm, self).__init__(*args, **kwargs) 
        


class DepartementForm(forms.ModelForm):
      class Meta:
        model = Departement
        fields = '__all__'
        widgets = {
                'nom':forms.TextInput(attrs={
                    'class':'form-control input name','autocomplete': 'off','placeholder':'denommination', 'required':'true'
               }),
                'description':forms.TextInput(attrs={
                   'class':'form-control input description','autocomplete': 'off','placeholder':'description', 'required':'true'
               }),
                   'responsable':forms.TextInput(attrs={
                    'class':'form-control input adresse','autocomplete': 'off','placeholder':'responsable', 'required':'true'
               }),
                'site':forms.Select(attrs={
                   'class':'form-control'
               }),
                 

        }
      
      
      def __init__(self, *args, **kwargs):
        super(DepartementForm, self).__init__(*args, **kwargs) 
        
        
class ServiceForm(forms.ModelForm):
      class Meta:
        model = Service
        fields = '__all__'
        widgets = {
                'nom':forms.TextInput(attrs={
                    'class':'form-control input name','autocomplete': 'off','placeholder':'denommination', 'required':'true'
               }),
                'description':forms.TextInput(attrs={
                   'class':'form-control input description','autocomplete': 'off','placeholder':'description', 'required':'true'
               }),
                'departement':forms.Select(attrs={
                   'class':'form-control'
               }),
                 

        }    
      def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs) 
        
class FonctionForm(forms.ModelForm):
      class Meta:
        model = Fonction
        fields = '__all__'
        widgets = {
                'nom':forms.TextInput(attrs={
                    'class':'form-control input name','autocomplete': 'off','placeholder':'denommination', 'required':'true'
               }),
                'categorie':forms.Select(attrs={
                   'class':'form-control'
               }),
                  'service':forms.Select(attrs={
                   'class':'form-control'
               }),
        }    
      def __init__(self, *args, **kwargs):
        super(FonctionForm, self).__init__(*args, **kwargs)      
        
class CategorieForm(forms.ModelForm):
      class Meta:
        model = Categorie
        fields = '__all__'
        widgets = {
                'nom':forms.TextInput(attrs={
                    'class':'form-control input name','autocomplete': 'off','placeholder':'denommination', 'required':'true'
               }),
                'paterson':forms.TextInput(attrs={
                    'class':'form-control input name','autocomplete': 'off','placeholder':'paterson', 'required':'true'
               }),
               'drc':forms.TextInput(attrs={
                    'class':'form-control input name','autocomplete': 'off','placeholder':'classification DRC', 'required':'true'
               }),
                'salaireBase':forms.NumberInput(attrs={
                    'class':'form-control  name','autocomplete': 'off','placeholder':'salaire de base', 'required':'true','type':'number'
               }),
        }    
      def __init__(self, *args, **kwargs):
        super(CategorieForm, self).__init__(*args, **kwargs)        
        
class EmployeForm(forms.ModelForm):
      class Meta:
        model = Employe
        fields = '__all__'   
        widgets = {
                'actif':forms.CheckboxInput(attrs={                 
               }),
               'matricule':forms.TextInput(attrs={
                    'class':'form-control input name','autocomplete': 'off','placeholder':'matricule', 'required':'true'
               }),
                  'prenom':forms.TextInput(attrs={
                    'class':'form-control input name','autocomplete': 'off','placeholder':'prenom', 'required':'true'
               }),
               'nom_postnom':forms.TextInput(attrs={
                    'class':'form-control','autocomplete': 'off','placeholder':'nom_postnom', 'required':'true'
               }),
                'fonction':forms.Select(attrs={
                    'class':'form-control  name','autocomplete': 'off',
               }),
                      'adresse':forms.TextInput(attrs={
                    'class':'form-control','autocomplete': 'off','placeholder':'adresse', 'required':'true'
               }),
                  'birthday':forms.DateInput(attrs={
                    'class':'form-control','type':'date'
               }),
                  
               'engagement':forms.DateInput(attrs={
                    'class':'form-control','type':'date'
               }),
                'phone':forms.TextInput(attrs={
                    'class':'form-control input phone','autocomplete': 'off','placeholder':'numéro de téléphone', 'required':'true','type':'number'
               }),
                'photo':forms.FileInput(attrs={
                    'class':''
               }),
                'genre':forms.Select(attrs={
                    'class':'form-control  name','autocomplete': 'off',
               }),
                

        }
      def __init__(self, *args, **kwargs):
        super(EmployeForm, self).__init__(*args, **kwargs)     
        
class FamilleForm(forms.ModelForm):
      class Meta:
        model = Famille
        fields = '__all__'   
        widgets = {
               'employe':forms.Select(attrs={
                    'class':'form-control', 'required':'true'
               }),
                  'prenom':forms.TextInput(attrs={
                    'class':'form-control input name','autocomplete': 'off','placeholder':'prenom', 'required':'true'
               }),
               'nom_postnom':forms.TextInput(attrs={
                    'class':'form-control','autocomplete': 'off','placeholder':'nom_postnom', 'required':'true'
               }),
                  'birthday':forms.DateInput(attrs={
                    'class':'form-control',
               }),
                'genre':forms.Select(attrs={
                    'class':'form-control ','autocomplete': 'off',
               }),
                'statut':forms.Select(attrs={
                    'class':'form-control  ','autocomplete': 'off',
               }),
                
        }
      def __init__(self, *args, **kwargs):
        super(FamilleForm, self).__init__(*args, **kwargs)        
             
                
            