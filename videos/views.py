from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView


from .models import Video

class VideoListView(ListView):
	model = Video

class VideoCreateView(CreateView):
	model = Video

class VideoUpdateView(UpdateView):
	model = Video

class VideoDetailView(DetailView):
	model = Video

