from django.conf.urls import patterns, include, url

from news.views import NewsListView

urlpatterns = patterns("",
	url(r'^$', NewsListView.as_view(), name='news'),
)