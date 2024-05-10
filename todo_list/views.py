from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import List
from .forms import Listform

# what kind they are

def home(request): #whenever the web server calls the webpg. it is requesting that web pg. we need to pass tat req into our func here
    
    if request.method == 'POST':
        form = Listform(request.POST or None)


        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Items added successfully!!'))
            return render(request, 'home.html', {'all_items': all_items})


    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

       

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Items deleted successfully!!'))
    return redirect('home')


def cross_off(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed =True
    item.save()
    return redirect('home')


def uncross(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed =False
    item.save()
    return redirect('home')


def edit(request, list_id): #whenever the web server calls the webpg. it is requesting that web pg. we need to pass tat req into our func here
    
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)

        form = Listform(request.POST or None, instance=item)


        if form.is_valid():
            form.save()
          
            messages.success(request,('Items edited successfully!!'))
            return redirect('home')


    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})