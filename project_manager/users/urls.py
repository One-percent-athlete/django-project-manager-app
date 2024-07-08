from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('update_profile', views.update_profile, name ='update-profile'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name = 'password-reset.html'), name='password-reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password-reset-done.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password-reset.html'), name = 'password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password-reset-complete.html'), name = 'password_reset_complete'),
]