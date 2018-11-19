from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "user_info/index.html", context=context)


def register(request):
    context = {}
    return render(request, 'user_info/register.html', context=context)


def manage(request):
    context = {}
    return render(request, "user_info/manage.html", context=context)
