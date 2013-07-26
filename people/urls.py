from django.conf.urls import patterns, include, url

from people.views import PeopleListView

urlpatterns = patterns("",
	url(r'^$', PeopleListView.as_view(), name='about'),
)