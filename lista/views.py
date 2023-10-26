from django.shortcuts import render
from .models import Item


def lista(request):
    itens = Item.objects.all()
    context = {'itens':itens}
    return render(request, "index.html", context)
