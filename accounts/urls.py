from django.urls import path, include
from django.contrib.auth import views as auth

from . import views

#app_name = "accounts"

urlpatterns = [
               path('logout/', auth.LogoutView.as_view(), name='logout'),
               path('profile/', views.redirect_to_user_details, name='redirect-user-details'),
               path('profile/<pk>/', views.UserDetails.as_view(), name='user-details'),
               path('edit/<pk>/', views.UserEdit.as_view(), name='user-edit'),
               path('signup/', views.SignUp.as_view(), name='signup'),
               path('login/', views.LogIn.as_view(template_name='login.html'), name='login'),
               path('change_password/', auth.PasswordChangeView.as_view(template_name='change-pass.html'),
                    name='password_change'),
               path('change_password/done/', auth.PasswordChangeDoneView.as_view(template_name='change-pass-done.html'),
                    name='password_change_done'),
               path('reset_password/', auth.PasswordResetView.as_view(template_name='reset-pass.html'),
                    name='password_reset'),
               path('reset_password/done/', auth.PasswordResetDoneView.as_view(template_name='reset-pass-done.html'),
                    name='password_reset_done'),
               path('reset_password/<uidb64>/<token>/',
                    auth.PasswordResetConfirmView.as_view(template_name='reset-pass-confirm.html'),
                    name='password_reset_confirm'),
               path('reset_password/complete/',
                    auth.PasswordResetCompleteView.as_view(template_name='reset-pass-complete.html'),
                    name='password_reset_complete'),

               ]