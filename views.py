from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    items = Item.objects.all().order_by('-id')[:5]
    context={
        'items':items,
    }
    return render(request,'crudsite/index.html',context)

def createItem(request):
    if request.method =='POST':
        # first we make the form to be displayed
        form = ItemForm(request.POST)
        if form.is_valid():
            # Get the form variables from the form
            it_name = request.POST.get('name')
            item = Item(name = it_name)
            # We save the Object to database
            item.save()
            # redirect to the page that contain the database items
            return HttpResponseRedirect( reverse('crudsite:index'))# this reverse address has a namespace prefix
    else:
        form = ItemForm()
        # if its a GET call we will show the form
        return render(request,'crudsite/create_item.html',{'form':form})

def updateItem(request,item_id):

    item = Item.objects.get(pk = item_id)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        # first we make the form to be displayed
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form' : form}
    return render(request,'crudsite/update_item.html',context)

def deleteItem(request,item_id):
    item = Item.objects.get(pk=item_id)
    #item.delete()
    #return redirect('/')
    if request.method =='POST':
        item.delete()
        return redirect('/')
    return render(request,'crudsite/delete_item.html',{'item':item})