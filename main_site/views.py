from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "index.html", context=context)


def manage(request):
    context = {}
    return render(request, "manage.html", context=context)
