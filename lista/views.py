from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


def lista(request):
    itens = Item.objects.all()
    context = {'itens':itens}
    return render(request, "index.html", context)

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = ItemForm()

    context = {'form': form}
    return render(request, "add_item.html", context)

# def add_item(request): 
#     if request.method == 'POST':
#         form = ItemForm()
#         context = {'form':form}
#         return render(request, "add_item.html", context)