from django.conf.urls import patterns, include, url

from .views import ContactCreateView, ContactUpdateView, ContactDetailView, ContactListView

urlpatterns = patterns("",
	url(r'^$', ContactCreateView.as_view(), name='contact_create'),
	url(r'^$', ContactUpdateView.as_view(), name='contact_update'),
	url(r'^$', ContactDetailView.as_view(), name='contact_detail'),
	url(r'^$', ContactListView.as_view(), name='contact_list'),

)