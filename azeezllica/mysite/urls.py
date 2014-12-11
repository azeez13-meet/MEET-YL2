from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from polls import views

urlpatterns = patterns('',
	url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.my_page, name='my_page'),
    url(r'^help$', views.help, name='help'),
    url(r'^about$', views.about, name='about'),
)
