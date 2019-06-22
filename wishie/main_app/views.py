from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django import forms
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import ItemForm
from .models import Item


def home(request):
        items = Item.objects.all()
        return render(request, 'home.html', {
            'items': items
        })

def add_item(request):
    item_form = ItemForm()
    model_item = Item
    if request.method == 'POST':
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            model_item = item_form.save()
            items = Item.objects.all()
            return render(request, 'home.html', {
                'item_form': item_form,
                'items': items
            })
        else:
            error_message = 'Invalid credentials -- try again'
    else:
        return render(request, 'add.html', {
            'item_form': item_form
        })


# def create_widget(request):
#     model_widget = Widget
#     if request.method == 'POST':
#         widget_form = WidgetForm(request.POST)
#         if widget_form.is_valid():
#             model_widget = widget_form.save()
#             widgets = Widget.objects.all()
#             return render(request, 'home.html', {
#                 'widget_form': widget_form,
#                 'widgets': widgets
#             })
#         else:
#             error_message = 'Invalid credentials -- try again'
#             return render(request, 'home.html', {
#                 'widget_form': widget_form,
#                 'model_widget': Widget
#             })


# def delete(request):
#     model_widget = Widget
#     if request.method == 'POST':
#         widget_form = WidgetForm(request.POST)
#         if widget_form.is_valid():
#             model_widget = widget_form.save()
#             return render(request, 'home.html', {
#                 'widget_form': widget_form,
#                 'model_widget': Widget
#             })
#         else:
#             error_message = 'Invalid credentials -- try again'
#             return render(request, 'home.html', {
#                 'widget_form': widget_form,
#                 'model_widget': Widget
#             })


class ItemDelete(DeleteView):
  model = Item
  template_name = 'home.html'
  success_url = reverse_lazy('home')
