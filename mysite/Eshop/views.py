from django.shortcuts import render, redirect
from django.http import HttpResponse
from Eshop.models import shop
from Eshop.forms import ItemForm


# Create your views here.

# Function based index view.
# --------------------------------------------------------------------------------
def index(request):
    itemlist = shop.objects.all()
    context = {
        'itemlist':itemlist
    }
    print(itemlist)
    return render(request, 'Eshop/index.html', context)



# Class based index view.
# --------------------------------------------------------------------------------


# Function based detail view.
# --------------------------------------------------------------------------------
def detail(request,item_id):
    item = shop.objects.get(id=item_id)
    context = {
        'item':item
        
    }
    return render(request, 'Eshop/detail.html', context)



# Function based create_item view.
# --------------------------------------------------------------------------------
def create_item(request):

    form = ItemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('Eshop:index')
    
    context={
        'form':form 
    }

    return render(request, 'Eshop/item-form.html', context)




# Function based update_item view.
# --------------------------------------------------------------------------------
def update_item(request, id):

    item = shop.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('Eshop:index')

    context = {
        'form':form

    }

    return render(request, 'Eshop/item-form.html', context)



# Function based delete_item view.
# --------------------------------------------------------------------------------
def delete_item(request, id):

    item = shop.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('Eshop:index')

    context = {
        'item':item

    }

    return render(request, 'Eshop/item-delete.html', context)




def search(request):
    return render(request, 'Eshop/search.html')
   
    







    

