"""Anzeige für Startseite."""
from django.shortcuts import render_to_response
from django.template import RequestContext


def start(request):
	return render_to_response(
		'vr/start.html',
		RequestContext(request,),)
