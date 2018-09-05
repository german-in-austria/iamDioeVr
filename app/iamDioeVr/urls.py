from django.conf.urls import include, url
from django.contrib import admin
from vr import views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', include('vr.urls', namespace='Vr')),
	url(r'^data/', views.data, name='data'),
	url(r'^updateaudio/', views.updateaudio, name='updateaudio'),
]
