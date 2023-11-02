from django.shortcuts import render
from .models import Item
from .forms import ItemForm


def lista(request):
    itens = Item.objects.all()
    context = {'itens':itens}
    return render(request, "index.html", context)

def add_item(request): 
    if request.method == 'GET':
        form = ItemForm()
        context = {'form':form}
        return render(request, "add_item.html", context)