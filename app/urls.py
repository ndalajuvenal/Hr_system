
from django.urls import path
from Hr import views
from django.contrib.auth import views
app_name='app'
urlpatterns = [
    #path('reset_password/', views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    #path('reset_password_send/', views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'), name='password_reset_done'),
    #path('reset_password_complete/', views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name='password_reset_complete'),
    #path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'), name='password_reset_confirm'),
]