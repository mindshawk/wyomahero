
from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^admin/', include(admin.site.urls)),

    url(r"^account/", include("account.urls")),

    url(r'newsletter/', include('newsletter.urls')),

    url(r'portfolio/', TemplateView.as_view(template_name="portfolio.html"), name="portfolio"),
    url(r'news/', include('news.urls')),
    url(r'about/', include('people.urls')),

    url(r'contact/', include('core.urls')),
    #url(r'contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),

    url(r'thanks/', TemplateView.as_view(template_name='thanks.html'), name='thanks'),

    url(r'indevelopment/', TemplateView.as_view(template_name="indevelopment.html"), name="indevelopment"),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

