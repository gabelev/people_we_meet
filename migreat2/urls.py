from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from peer_app import views
from django.views.generic import RedirectView
from django.http import HttpResponse, HttpResponseRedirect


urlpatterns = patterns('',
	url(r'^$',  lambda r: HttpResponseRedirect('/login/')),
    url(r'^main/$', views.main_list),
    url(r'^event/$', views.main_list_event),
    url(r'^admin/', include(admin.site.urls)),
    url('^login/', 'django.contrib.auth.views.login',
        {'template_name': 'login_true.html'})


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)