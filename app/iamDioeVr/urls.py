from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
from vr import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'main/login.html'}, name='iamdioevr_login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': reverse_lazy('Vr:start')}, name='iamdioevr_logout'),
	url(r'^$', include('vr.urls', namespace='Vr')),
	url(r'^data/', views.data, name='data'),
	url(r'^updateaudio/', views.updateaudio, name='updateaudio'),
	url(r'^evaluation/', include('evaluation.urls', namespace='evaluation')),
]
