"""Anzeige für Startseite."""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
import vr.models as dbmodels
from django.db.models import Sum

import os
import json

pTypen = [
	{'s': 'S', 't': 'Standard'},
	{'s': 'D', 't': 'Dialekt'}
]
pOrte = [
	{'s': 'GAW', 'sf': 'GAW', 't': 'Gaweinstal'},
	{'s': 'HÜT', 'sf': 'HUET', 't': 'Hüttschlag'},
	{'s': 'NEC', 'sf': 'NEC', 't': 'Neckenmarkt'},
	{'s': 'NEU', 'sf': 'NEU', 't': 'Neumarkt an der Ybbs'},
	{'s': 'RAG', 'sf': 'RAG', 't': 'Raggal'},
	{'s': 'TAR', 'sf': 'TAR', 't': 'Tarrenz'},
	{'s': 'TAU', 'sf': 'TAU', 't': 'Taufkirchen an der Pram'},
	{'s': 'TUX', 'sf': 'TUX', 't': 'Tux'},
	{'s': 'WEI', 'sf': 'WEI', 't': 'Weißbriach'}
]
pAlter = [
	{'s': 'j', 't': 'jung'},
	{'s': 'a', 't': 'alt'}
]
pSaetze = [
	{'s': '02', 't': '02'},
	{'s': '05', 't': '05'},
	{'s': '12', 't': '12'},
	{'s': '28', 't': '28'}
]


def start(request):
	"""Startseite."""
	return render_to_response(
		'vr/start.html',
		RequestContext(request, {'mediaUrl': settings.MEDIA_URL, 'gData': {'typ': pTypen, 'orte': pOrte, 'alter': pAlter, 'saetze': pSaetze}}),)


def data(request):
	"""Daten abfragen durch VUE."""
	if 'get' in request.POST:
		if request.POST.get('get') == 'gameData' and 'playerUuId' in request.POST:
			game = {
				'playerUuId': request.POST.get('playerUuId')
			}
			if game['playerUuId']:
				dbmodels.spieler.objects.get(uuid=game['playerUuId'])  # Überprüfen ob UuId existiert
				from random import shuffle
				# Sätze
				aSaetze = dbmodels.audiodatei.objects.all().values('satz').annotate(benutzt=Sum('benutzt')).order_by('benutzt')
				# ToDo: Bereits gespielte Sätze unwarscheinlicher machen!
				aSaetzeMax = 0
				for aSatz in aSaetze:
					if aSatz['benutzt'] > aSaetzeMax:
						aSaetzeMax = aSatz['benutzt']
				uSatz = weighted_choice([x['satz'] for x in aSaetze], [aSaetzeMax - x['benutzt'] + 1 for x in aSaetze])
				# Orte
				aOrte = dbmodels.audiodatei.objects.filter(satz=uSatz).values('ort').annotate(benutzt=Sum('benutzt')).order_by('benutzt')
				# ToDo: Bereits gespielte Orte unwarscheinlicher machen!
				aOrteMax = 0
				for aOrt in aOrte:
					if aOrt['benutzt'] > aOrteMax:
						aOrteMax = aOrt['benutzt']
				uOrte = []
				dg = 0
				while len(uOrte) < 3:
					dg += 1
					uOrt = weighted_choice([x['ort'] for x in aOrte], [aOrteMax - x['benutzt'] + 1 for x in aOrte])
					if uOrt not in uOrte or dg > 10:
						uOrte.append(uOrt)
				# Spieldaten
				for uTyp in ['S', 'D']:
					for uOrt in uOrte:
						aFiles = []
						aFilesMax = 0
						for aFile in dbmodels.audiodatei.objects.filter(satz=uSatz, ort=uOrt, typ=uTyp).order_by('benutzt')[:10]:
							# ToDo: Durchschnittswert
							aFiles.append({'pk': aFile.pk, 'file': aFile.file, 'ort': aFile.ort, 'benutzt': aFile.benutzt})
							if aFile.benutzt > aFilesMax:
								aFilesMax = aFile.benutzt
						uFile = weighted_choice(aFiles, [aFilesMax - x['benutzt'] + 1 for x in aFiles])
						if uTyp not in game:
							game[uTyp] = []
						game[uTyp].append(uFile)
					shuffle(uOrte)
				return httpOutput(json.dumps(game), mimetype='application/json; charset=utf-8')
	return httpOutput(json.dumps({'error': 'unknown request'}), mimetype='application/json; charset=utf-8')


def updateaudio(request):
	"""Audiodateien in Datenbank eintragen."""
	if not request.user.is_authenticated():
		return httpOutput('Erst einloggen!')
	files = [f for f in os.listdir(settings.MEDIA_DIR) if os.path.isfile(os.path.join(settings.MEDIA_DIR, f))]
	aLen = 0
	aUpdate = 0
	output = ''
	for file in files:
		fileData = file[:-4].split("_")
		if file.split(".")[-1] == "ogg" and len(fileData) == 5:
			(aTyp, aOrt, aAlter, aSatz, aGpKennzahl) = fileData
			if (
				any(d['s'] == aSatz for d in pSaetze) and
				any(d['sf'] == aOrt for d in pOrte) and
				any(d['s'] == aTyp for d in pTypen) and
				any(d['s'] == aAlter for d in pAlter)
			):
				aLen += 1
				output += str(aLen).rjust(4, ' ') + ' - ' + file + ' -> '
				try:
					dbmodels.audiodatei.objects.get(file=file)
					output += 'exists\n'
				except dbmodels.audiodatei.DoesNotExist:
					aUpdate += 1
					nAudiodatei = dbmodels.audiodatei()
					nAudiodatei.file = file
					nAudiodatei.typ = aTyp
					nAudiodatei.ort = aOrt
					nAudiodatei.alter = aAlter
					nAudiodatei.satz = aSatz
					nAudiodatei.gpKennzahl = aGpKennzahl
					nAudiodatei.benutzt = 0
					nAudiodatei.save()
					output += 'added\n'
	return httpOutput('Updated ... ' + str(aUpdate) + '/' + str(aLen) + '/' + str(len(files)) + '\n' + '-----' + '\n' + output)


def httpOutput(aoutput, mimetype='text/plain; charset=utf-8'):
	"""Einfache http Ausgabe."""
	txtausgabe = HttpResponse(aoutput)
	txtausgabe['Content-Type'] = mimetype
	return txtausgabe


def weighted_choice(values, weights):
	"""Gewichteter Zufall."""
	from random import random
	from bisect import bisect
	total = 0
	cum_weights = []
	for w in weights:
		total += w
		cum_weights.append(total)
	x = random() * 0.9999 * total
	i = bisect(cum_weights, x)
	return values[i]
