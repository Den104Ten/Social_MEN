from django.urls import path
from .views import *



urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('full_post/<int:pk>/', FullPost.as_view(), name='full_post'),
]

