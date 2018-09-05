"""Anzeige für Startseite."""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
import vr.models as dbmodels

import os
import json

pTypen = [
	{'s': 'S', 't': 'Standard'},
	{'s': 'D', 't': 'Dialekt'}
]
pOrte = [
	{'s': 'GAW', 't': 'Gaweinstal'},
	{'s': 'HÜT', 't': 'Hüttschlag'},
	{'s': 'NEC', 't': 'Neckenmarkt'},
	{'s': 'NEU', 't': 'Neumarkt an der Ybbs'},
	{'s': 'RAG', 't': 'Raggal'},
	{'s': 'TAR', 't': 'Tarrenz'},
	{'s': 'TAU', 't': 'Taufkirchen an der Pram'},
	{'s': 'TUX', 't': 'Tux'},
	{'s': 'WEI', 't': 'Weißbriach'}
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
	return render_to_response(
		'vr/start.html',
		RequestContext(request, {'mediaUrl': settings.MEDIA_URL, 'gData': {'typ': pTypen, 'orte': pOrte, 'alter': pAlter, 'saetze': pSaetze}}),)


def data(request):
	posFiles = getFiles()
	game = {'S': [], 'D': []}
	game['S'].append(list(posFiles['02']['GAW']['S']['j'].values())[0])
	game['S'].append(list(posFiles['02']['TAR']['S']['a'].values())[0])
	game['S'].append(list(posFiles['02']['WEI']['S']['j'].values())[0])
	game['D'].append(list(posFiles['02']['GAW']['D']['a'].values())[0])
	game['D'].append(list(posFiles['02']['TAR']['D']['j'].values())[0])
	game['D'].append(list(posFiles['02']['WEI']['D']['a'].values())[0])
	return httpOutput(json.dumps(game), mimetype='application/json; charset=utf-8')

def updateaudio(request):
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
				any(d['s'] == aOrt for d in pOrte) and
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

def getFiles():
	oFiles = {}
	files = [f for f in os.listdir(settings.MEDIA_DIR) if os.path.isfile(os.path.join(settings.MEDIA_DIR, f))]
	aLen = 0
	for file in files:
		fileData = file[:-4].split("_")
		if file.split(".")[-1] == "ogg" and len(fileData) == 5:
			(aTyp, aOrt, aAlter, aSatz, aGpKennzahl) = fileData
			if any(d['s'] == aSatz for d in pSaetze):
				if aSatz not in oFiles:
					oFiles[aSatz] = {}
				if any(d['s'] == aOrt for d in pOrte):
					if aOrt not in oFiles[aSatz]:
						oFiles[aSatz][aOrt] = {}
					if any(d['s'] == aTyp for d in pTypen):
						if aTyp not in oFiles[aSatz][aOrt]:
							oFiles[aSatz][aOrt][aTyp] = {}
						if any(d['s'] == aAlter for d in pAlter):
							if aAlter not in oFiles[aSatz][aOrt][aTyp]:
								oFiles[aSatz][aOrt][aTyp][aAlter] = {}
							oFiles[aSatz][aOrt][aTyp][aAlter][aGpKennzahl] = {'typ': aTyp, 'ort': aOrt, 'alter': aAlter, 'satz': aSatz, 'gpKennzahl': aGpKennzahl, 'file': file}
							aLen += 1
	return oFiles


def httpOutput(aoutput, mimetype='text/plain; charset=utf-8'):
	"""Einfache http Ausgabe."""
	txtausgabe = HttpResponse(aoutput)
	txtausgabe['Content-Type'] = mimetype
	return txtausgabe
