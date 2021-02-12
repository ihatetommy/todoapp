from django.contrib import admin
from django.urls import path
from .views import TodoitemListView, TodoitemCreateView, TodoitemUpdateView, TodoitemDeleteView

urlpatterns = [
	path('', TodoitemListView.as_view(), name='item-list'),
	path('new-item/', TodoitemCreateView.as_view(), name='item-new'),
	path('edit/<int:pk>/', TodoitemUpdateView.as_view(), name='item-edit'),
	path('delete/<int:pk>/', TodoitemDeleteView.as_view(), name='item-delete'),
]

