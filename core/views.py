from django.views.generic import CreateView, UpdateView, DetailView, ListView

from .models import Contact

class ContactCreateView(CreateView):
	model = Contact
	action = 'created'

class ContactUpdateView(UpdateView):
	model = Contact
	action = 'updated'

class ContactDetailView(DetailView):
	model = Contact

class ContactListView(ListView):
	model = Contact