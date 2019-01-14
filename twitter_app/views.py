from django.shortcuts import render


# Create your views here.
def baseindexview(request):
    context = {}
    return render(request, "accounts/login.html", context)


def dashboard_view(request):
    context = {}
    return render(request, "home/index.html", context)


def timeline_view(request):
    context = {}
    return render(request, "accounts/detail.html", context)