from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View
from .models import User, Post
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

class RegistrationView(View):
    universal_text = 'Страница регистрации'

    def get(self, request):
        context = {'universal_text': RegistrationView.universal_text}
        return render(request, 'main_app/registration.html', context=context)  # разобраться с этим моментом

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            if User.objects.get(username=username, password=password, email=email):
                return redirect('home')  # пользователь уже существует отправляем на страничку home
        except ObjectDoesNotExist:
            User.objects.create(username=username, password=password, email=email)
            return redirect('login')  # Перенаправление на страницу входа
        except MultipleObjectsReturned:
            User.objects.create(username=username, password=password, email=email)
            return redirect('login')  # Перенаправление на страницу входа

class LoginView(View):
    universal_text_login = 'Страница входа'

    def get(self, request):
        context = {'universal_text_login': LoginView.universal_text_login}
        return render(request, 'main_app/login.html', context=context)  # нужен метод, чтобы вызывать его в других классах

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            if User.objects.get(username=username) and User.objects.get(password=password):
                return redirect('home')
            else:
                return redirect('register')
        except ObjectDoesNotExist:
            return redirect('register')
        except MultipleObjectsReturned:
            return redirect('register')


class HomeView(View):
    def get(self, request):
        posts = Post.objects.all()

        return render(request, 'main_app/home.html', {'posts': posts})


class ProfileView(View):
    def get(self, request):
        return render(request, 'main_app/profile.html')


class CreatePost(View):
    def get(self, request):
        return render(request, 'main_app/create_post.html')

    def post(self, request):
        title = request.POST['title']
        body = request.POST['body']
        Post.objects.create(title=title, body=body)
        return redirect('home')

class FullPost(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'main_app/full_post.html', {'post': post})

