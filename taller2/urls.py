from django.conf.urls import patterns, include, url
from principal.views import HomeView, IndexView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taller2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view()),
    url(r'^index/$', IndexView.as_view()),
    url(r'^crear$', 'principal.views.crear'),
    url(r'^log-out/$', 'principal.views.LogOut'),
    url(r'^admin/', include(admin.site.urls)),
)
