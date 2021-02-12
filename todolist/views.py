from django.shortcuts import render
from .models import Todoitem
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
)

class TodoitemListView(ListView):
	model = Todoitem
	template_name = 'todolist/index.html'
	context_object_name = 'items'
	ordering = ['-date_posted']

class TodoitemCreateView(CreateView):
	model = Todoitem
	fields = ['title']
	template_name = 'todolist/new-item.html'

class TodoitemUpdateView(UpdateView):
	model = Todoitem
	fields = ['title']
	template_name = 'todolist/new-item.html'

class TodoitemDeleteView(DeleteView):
	model = Todoitem
	context_object_name = 'item'
	success_url = '/'
