from django.shortcuts import render, HttpResponseRedirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    return render(request, "user_info/index.html", context=context)


def auth(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            context['error'] = "用户名或密码错误"
            return render(request, "main_site/error.html", context=context)
    else:
        return render(request, 'user_info/login.html', context=context)


def register(request):
    context = {}
    if request.method == "GET":
        return render(request, 'user_info/register.html', context=context)
    else:
        username = request.POST['username']
        e_mail = request.POST['email']
        password = request.POST['password']
        real_name = request.POST['username']
        student_id = request.POST['student_id']
        new_user = User.objects.create_user(
            username=username,
            email=e_mail,
            password=password,
            real_name=real_name,
            student_id=student_id,
        )
        new_user.save()
        return HttpResponseRedirect("/user_info/login")


def manage(request):
    context = {}
    return render(request, "user_info/manage.html", context=context)
