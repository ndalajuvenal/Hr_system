from django.urls import path
from . import views
from .views import  *
#from django.contrib.auth import views

#from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView



urlpatterns = [
    path('register/', views.register, name='register'),
    path('Auth_login/', views.Auth_login, name='Auth_login'),
    path('logout/', views.logOut, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
   
    
    
    path('', views.home, name='home'),
    path('accueuil/', views.accueuil, name='accueuil'),
    #site
    path('site/', views.site_form,name='site'),
    path('siteList', views.siteList, name='siteList'),
    path('siteDetail/<int:pk>/', siteDetail.as_view(), name="siteDetail"),
    path('siteUpdate<int:pk>/', siteUpdate.as_view(), name="siteUpdate"),
    path('siteDelete/<int:pk>/', siteDelete.as_view(), name="siteDelete"),
    #departement
    path('departement/', views.departement_form,name='departement'),
    path('departementList', views.departementList, name='departementList'),
    path('departementDetail/<int:pk>/', departementDetail.as_view(), name="departementDetail"),
    path('departementUpdate<int:pk>/', departementUpdate.as_view(), name="departementUpdate"),
    path('departementDelete/<int:pk>/', departementDelete.as_view(), name="departementDelete"),
    #service
    path('service/', views.service_form,name='service'),
    path('serviceList', views.serviceList, name='serviceList'),
    path('serviceDetail/<int:pk>/', serviceDetail.as_view(), name="serviceDetail"),
    path('serviceUpdate<int:pk>/', serviceUpdate.as_view(), name="serviceUpdate"),
    path('serviceDelete/<int:pk>/', serviceDelete.as_view(), name="serviceDelete"),
    #fonction
    path('fonction/', views.fonction_form,name='fonction'),
    path('fonctionList', views.fonctionList, name='fonctionList'),
    path('fonctionDetail/<int:pk>/', fonctionDetail.as_view(), name="fonctionDetail"),
    path('fonctionUpdate<int:pk>/', fonctionUpdate.as_view(), name="fonctionUpdate"),
    path('fonctionDelete/<int:pk>/', fonctionDelete.as_view(), name="fonctionDelete"),
    #categorie
    path('categorie/', views.categorie_form,name='categorie'),
    path('categorieList', views.categorieList, name='categorieList'),
    path('categorieDetail/<int:pk>/', categorieDetail.as_view(), name="categorieDetail"),
    path('categorieUpdate<int:pk>/', categorieUpdate.as_view(), name="categorieUpdate"),
    path('categorieDelete/<int:pk>/', categorieDelete.as_view(), name="categorieDelete"),
    #employe
    path('employe/', views.employe_form.as_view(),name='employe'),
    path('employeList', views.employeList, name='employeList'),
    path('employeDetail/<int:pk>/', employeDetail.as_view(), name="employeDetail"),
    path('employeUpdate<int:pk>/', employeUpdate.as_view(), name="employeUpdate"),
    #path('site/', views.site_form,name='site'),
    #path('employeUpdate<int:id>/', views.employe_update, name="employeUpdate"),
    path('employeDelete/<int:pk>/', employeDelete.as_view(), name="employeDelete"),
    
     #famille
    path('famille/', views.famille_form.as_view(),name='famille'),
    path('familleList', views.familleList, name='familleList'),
    path('familleDetail/<int:pk>/', familleDetail.as_view(), name="familleDetail"),
    path('familleUpdate<int:pk>/', familleUpdate.as_view(), name="familleUpdate"),
    path('familleDelete/<int:pk>/', familleDelete.as_view(), name="familleDelete"),
]