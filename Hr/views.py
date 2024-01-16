from typing import Any, Dict, Optional
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.db.models import Sum
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.forms.forms import BaseForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # Login required to access private pagas
from django.views.decorators.cache import cache_control # Prevent back button (destroy the last section)
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.db.models import Sum
from .forms import *
from .models import *
from django.views.generic import TemplateView, DeleteView, CreateView, View, DetailView, UpdateView, ListView
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.http import Http404, FileResponse
from django.db.models import Q,Value as V
from django.db.models.functions import Concat
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import template 
from django.contrib.contenttypes.models import ContentType
#from .mixins import CheckPremiumGroupMixin
from tablib import Dataset
import datetime
import csv
import io

from django.shortcuts import render,HttpResponse,redirect
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes , force_text
from django.contrib.auth.models import User
from django.contrib import messages
from Hr_System import settings
from django.core.mail import send_mail, EmailMessage
from Hr.token import generatorToken

# Create your views here.

# Register and Login
def register(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if User.objects.filter(username = username):
            messages.error(request, "ce nom utilisateur est deja pris")
            return redirect('register')
        if User.objects.filter(email = email):
            messages.error(request, "cet email  est deja pris")
            return redirect('register') 
        #if not username.isalnum():
           # messages.error(request, "le nom utilisateur doit etre alphanumerique")
            #return redirect('register') 
        if password != password1:
            messages.error(request, "les mots de passe ne correspondent pas")
            return redirect('register')
        
        mon_utilisateur = User.objects.create_user(username, email, password )
        mon_utilisateur.first_name = firstname
        mon_utilisateur.last_name = lastname
        mon_utilisateur.is_active = False
        mon_utilisateur.save()
        messages.success (request, 'votre compte a ete crees avec success')
        subject = "bienvenu sur l'application d'authentification "
        message = "Bienvenu"+ " "+mon_utilisateur.first_name+" "+mon_utilisateur.last_name+" \n nous sommes heureux de vous compter parmi nous\n\n\n Merci \n\n juvenal"
        from_email = settings.EMAIL_HOST_USER
        to_list = [mon_utilisateur.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        #email de confirmation
        current_site = get_current_site(request)
        email_subject = "confirmation de l'adresse email "
        messageConfirm = render_to_string( "emailconfirm.html", {
            "name":mon_utilisateur.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(mon_utilisateur.pk)),
            'token': generatorToken.make_token(mon_utilisateur)
        })
        email = EmailMessage(
            email_subject,
            messageConfirm,
            settings.EMAIL_HOST_USER,
            [mon_utilisateur.email]           
        )
        email.fail_silently = False
        email.send()
        return redirect('Auth_login')
    return render(request, 'register.html')

def Auth_login(request):  
       if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('accueuil')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
       return render (request,'login.html')   
        
       

def logOut(request):  
    logout(request)
    messages.success(request, 'deconnecter avec success')
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
        
    if user is not None   and generatorToken.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "votre compte a ete active avec success, connectez-vous maintenant")      
        return redirect('Auth_login')
    else:
        messages.error(request, " l'activation a echoue ")
        return redirect('home')



def base(request):  
    return render(request, 'base.html')
def accueuil(request):  
    return render(request, 'accueuil.html')


def site(request):  
    return render(request, 'site_create.html')

def home(request):  
    return render(request, 'home.html')



#site
class siteDelete(DeleteView):
    template_name="site_delete.html"
    queryset = Site.objects.all()
    success_message = 'bravo...deleted ...'
    success_url=reverse_lazy('siteList') 

    
class siteUpdate(SuccessMessageMixin, UpdateView):
    model = Site
    form_class = SiteForm
    template_name="site_update.html"  
    success_message = 'bravo... %(nom)s mis à jour avec succes ...'
    success_url=reverse_lazy('siteList') 

class siteDetail(DetailView):
    template_name="site_detail.html"
    queryset = Site.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Site, pk = id_)

@login_required(login_url='Auth_login')
def siteList(request):
    queryset=Site.objects.all().order_by('nom')       
    paginator = Paginator(queryset, 4)
    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)
    
    context = {
        "queryset" : queryset,
         "header" : "liste des sites",
    }
    
    return render(request, "siteList.html", context)

