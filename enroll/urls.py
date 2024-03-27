# authentication_app/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.custom_login, name='login'),
#     path('password_reset/', views.custom_password_reset, name='password_reset'),
#     path('password_reset_done/', views.custom_password_reset_done, name='password_reset_done'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('logout/', views.custom_logout, name='logout'),  # Add this line for logout


# ]

from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in auth views

from enroll import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('view_data/', views.view_data, name='view_data'),
    path('password_reset/', views.custom_password_reset, name='password_reset'),
    path('password_reset_done/', views.custom_password_reset_done, name='password_reset_done'),
    path('logout/', views.custom_logout, name='logout'),  
    # Add Django's built-in password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

