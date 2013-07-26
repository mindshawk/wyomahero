from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView


from .models import Person

class PeopleListView(ListView):
	model = Person
	