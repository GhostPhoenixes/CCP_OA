from django.shortcuts import render
from .models import User


def index(request):
    context = {}
    return render(request, "user_info/index.html", context=context)


def register(request):
    context = {}
    if request.method == "GET":
        return render(request, 'user_info/register.html', context=context)
    else:
        username = request.POST['username']
        e_mail = request.POST['email']
        password = request.POST['username']
        real_name = request.POST['username']
        student_id = request.POST['student_id']
        new_user = User(
            username = username,
            e_mail=e_mail,
            password=password,
            real_name=real_name,
            student_id=student_id,
        )


def manage(request):
    context = {}
    return render(request, "user_info/manage.html", context=context)
