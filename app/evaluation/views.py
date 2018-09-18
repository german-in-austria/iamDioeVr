from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
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
	maxPerPage = 14
	aAntwortenM = dbmodels.antworten.objects.all().order_by('-spiel__spieler__zeit', 'spiel__zeit')
	aCount = aAntwortenM.count()
	# Seiten
	if getXls:
		import xlwt
		response = HttpResponse(content_type='text/ms-excel')
		response['Content-Disposition'] = 'attachment; filename="iamdioevr_' + datetime.date.today().strftime('%Y%m%d') + '.xls"'
		wb = xlwt.Workbook(encoding='utf-8')
		ws = wb.add_sheet('iamDioeVr')
		row_num = 0
		columns = []
		columns.append(('Nr', 2000))
		columns.append(('Antworten Id', 2000))
		columns.append(('Antworten runde', 2000))
		columns.append(('Antworten beispiel', 2000))
		columns.append(('Antworten wiedergaben', 2000))
		columns.append(('Antworten gewOrt', 2000))
		columns.append(('Antworten sympathie', 2000))
		columns.append(('Antworten zeit', 2000))
		columns.append(('Spiel Id', 2000))
		columns.append(('Spiel Zeit', 2000))
		columns.append(('Audiodatei Id', 2000))
		columns.append(('Audiodatei file', 2000))
		columns.append(('Audiodatei typ', 2000))
		columns.append(('Audiodatei ort', 2000))
		columns.append(('Audiodatei alter', 2000))
		columns.append(('Audiodatei satz', 2000))
		columns.append(('Audiodatei gpKennzahl', 2000))
		columns.append(('Audiodatei benutzt', 2000))
		columns.append(('Spieler Id', 2000))
		columns.append(('Spieler zeit', 2000))
		columns.append(('Spieler geburtsjahr', 2000))
		columns.append(('Spieler bioGesch', 2000))
		columns.append(('Spieler beruf', 2000))
		columns.append(('Spieler wohnort', 2000))
		columns.append(('Spieler wohnortLeben', 2000))
		columns.append(('Spieler sprachenDialekte', 2000))
		columns.append(('Spieler weitere', 2000))
		columns.append(('Spieler wohnortVater', 2000))
		columns.append(('Spieler wohnortMutter', 2000))
		columns.append(('Spieler sprachlichErzogenVater', 2000))
		columns.append(('Spieler sprachlichErzogenMutter', 2000))
		columns.append(('Spieler dialektSelbst', 2000))
		columns.append(('Spieler dialektSelbstWelcher', 2000))
		columns.append(('Spieler dialektSprechen', 2000))
		columns.append(('Spieler dialektNutzen', 2000))
		columns.append(('Spieler hochdeutschSprechen', 2000))
		columns.append(('Spieler hochdeutschNutzen', 2000))
		columns.append(('Spieler alltagSprechen', 2000))
		columns.append(('Spieler bezeichnungSprechweise', 2000))
		columns.append(('Spieler anmerkungen', 2000))
		columns.append(('Spieler dialektSympathisch', 2000))
		columns.append(('Spieler dialektSympathischWarum', 2000))
		columns.append(('Spieler dialektUnsympathisch', 2000))
		columns.append(('Spieler dialektUnsympathischWarum', 2000))
		columns.append(('Spieler gehoerteDialekte', 2000))
		font_style = xlwt.XFStyle()
		font_style.font.bold = True
		for col_num in range(len(columns)):
			ws.write(row_num, col_num, columns[col_num][0], font_style)
		font_style = xlwt.XFStyle()
		font_style_datetime = xlwt.XFStyle()
		font_style_datetime.num_format_str = 'YYYY-MM-DD hh:mm:ss'
		for obj in aAntwortenM:
			row_num += 1
			ws.write(row_num, 0, row_num, font_style)
			ws.write(row_num, 1, obj.pk, font_style)
			ws.write(row_num, 2, obj.runde, font_style)
			ws.write(row_num, 3, obj.beispiel, font_style)
			ws.write(row_num, 4, obj.wiedergaben, font_style)
			ws.write(row_num, 5, str(obj.gewOrt), font_style)
			ws.write(row_num, 6, obj.sympathie, font_style)
			ws.write(row_num, 7, obj.zeit, font_style_datetime)
			ws.write(row_num, 8, obj.spiel.pk, font_style)
			ws.write(row_num, 9, obj.spiel.zeit, font_style_datetime)
			ws.write(row_num, 10, obj.audiodatei.pk, font_style)
			ws.write(row_num, 11, obj.audiodatei.file, font_style)
			ws.write(row_num, 12, obj.audiodatei.typ, font_style)
			ws.write(row_num, 13, str(obj.audiodatei.ort), font_style)
			ws.write(row_num, 14, obj.audiodatei.alter, font_style)
			ws.write(row_num, 15, obj.audiodatei.satz, font_style)
			ws.write(row_num, 16, obj.audiodatei.gpKennzahl, font_style)
			ws.write(row_num, 17, obj.audiodatei.benutzt, font_style)
			ws.write(row_num, 18, obj.spiel.spieler.pk, font_style)
			ws.write(row_num, 19, obj.spiel.spieler.zeit, font_style_datetime)
			ws.write(row_num, 20, obj.spiel.spieler.geburtsjahr, font_style)
			ws.write(row_num, 21, obj.spiel.spieler.bioGesch, font_style)
			ws.write(row_num, 22, obj.spiel.spieler.beruf, font_style)
			ws.write(row_num, 23, str(obj.spiel.spieler.wohnort), font_style)
			ws.write(row_num, 24, str(obj.spiel.spieler.wohnortLeben), font_style)
			ws.write(row_num, 25, obj.spiel.spieler.sprachenDialekte, font_style)
			ws.write(row_num, 26, obj.spiel.spieler.weitere, font_style)
			ws.write(row_num, 27, str(obj.spiel.spieler.wohnortVater), font_style)
			ws.write(row_num, 28, str(obj.spiel.spieler.wohnortMutter), font_style)
			ws.write(row_num, 29, obj.spiel.spieler.sprachlichErzogenVater, font_style)
			ws.write(row_num, 30, obj.spiel.spieler.sprachlichErzogenMutter, font_style)
			ws.write(row_num, 31, obj.spiel.spieler.dialektSelbst, font_style)
			ws.write(row_num, 32, obj.spiel.spieler.dialektSelbstWelcher, font_style)
			ws.write(row_num, 33, obj.spiel.spieler.dialektSprechen, font_style)
			ws.write(row_num, 34, obj.spiel.spieler.dialektNutzen, font_style)
			ws.write(row_num, 35, obj.spiel.spieler.hochdeutschSprechen, font_style)
			ws.write(row_num, 36, obj.spiel.spieler.hochdeutschNutzen, font_style)
			ws.write(row_num, 37, obj.spiel.spieler.alltagSprechen, font_style)
			ws.write(row_num, 38, obj.spiel.spieler.bezeichnungSprechweise, font_style)
			ws.write(row_num, 39, obj.spiel.spieler.anmerkungen, font_style)
			ws.write(row_num, 40, obj.spiel.spieler.dialektSympathisch, font_style)
			ws.write(row_num, 41, obj.spiel.spieler.dialektSympathischWarum, font_style)
			ws.write(row_num, 42, obj.spiel.spieler.dialektUnsympathisch, font_style)
			ws.write(row_num, 43, obj.spiel.spieler.dialektUnsympathischWarum, font_style)
			ws.write(row_num, 44, obj.spiel.spieler.gehoerteDialekte, font_style)
		wb.save(response)
		return response
	else:
		if aSeite > 0:
			prev = aSeite - 1
		if aCount > (aSeite + 1) * maxPerPage:
			next = aSeite + 1
		# Antworten ... weiter
		aNr = aSeite * maxPerPage
		for aAntwort in aAntwortenM[aSeite * maxPerPage:aSeite * maxPerPage + maxPerPage]:
			aNr += 1
			aAuswertungen.append({'aNr': aNr, 'model': aAntwort})

		return render_to_response('evaluation/auswertungstart.html', RequestContext(request, {'aAuswertungen': aAuswertungen, 'aCount': aCount, 'prev': prev, 'next': next}))
