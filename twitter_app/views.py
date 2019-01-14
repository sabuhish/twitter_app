from django.shortcuts import render


# Create your views here.
def baseindexview(request):
    context = {}
    return render(request, "accounts/login.html", context)
