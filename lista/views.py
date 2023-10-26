from django.shortcuts import render
from .models import Item


""" def lista(request):
    itens = Item.objects.all()
    context = {'itens':itens}
    return r """ender(request, "index.html", context)
