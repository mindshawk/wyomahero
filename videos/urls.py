from django.conf.urls import patterns, include, url

from videos.views import VideoListView

urlpatterns = patterns("",
	url(r'^$', VideoListView.as_view(), name='portfolio'),
)