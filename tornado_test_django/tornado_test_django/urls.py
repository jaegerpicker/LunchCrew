from django.conf.urls import patterns, include, url
from django.contrib import admin
from lunch_crew.views import DjangoView

admin.autodiscover()	

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tornado_test_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^d/', DjangoView.as_view()),
)
