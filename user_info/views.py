from django.shortcuts import render


# Create your views here.
def register(request):
    context = {}
    return render(request, 'user_info/register.html', context=context)
