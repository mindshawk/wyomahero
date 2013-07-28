from django.conf.urls import patterns, include, url

#from .views import ContactCreateView, ContactUpdateView, ContactDetailView, ContactListView

from .views import Contact

urlpatterns = patterns("",
	url(r'^$', Contact, name='contact'),
	#url(r'^contact_create/$', ContactCreateView.as_view(), name='contact_create'),
	#url(r'^contact_update/$', ContactUpdateView.as_view(), name='contact_update'),
	#url(r'^contact_detail/$', ContactDetailView.as_view(), name='contact_detail'),
	#url(r'^contact_list/$', ContactListView.as_view(), name='contact_list'),

)