from django.shortcuts import render, HttpResponseRedirect
from .models import User


def index(request):
    context = {}
    return render(request, "user_info/index.html", context=context)


def manage(request):
    context = {}
    return render(request, "user_info/manage.html", context=context)
