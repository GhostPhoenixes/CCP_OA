from django.shortcuts import render, HttpResponseRedirect
from user_info.models import User


def index(request):
    context = {}
    return render(request, "main_site/index.html", context=context)


def login(request):
    context = {}
    if request.method == "GET":
        return render(request, 'main_site/login.html', context=context)
    else:
        username = request.POST['username']
        e_mail = request.POST['email']
        password = request.POST['username']
        real_name = request.POST['username']
        student_id = request.POST['student_id']
        new_user = User(
            username=username,
            e_mail=e_mail,
            password=password,
            real_name=real_name,
            student_id=student_id,
        )
        new_user.save()
        return HttpResponseRedirect("/")


def register(request):
    context = {}
    if request.method == "GET":
        return render(request, 'main_site/register.html', context=context)
    else:
        username = request.POST['username']
        e_mail = request.POST['email']
        password = request.POST['username']
        real_name = request.POST['username']
        student_id = request.POST['student_id']
        new_user = User(
            username=username,
            e_mail=e_mail,
            password=password,
            real_name=real_name,
            student_id=student_id,
        )
        new_user.save()
        return HttpResponseRedirect("/")


def manage(request):
    context = {}
    return render(request, "main_site/index.html", context=context)
