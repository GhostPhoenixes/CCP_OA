from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "activity/index.html", context=context)


def manage(request):
    context = {}
    return render(request, "activity/manage.html", context=context)