def site_form(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "site ajouté avec succès")
            return redirect('siteList')

    else:
        form = SiteForm()
    context = {
        'form': form
    }
    return render(request, 'site_create.html', context)

#departement
class departementDelete(DeleteView):
    template_name="departement_delete.html"
    queryset = Departement.objects.all()
    success_message = 'bravo...deleted ...'
    success_url=reverse_lazy('departementList') 
    
class departementUpdate(SuccessMessageMixin,UpdateView):
    model = Departement
    form_class = DepartementForm
    template_name="departement_update.html"  
    success_message = 'bravo... %(nom)s mis à jour avec succes ...'
    success_url=reverse_lazy('departementList') 
    
class departementDetail(DetailView):
    template_name="departement_detail.html"
    queryset = Departement.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Departement, pk = id_)
    
def departement_form(request):
    if request.method == 'POST':
        form = DepartementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "departement ajouté avec succès")
            return redirect('departementList')

    else:
        form = DepartementForm()
    context = {
        'form': form
    }
    return render(request, 'departement_create.html', context)

def departementList(request):
    queryset=Departement.objects.all().order_by('-id')       
    paginator = Paginator(queryset, 4)
    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)
    
    context = {
        "queryset" : queryset,
         "header" : "liste des departements",
    }
    
    return render(request, "departementList.html", context)

#service
class serviceDelete(DeleteView):
    template_name="service_delete.html"
    queryset = Service.objects.all()
    success_message = 'bravo...deleted ...'
    success_url=reverse_lazy('serviceList') 
    
class serviceUpdate(SuccessMessageMixin,UpdateView):
    model = Service
    form_class = ServiceForm
    template_name="service_update.html"  
    success_message = 'bravo... %(nom)s mis à jour avec succes ...'
    success_url=reverse_lazy('serviceList') 

class serviceDetail(DetailView):
    template_name="service_detail.html"
    queryset = Service.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Service, pk = id_)
    
def service_form(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "service ajouté avec succès")
            return redirect('serviceList')

    else:
        form = ServiceForm()
    context = {
        'form': form
    }
    return render(request, 'service_create.html', context)

def serviceList(request):
     if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "service ajouté avec succès")
            return redirect('serviceList')

     else:
        form = ServiceForm()
 
    
    
     queryset=Service.objects.all().order_by('-id')       
     paginator = Paginator(queryset, 4)
     page_number = request.GET.get('page')
     queryset = paginator.get_page(page_number)
    
     context = {
        "queryset" : queryset,
         "header" : "liste des services",
           'form': form
    }
    
     return render(request, "serviceList.html", context)


#fonctions
class fonctionDelete(DeleteView):
    template_name="fonction_delete.html"
    queryset = Fonction.objects.all()
    success_message = 'bravo...deleted ...'
    success_url=reverse_lazy('fonctionList') 
    
class fonctionUpdate(SuccessMessageMixin,UpdateView):
    model = Fonction
    form_class = FonctionForm
    template_name="fonction_update.html"  
    success_message = 'bravo... %(nom)s mis à jour avec succes ...'
    success_url=reverse_lazy('fonctionList') 

class fonctionDetail(DetailView):
    template_name="fonction_detail.html"
    queryset = Fonction.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Fonction, pk = id_)
    
def fonction_form(request):
    if request.method == 'POST':
        form = FonctionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "fonction ajouté avec succès")
            return redirect('fonctionList')

    else:
        form = FonctionForm()
    context = {
        'form': form
    }
    return render(request, 'fonction_create.html', context)

def fonctionList(request):
    queryset=Fonction.objects.all().order_by('-id')       
    paginator = Paginator(queryset, 4)
    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)
    
    context = {
        "queryset" : queryset,
         "header" : "liste des fonctions",
    }
    
    return render(request, "fonctionList.html", context)

#categorie
class categorieDelete(DeleteView):
    template_name="categorie_delete.html"
    queryset = Categorie.objects.all()
    success_message = 'bravo...deleted ...'
    success_url=reverse_lazy('categorieList') 
    
class categorieUpdate(SuccessMessageMixin,UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name="categorie_update.html"  
    success_message = 'bravo... %(nom)s mis à jour avec succes ...'
    success_url=reverse_lazy('categorieList') 

class categorieDetail(DetailView):
    template_name="categorie_detail.html"
    queryset = Categorie.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Categorie, pk = id_)
    
