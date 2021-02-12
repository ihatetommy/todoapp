from django.db import models
from django.utils import timezone
from django.urls import reverse

class Todoitem(models.Model):
	title = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('item-list')

	class Meta:
		db_table = 'Item'
