from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, "journey/index.html", context=context)


def course(request):
    context = {}
    return render(request, "journey/index.html", context=context)


def document(request):
    context = {}
    return render(request, "journey/index.html", context=context)


def course_manage(request):
    context = {}
    return render(request, "journey/manage.html", context=context)


def document_manage(request):
    context = {}
    return render(request, "journey/manage.html", context=context)
