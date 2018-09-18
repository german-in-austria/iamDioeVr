from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import vr.models as dbmodels
import datetime


def start(request):
	"""Startseite."""
	if not request.user.is_authenticated():
		return redirect('iamdioevr_login')
	aSeite = 0
	if 'seite' in request.GET and request.GET.get('seite'):
		aSeite = int(request.GET.get('seite'))
	getXls = False
	if 'get' in request.GET and request.GET.get('get') == 'xls':
		getXls = True
	aAuswertungen = []
	prev = -1
	next = -1
	maxPerPage = 15
	aAntwortenM = dbmodels.antworten.objects.all().order_by('-spiel__spieler__zeit', 'spiel__zeit')
	aCount = aAntwortenM.count()
	# Seiten
	if getXls:
		pass
	else:
		if aSeite > 0:
			prev = aSeite - 1
		if aCount > (aSeite + 1) * maxPerPage:
			next = aSeite + 1
		# Antworten ... weiter
		aNr = aSeite * maxPerPage
		for aAntwort in aAntwortenM if getXls else aAntwortenM[aSeite * maxPerPage:aSeite * maxPerPage + maxPerPage]:
			aNr += 1
			aAuswertungen.append({'aNr': aNr, 'model': aAntwort})

		return render_to_response('evaluation/auswertungstart.html', RequestContext(request, {'aAuswertungen': aAuswertungen, 'aCount': aCount, 'prev': prev, 'next': next}))