def categorie_form(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "catégorie ajouté avec succès")
            return redirect('categorieList')

    else:
        form = CategorieForm()
    context = {
        'form': form
    }
    return render(request, 'categorie_create.html', context)
#def is_editor(user):
    #return user.groups.filter(name="G1").exists()

#editor_required = user_passes_test(is_editor)

#@editor_required
from .decorators import group_required
@group_required('G1')
def categorieList(request):
    #if request.user.groups.filter(name='G1').exists():
       queryset=Categorie.objects.all().order_by('-id')       
       paginator = Paginator(queryset, 4)
       page_number = request.GET.get('page')
       queryset = paginator.get_page(page_number)
    
       context = {
        "queryset" : queryset,
         "header" : "liste des catégories",
        }
    
       return render(request, "categorieList2.html", context)
    #else:
       #return HttpResponse('<h1> Vous n\' avez pas le droit requis pour voir les categories')
    
  

#employe
class employeDelete(DeleteView):
    template_name="employe_delete.html"
    queryset = Employe.objects.all()
    success_message = 'bravo...deleted ...'
    success_url=reverse_lazy('employeList') 
    
class employeUpdate(SuccessMessageMixin,UpdateView):
    model = Employe
    form_class = EmployeForm
    template_name="employe_update.html"  
    success_message = 'bravo... %(prenom)s mis à jour avec succes ...'
    success_url=reverse_lazy('employeList') 
    def get_form(self):
        form = super().get_form()
        #form.fields['birthday'].widget.input_type = 'date'
        #form.fields['engagement'].widget.input_type = 'date'
        return form

class employeDetail(DetailView):
    template_name="employe_detail.html"
    queryset =Employe .objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Employe, pk = id_)
    
class employe_form(SuccessMessageMixin,CreateView):
    form_class = EmployeForm
    template_name="employe_create.html"
    queryset =Employe.objects.all()
    success_message = 'bravo... %(prenom)s enregistré  avec succes ...'
    success_url=reverse_lazy('employeList') 
   
    def get_form(self):
        form = super().get_form()
        form.fields['birthday'].widget.input_type = 'date'
        form.fields['engagement'].widget.input_type = 'date'
        return form
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

def employeList(request):
    
     if request.method == 'POST':
        form = EmployeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "employe ajouté avec succès")
            return redirect('employeList')

     else:
         form = EmployeForm()
     queryset=Employe.objects.all().order_by('-id')       
     paginator = Paginator(queryset, 4)
     page_number = request.GET.get('page')
     queryset = paginator.get_page(page_number)
    
     context = {
        "queryset" : queryset,
         "header" : "liste des employés",
          'form': form,
    }
    
     return render(request, "employeList2.html", context)

#famille
class familleDelete(DeleteView):
    template_name="famille_delete.html"
    queryset = Famille.objects.all()
    success_message = 'bravo...deleted ...'
    success_url=reverse_lazy('familleList') 
    
class familleUpdate(SuccessMessageMixin,UpdateView):
    model = Famille
    form_class = FamilleForm
    template_name="famille_update.html"  
    success_message = 'bravo... %(nom_postnom)s mis à jour avec succes ...'
    success_url=reverse_lazy('familleList') 
    def get_form(self):
        form = super().get_form()
        #form.fields['birthday'].widget.input_type = 'date'
        #form.fields['engagement'].widget.input_type = 'date'
        return form

class familleDetail(DetailView):
    template_name="famille_detail.html"
    queryset =Famille .objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Famille, pk = id_)
    
class famille_form(SuccessMessageMixin,CreateView):
    form_class = FamilleForm
    template_name="famille_create.html"
    queryset =Famille.objects.all()
    success_message = 'bravo... %(nom_postnom)s enregistré  avec succes ...'
    success_url=reverse_lazy('familleList') 
   
    def get_form(self):
        form = super().get_form()
        form.fields['birthday'].widget.input_type = 'date'
        return form
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

def familleList(request):
    queryset=Famille.objects.all().order_by('-id')       
    paginator = Paginator(queryset, 4)
    page_number = request.GET.get('page')
    queryset = paginator.get_page(page_number)
    
    context = {
        "queryset" : queryset,
         "header" : "liste des familles",
    }
    
    return render(request, "familleList.html", context)











