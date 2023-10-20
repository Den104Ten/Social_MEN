from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib.auth import authenticate, login
from django.views import View
from .models import User, Post
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.mail import send_mail


# ---- Обработка неверного маршрута ---------------------------------------------------------------------------------- #

def page_not_found(request, exception):
    """Функция перенаправляет на страницу с информацией, что нет такого маршрута. Если отладка выключена."""
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

# --^-- Обработка неверного маршрута ----------^--------------------------------------^-------------------------^----- #


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



# Функция для отправки письма

# Сделать код действительным в течении трех минут, так как у разных пользователей разные коды
import time
from random import randrange

def generate_new_code():
    return randrange(1000, 9999)

new_code = generate_new_code()  # Вообщем проверка работает, но код теперь не обновляется.

def send_email(email):
    # Теперь каждый раз код обновляется. Но теперь надо понять возможно ли будет проводить проверку на другой страничке путем вызова этой переменной
    subject = 'Восстановление пароля'
    message = f'Код для входа в аккаунт: {new_code}'
    from_email = 'mediaspacehelp@gmail.com'
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)


class ResetPasswordView(View):

    def get(self, request):
        return render(request, 'main_app/Password_Reset.html')


    def post(self, request):
        email = request.POST['email_password_reset']
        try:
            if User.objects.get(email=email):
                send_email(email)
                return redirect('check_reset_password')  # здесь нужно перенаправить на страницу подтверждения кода из письма и проверить
            else:
                # потом сделать, динамическую переменную для вывода информации о том, что пользователя с такой почты нет
                return redirect('login')
        except ObjectDoesNotExist:
            return redirect('login')
        except MultipleObjectsReturned:
            return redirect('login')


class CheckResetPassword(View):

    def get(self, request):
        return render(request, 'main_app/Password_CheckReset.html')

    def post(self, request):
        code = request.POST['check_password_reset']  # не работает так как функция просто вызывается второй раз, а нужно как-то сохранить значение
        if str(code) == str(new_code):
            return redirect('home')
        else:
            return redirect('login')





# --- Далее все что связано со страничкой Home ----------------------------------------------------------------------- #

class HomeView(View):

    def get(self, request):
        posts = Post.objects.filter(is_published=True)
        # Передаю все посты шаблону главной страницы
        return render(request, 'main_app/home.html', context={'posts': posts})


class FullPostView(View):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'main_app/full_post_view.html', {'post': post})





# -----------------------------------------Часть функционала для будущего--------------------------------------------- #

"""class HomeView(View):
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
        return render(request, 'main_app/full_post.html', {'post': post})"""

