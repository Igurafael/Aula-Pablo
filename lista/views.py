from django.shortcuts import render

def lista(request):
    return render(request, "index.html")
