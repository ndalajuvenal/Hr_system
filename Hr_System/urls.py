from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Hr import views
from django.contrib.auth import views

urlpatterns = [
    # Admin
    path('@123/', admin.site.urls,),
    path('', include('Hr.urls')),
    #path('', include('app.urls')),
    #path('', include('django.contrib.auth.urls')),
    path('reset_password/', views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('reset_password_send/', views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
     path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),
   
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)