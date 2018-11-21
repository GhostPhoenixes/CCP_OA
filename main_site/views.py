from django.shortcuts import render, HttpResponseRedirect
from user_info.models import User
from django.contrib.auth.decorators import login_required

context = {}


def index(request):
    context['user'] = request.user
    return render(request, "main_site/index.html", context=context)


def manage(request):
    context = {}
    return render(request, "main_site/index.html", context=context)
