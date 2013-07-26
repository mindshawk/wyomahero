from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView


from .models import NewsPost

class NewsListView(ListView):
	model = NewsPost
	