"""Anzeige für Startseite."""
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Sum, Count

import os
import json

pTypen = [
	{'s': 'S', 't': 'Standard'},
	{'s': 'D', 't': 'Dialekt'}
]
pOrte = [
	{'s': 'GAW', 'sf': 'GAW', 't': 'Gaweinstal', 'bl': 'Niederösterreich', 'dr': 'Ostmittelbairisch', 'cy': 420.4, 'cx': 2725.5},
	{'s': 'HÜT', 'sf': 'HUET', 't': 'Hüttschlag', 'bl': 'Salzburg', 'dr': 'Südmittelbairisch', 'cy': 1126.2, 'cx': 1503.1},
	{'s': 'NEC', 'sf': 'NEC', 't': 'Neckenmarkt', 'bl': 'Burgenland', 'dr': 'Südmittelbairisch', 'cy': 896.3, 'cx': 2714.1},
	{'s': 'NEU', 'sf': 'NEU', 't': 'Neumarkt an der Ybbs', 'bl': 'Niederösterreich', 'dr': 'Ostmittelbairisch', 'cy': 605, 'cx': 2168.7},
	{'s': 'RAG', 'sf': 'RAG', 't': 'Raggal', 'bl': 'Vorarlberg', 'dr': 'Alemannisch', 'cy': 1107.3, 'cx': 266.8},
	{'s': 'TAR', 'sf': 'TAR', 't': 'Tarrenz', 'bl': 'Tirol', 'dr': 'Bairisch-Alemannisch', 'cy': 1079.5, 'cx': 604.8},
	{'s': 'TAU', 'sf': 'TAU', 't': 'Taufkirchen an der Pram', 'bl': 'Oberösterreich', 'dr': 'Ostmittelbairisch', 'cy': 457.4, 'cx': 1614.2, 'top': True},
	{'s': 'TUX', 'sf': 'TUX', 't': 'Tux', 'bl': 'Tirol', 'dr': 'Südbairisch', 'cy': 1137.1, 'cx': 945.4},
	{'s': 'WEI', 'sf': 'WEI', 't': 'Weißbriach', 'bl': 'Kärnten', 'dr': 'Südbairisch', 'cy': 1387.8, 'cx': 1511.2},
	{'s': 'BRE', 'sf': 'BRE', 't': 'Bregenz', 'bl': 'Vorarlberg', 'dr': 'Alemannisch', 'cy': 950.4, 'cx': 233.4},
	{'s': 'INN', 'sf': 'INN', 't': 'Innsbruck', 'bl': 'Tirol', 'dr': 'Südbairisch', 'cy': 1077.1, 'cx': 833.2, 'top': True},
	{'s': 'LIE', 'sf': 'LIE', 't': 'Lienz', 'bl': 'Tirol', 'dr': 'Südbairisch', 'cy': 1312.1, 'cx': 1334.6},
	{'s': 'KLA', 'sf': 'KLA', 't': 'Klagenfurt', 'bl': 'Kärnten', 'dr': 'Südbairisch', 'cy': 1422.4, 'cx': 1896.1},
	{'s': 'SBG', 'sf': 'SBG', 't': 'Salzburg', 'bl': 'Salzburg', 'dr': 'Südmittelbairisch', 'cy': 789.8, 'cx': 1434.7},
	{'s': 'STY', 'sf': 'STY', 't': 'Steyrling', 'bl': 'Oberösterreich', 'dr': 'Ostmittelbairisch', 'cy': 787.3, 'cx': 1830.5},
	{'s': 'LIN', 'sf': 'LIN', 't': 'Linz', 'bl': 'Oberösterreich', 'dr': 'Ostmittelbairisch', 'cy': 515.5, 'cx': 1887.9},
	{'s': 'OWÖ', 'sf': 'OWOE', 't': 'Oberwölz', 'bl': 'Steiermark', 'dr': 'Südbairisch', 'cy': 1111.8, 'cx': 1885.4},
	{'s': 'PAS', 'sf': 'PAS', 't': 'Passail', 'bl': 'Steiermark', 'dr': 'Südmittelbairisch', 'cy': 1069.9, 'cx': 2334.6},
	{'s': 'GRA', 'sf': 'GRA', 't': 'Graz', 'bl': 'Steiermark', 'dr': 'Südmittelbairisch', 'cy': 1176.2, 'cx': 2305.9},
	{'s': 'EIS', 'sf': 'EIS', 't': 'Eisenstadt', 'bl': 'Burgenland', 'dr': 'Ostmittelbairisch', 'cy': 765.5, 'cx': 2700.1},
	{'s': 'ALL', 'sf': 'ALL', 't': 'Allentsteig', 'bl': 'Niederösterreich', 'dr': 'Ostmittelbairisch', 'cy': 300.6, 'cx': 2267},
	{'s': 'STP', 'sf': 'STP', 't': 'St.Pölten', 'bl': 'Niederösterreich', 'dr': 'Ostmittelbairisch', 'cy': 568.4, 'cx': 2374.5, 'top': True},
	{'s': 'WIE', 'sf': 'WIE', 't': 'Wien', 'bl': 'Wien', 'dr': 'Ostmittelbairisch', 'cy': 571.2, 'cx': 2645.5},
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
	"""Daten abfragen/setzen durch VUE."""
	import vr.models as dbmodels
	if 'set' in request.POST:
		# Speichere Spracheinstellung
		if request.POST.get('set') == 'playerDataSe':
			aData = json.loads(request.POST.get('data'))
			aSpieler = dbmodels.spieler.objects.get(uuid=request.POST.get('playerUuId'))  # Überprüfen ob Spiel mit Spieler existiert
			aSpieler.dialektSympathisch = aData['data']['dialektSympathisch'].strip()
			aSpieler.dialektSympathischWarum = aData['data']['dialektSympathischWarum'].strip()
			aSpieler.dialektUnsympathisch = aData['data']['dialektUnsympathisch'].strip()
			aSpieler.dialektUnsympathischWarum = aData['data']['dialektUnsympathischWarum'].strip()
			aSpieler.gehoerteDialekte = aData['data']['gehoerteDialekte'].strip()
			aSpieler.save()
			return httpOutput(json.dumps({'OK': True, 'playerUuId': str(aSpieler.uuid)}), mimetype='application/json; charset=utf-8')
		# Speichere Spielerdaten
		if request.POST.get('set') == 'playerData':
			aData = json.loads(request.POST.get('data'))
			aSpieler = dbmodels.spieler()
			aSpieler.geburtsjahr = int(aData['data']['geburtsjahr'])
			aSpieler.bioGesch = int(aData['data']['bioGesch'])
			aSpieler.beruf = aData['data']['beruf'].strip()
			if ('ort' in aData['data']['wohnort'] and aData['data']['wohnort']['ort'].strip()) or ('plz' in aData['data']['wohnort'] and aData['data']['wohnort']['plz'] and int(aData['data']['wohnort']['plz']) > 0):
				aOrt = None
				try:
					aOrt = dbmodels.ort.objects.get(plz=int(aData['data']['wohnort']['plz']), ort=aData['data']['wohnort']['ort'].strip())
				except dbmodels.ort.DoesNotExist:
					aOrt = dbmodels.ort()
					aOrt.plz = int(aData['data']['wohnort']['plz'])
					aOrt.ort = aData['data']['wohnort']['ort'].strip()
					aOrt.save()
				aSpieler.wohnort = aOrt
			if ('ort' in aData['data']['wohnortLeben'] and aData['data']['wohnortLeben']['ort'].strip()) or ('plz' in aData['data']['wohnortLeben'] and aData['data']['wohnortLeben']['plz'] and int(aData['data']['wohnortLeben']['plz']) > 0):
				aOrt = None
				try:
					aOrt = dbmodels.ort.objects.get(plz=int(aData['data']['wohnortLeben']['plz']), ort=aData['data']['wohnortLeben']['ort'].strip())
				except dbmodels.ort.DoesNotExist:
					aOrt = dbmodels.ort()
					aOrt.plz = int(aData['data']['wohnortLeben']['plz'])
					aOrt.ort = aData['data']['wohnortLeben']['ort'].strip()
					aOrt.save()
				aSpieler.wohnortLeben = aOrt
			aSpieler.sprachenDialekte = aData['data']['sprachenDialekte'].strip()
			aSpieler.dsgvo = aData['data']['dsgvo']
			if aData['weitere']:
				aSpieler.weitere = True
				if ('ort' in aData['data']['wohnortVater'] and aData['data']['wohnortVater']['ort'].strip()) or ('plz' in aData['data']['wohnortVater'] and aData['data']['wohnortVater']['plz'] and int(aData['data']['wohnortVater']['plz']) > 0):
					aOrt = None
					try:
						aOrt = dbmodels.ort.objects.get(plz=int(aData['data']['wohnortVater']['plz']), ort=aData['data']['wohnortVater']['ort'].strip())
					except dbmodels.ort.DoesNotExist:
						aOrt = dbmodels.ort()
						aOrt.plz = int(aData['data']['wohnortVater']['plz'])
						aOrt.ort = aData['data']['wohnortVater']['ort'].strip()
						aOrt.save()
					aSpieler.wohnortVater = aOrt
				if ('ort' in aData['data']['wohnortMutter'] and aData['data']['wohnortMutter']['ort'].strip()) or ('plz' in aData['data']['wohnortMutter'] and aData['data']['wohnortMutter']['plz'] and int(aData['data']['wohnortMutter']['plz']) > 0):
					aOrt = None
					try:
						aOrt = dbmodels.ort.objects.get(plz=int(aData['data']['wohnortMutter']['plz']), ort=aData['data']['wohnortMutter']['ort'].strip())
					except dbmodels.ort.DoesNotExist:
						aOrt = dbmodels.ort()
						aOrt.plz = int(aData['data']['wohnortMutter']['plz'])
						aOrt.ort = aData['data']['wohnortMutter']['ort'].strip()
						aOrt.save()
					aSpieler.wohnortMutter = aOrt
				aSpieler.sprachlichErzogenVater = int(aData['data']['sprachlichErzogenVater'])
				aSpieler.sprachlichErzogenMutter = int(aData['data']['sprachlichErzogenMutter'])
				aSpieler.dialektSelbst = True if aData['data']['dialektSelbst'] == 'Ja' else False if aData['data']['dialektSelbst'] == 'Nein' else None
				if aSpieler.dialektSelbst:
					aSpieler.dialektSelbstWelcher = aData['data']['dialektSelbstWelcher'].strip()
					aSpieler.dialektSprechen = int(aData['data']['dialektSprechen'])
					aSpieler.dialektNutzen = int(aData['data']['dialektNutzen'])
				aSpieler.hochdeutschSprechen = int(aData['data']['hochdeutschSprechen'])
				aSpieler.hochdeutschNutzen = int(aData['data']['hochdeutschNutzen'])
				aSpieler.alltagSprechen = int(aData['data']['alltagSprechen'])
				aSpieler.bezeichnungSprechweise = aData['data']['bezeichnungSprechweise'].strip()
				aSpieler.anmerkungen = aData['data']['anmerkungen'].strip()
			aSpieler.save()
			return httpOutput(json.dumps({'OK': True, 'playerUuId': str(aSpieler.uuid)}), mimetype='application/json; charset=utf-8')
		# Speichere Spielrunde
		if request.POST.get('set') == 'gameRound' and 'playerUuId' in request.POST:
			aData = json.loads(request.POST.get('data'))  # {'selOrt': 'NEU', 'rundeNr': 0, 'played': 1, 'beispielNr': 0, 'gId': 11, 'sympathie': 3, 'aId': 12}
			aGame = dbmodels.spiel.objects.get(pk=aData['gId'], spieler__uuid=request.POST.get('playerUuId'))  # Überprüfen ob Spiel mit Spieler existiert
			aAntwort = dbmodels.antworten()
			aAntwort.spiel = aGame
			aAntwort.audiodatei = dbmodels.audiodatei.objects.get(pk=aData['aId'])
			aAntwort.runde = aData['rundeNr']
			aAntwort.beispiel = aData['beispielNr']
			aAntwort.wiedergaben = aData['played']
			aAntwort.gewOrt = aData['selOrt']
			aAntwort.sympathie = aData['sympathie']
			sollOrt = None
			selOrt = None
			for d in pOrte:
				if d['s'] == aAntwort.audiodatei.ort:
					sollOrt = d
			for d in pOrte:
				if d['s'] == aAntwort.gewOrt:
					selOrt = d
			if aAntwort.audiodatei.ort == aAntwort.gewOrt:
				aAntwort.correct = True
			if sollOrt and selOrt:
				if selOrt['bl'] == sollOrt['bl']:
					aAntwort.correctBl = True
				if selOrt['dr'] == sollOrt['dr']:
					aAntwort.correctDr = True
			aAntwort.save()
			aAntwort.audiodatei.benutzt += 1
			aAntwort.audiodatei.save()
			return httpOutput(json.dumps({'OK': True, 'playerUuId': request.POST.get('playerUuId')}), mimetype='application/json; charset=utf-8')
	if 'get' in request.POST:
		# Auswertung
		if request.POST.get('get') == 'auswertungsData' and 'playerUuId' in request.POST:
			auswertung = {
				'playerUuId': request.POST.get('playerUuId')
			}
			if auswertung['playerUuId']:
				aSpieler = dbmodels.spieler.objects.get(uuid=auswertung['playerUuId'])  # Überprüfen ob UuId existiert
				auswertung['antworten'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk).count()
				auswertung['antwortenRichtig'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, correct=True).count()
				auswertung['antwortenRichtigBl'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, correctBl=True).count()
				auswertung['antwortenRichtigDr'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, correctDr=True).count()
				auswertung['antwortenDialekt'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__typ='D').count()
				auswertung['antwortenDialektRichtig'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__typ='D', correct=True).count()
				auswertung['antwortenDialektRichtigBl'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__typ='D', correctBl=True).count()
				auswertung['antwortenDialektRichtigDr'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__typ='D', correctDr=True).count()
				auswertung['antwortenStandard'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__typ='S').count()
				auswertung['antwortenStandardRichtig'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__typ='S', correct=True).count()
				auswertung['antwortenStandardRichtigBl'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__typ='S', correctBl=True).count()
				auswertung['antwortenStandardRichtigDr'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__typ='S', correctDr=True).count()
				auswertung['antwortenJung'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__alter='j').count()
				auswertung['antwortenJungRichtig'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__alter='j', correct=True).count()
				auswertung['antwortenJungRichtigBl'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__alter='j', correctBl=True).count()
				auswertung['antwortenJungRichtigDr'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__alter='j', correctDr=True).count()
				auswertung['antwortenAlt'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__alter='a').count()
				auswertung['antwortenAltRichtig'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__alter='a', correct=True).count()
				auswertung['antwortenAltRichtigBl'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__alter='a', correctBl=True).count()
				auswertung['antwortenAltRichtigDr'] = dbmodels.antworten.objects.filter(spiel__spieler_id=aSpieler.pk, audiodatei__alter='a', correctDr=True).count()
				auswertung['statistik'] = []
				for x in [1, 2, 3, 4, 5]:
					auswertung['statistik'].append({
						'Ho': dbmodels.spieler.objects.filter(richtigeKlasse=x).count(),
						'Bl': dbmodels.spieler.objects.filter(richtigeKlasseBl=x).count(),
						'Dr': dbmodels.spieler.objects.filter(richtigeKlasseDr=x).count()
					})
				auswertung['richtigeKlasse'] = aSpieler.richtigeKlasse
				auswertung['richtigeKlasseBl'] = aSpieler.richtigeKlasseBl
				auswertung['richtigeKlasseDr'] = aSpieler.richtigeKlasseDr
			return httpOutput(json.dumps(auswertung), mimetype='application/json; charset=utf-8')
		# Spiel Daten
		if request.POST.get('get') == 'gameData' and 'playerUuId' in request.POST:
			game = {
				'playerUuId': request.POST.get('playerUuId')
			}
			if game['playerUuId']:
				aSpiel = dbmodels.spiel()
				aSpiel.spieler = dbmodels.spieler.objects.get(uuid=game['playerUuId'])  # Überprüfen ob UuId existiert
				aSpiel.save()
				game['gId'] = aSpiel.pk
				from random import shuffle
				# Sätze
				# ToDo: Bereits gespielte Sätze unwarscheinlicher machen!
				xSaetze = dbmodels.antworten.objects.filter(spiel__spieler__uuid=game['playerUuId']).values('audiodatei__satz').annotate(satz_Count=Count('audiodatei__satz')).order_by('audiodatei__satz')
				# [{'satz_Count': 2, 'audiodatei__satz': '02'}, {'satz_Count': 1, 'audiodatei__satz': '12'}]
				xSatzCountMax = 0
				xSatzCountMin = 99999999
				for xSatz in xSaetze:
					if xSatz['satz_Count'] > xSatzCountMax:
						xSatzCountMax = xSatz['satz_Count']
					if xSatz['satz_Count'] < xSatzCountMin:
						xSatzCountMin = xSatz['satz_Count']
				iSaetze = []
				if xSatzCountMin != 99999999 and xSatzCountMax > xSatzCountMin:
					for xSatz in xSaetze:
						if xSatz['satz_Count'] == xSatzCountMax:
							iSaetze.append(xSatz['audiodatei__satz'])
				aSaetze = []
				for aSatz in dbmodels.audiodatei.objects.all().values('satz').annotate(benutzt=Sum('benutzt')).order_by('benutzt'):
					if aSatz['satz'] not in iSaetze:
						aSaetze.append(aSatz)
				aSaetzeMax = 0
				for aSatz in aSaetze:
					if aSatz['benutzt'] > aSaetzeMax:
						aSaetzeMax = aSatz['benutzt']
				uSatz = weighted_choice([x['satz'] for x in aSaetze], [aSaetzeMax - x['benutzt'] + 1 for x in aSaetze])
				# Orte
				aOrte = []
				for aOrt in dbmodels.audiodatei.objects.filter(satz=uSatz).values('ort').annotate(benutzt=Sum('benutzt')).order_by('benutzt'):
					useOrt = True
					for uTyp in ['S', 'D']:
						if dbmodels.audiodatei.objects.filter(satz=uSatz, ort=aOrt['ort'], typ=uTyp, alter='j').count() < 1 or dbmodels.audiodatei.objects.filter(satz=uSatz, ort=aOrt['ort'], typ=uTyp, alter='a').count() < 1:
							useOrt = False
					if useOrt:
						aOrte.append(aOrt)
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
						for aAlter in pAlter:
							aFiles = []
							aFilesMax = 0
							for aFile in dbmodels.audiodatei.objects.filter(satz=uSatz, ort=uOrt, typ=uTyp, alter=aAlter['s']).order_by('benutzt')[:10]:
								# ToDo: Durchschnittswert hinzufügen
								aFiles.append({'pk': aFile.pk, 'file': aFile.file, 'ort': aFile.ort, 'benutzt': aFile.benutzt})
								if aFile.benutzt > aFilesMax:
									aFilesMax = aFile.benutzt
							uFile = weighted_choice(aFiles, [aFilesMax - x['benutzt'] + 1 for x in aFiles])
							if uTyp not in game:
								game[uTyp] = []
							game[uTyp].append(uFile)
					shuffle(game[uTyp])
					# Selber Ort nicht hintereinander!
					lOrt = None
					for aOrtIdx, aOrt in enumerate(game[uTyp]):
						if aOrt['ort'] == lOrt:
							if aOrtIdx < len(game[uTyp]) - 1:
								lOrt = game[uTyp][aOrtIdx + 1]['ort']
								game[uTyp][aOrtIdx], game[uTyp][aOrtIdx + 1] = game[uTyp][aOrtIdx + 1], game[uTyp][aOrtIdx]
							else:
								game[uTyp][aOrtIdx], game[uTyp][0] = game[uTyp][0], game[uTyp][aOrtIdx]
						else:
							lOrt = aOrt['ort']
					shuffle(uOrte)
				return httpOutput(json.dumps(game), mimetype='application/json; charset=utf-8')
	return httpOutput(json.dumps({'error': 'unknown request'}), mimetype='application/json; charset=utf-8')


def updateaudio(request):
	"""Audiodateien in Datenbank eintragen."""
	import vr.models as dbmodels
	if not request.user.is_authenticated():
		return httpOutput('Erst einloggen!')
	files = [f for f in os.listdir(settings.MEDIA_DIR) if os.path.isfile(os.path.join(settings.MEDIA_DIR, f))]
	aLen = 0
	aUpdate = 0
	output = ''
	for file in files:
		fileData = file[:-4].split("_")
		if file.split(".")[-1] == "ogg" and len(fileData) == 5:
			uOrt = False
			(aTyp, aOrt, aAlter, aSatz, aGpKennzahl) = fileData
			for d in pOrte:
				if d['sf'] == aOrt:
					uOrt = d['s']
			if (
				any(d['s'] == aSatz for d in pSaetze) and
				uOrt and
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
					nAudiodatei.ort = uOrt
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
