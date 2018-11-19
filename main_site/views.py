from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "main_site/index.html", context=context)


def manage(request):
    context = {}
    return render(request, "main_site/manage.html", context=context)
