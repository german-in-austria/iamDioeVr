from django.db import models
import uuid
import math
from vr.views import pOrte


class audiodatei(models.Model):
	added			= models.DateTimeField(auto_now_add=True															, verbose_name="Hinzugefügt")
	file			= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="Dateiname")
	typ				= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="Typ (S/D)")
	ort				= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="Ort")
	alter			= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="Alter (j/a)")
	satz			= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="Satz (02/05/12/28)")
	gpKennzahl		= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="Kennzahl")
	benutzt			= models.IntegerField(				  blank=True, null=True											, verbose_name="Benutzt")

	def __str__(self):
		return '{} ({})'.format(self.file, self.added)

	class Meta:
		verbose_name = "Audiodatei"
		verbose_name_plural = "Audiodateien"
		ordering = ('satz', 'ort', 'typ', 'alter', 'gpKennzahl', )


class antworten(models.Model):
	spiel			= models.ForeignKey('spiel'			, on_delete=models.CASCADE										, verbose_name="Spiel")
	runde			= models.IntegerField(				  blank=True, null=True											, verbose_name="Runde")
	beispiel		= models.IntegerField(				  blank=True, null=True											, verbose_name="Beispiel")
	zeit			= models.DateTimeField(auto_now_add=True															, verbose_name="Zeit")
	audiodatei		= models.ForeignKey('audiodatei'	, on_delete=models.CASCADE										, verbose_name="Audiodatei")
	wiedergaben		= models.IntegerField(				  blank=True, null=True											, verbose_name="Wiedergaben")
	gewOrt			= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="gewählter Ort")
	sympathie		= models.IntegerField(				  blank=True, null=True											, verbose_name="Sympathie (0-6)")
	correct			= models.BooleanField(default=False																	, verbose_name="Richtige Antwort")
	correctBl		= models.BooleanField(default=False																	, verbose_name="Richtiges Bundesland")
	correctDr		= models.BooleanField(default=False																	, verbose_name="Richtiger Dialektraum")

	def save(self, *args, **kwargs):
		try:
			aSpieler = self.spiel.spieler
			aAntw = antworten.objects.filter(spiel__spieler_id=aSpieler.pk).count()
			aRichtigeKlasse = None
			if aAntw > 0:
				aRichtigeKlasse = math.floor(4.99 / aAntw * antworten.objects.filter(spiel__spieler_id=aSpieler.pk, correct=True).count()) + 1
			aSpieler.richtigeKlasse = aRichtigeKlasse
			aRichtigeKlasseBl = None
			if aAntw > 0:
				aRichtigeKlasseBl = math.floor(4.99 / aAntw * antworten.objects.filter(spiel__spieler_id=aSpieler.pk, correctBl=True).count()) + 1
			aSpieler.richtigeKlasseBl = aRichtigeKlasseBl
			aRichtigeKlasseDr = None
			if aAntw > 0:
				aRichtigeKlasseDr = math.floor(4.99 / aAntw * antworten.objects.filter(spiel__spieler_id=aSpieler.pk, correctDr=True).count()) + 1
			aSpieler.richtigeKlasseDr = aRichtigeKlasseDr
			aSpieler.save()
		except Exception as e:
			print(e)
		super(antworten, self).save(*args, **kwargs)

	def __str__(self):
		return '{}, {} [{}] [{}] [{}] {} ({}) - {}'.format(self.runde, self.beispiel, 'X' if self.correct else ' ', 'X' if self.correctBl else ' ', 'X' if self.correctDr else ' ', self.sympathie, self.zeit, self.audiodatei)

	class Meta:
		verbose_name = "Antwort"
		verbose_name_plural = "Antworten"
		ordering = ('zeit', 'runde', 'beispiel', )


class spiel(models.Model):
	spieler			= models.ForeignKey('spieler'		, on_delete=models.CASCADE										, verbose_name="Spieler")
	zeit			= models.DateTimeField(auto_now_add=True															, verbose_name="Zeit")

	def __str__(self):
		return '{} ({}) - {}'.format(self.pk, self.zeit, self.spieler)

	class Meta:
		verbose_name = "Spiel"
		verbose_name_plural = "Spiele"
		ordering = ('spieler', 'zeit', )


class spieler(models.Model):
	zeit			= models.DateTimeField(auto_now_add=True															, verbose_name="Zeit")
	uuid			= models.UUIDField(default=uuid.uuid4, editable=False, unique=True									, verbose_name="uuid")
	# Fragebogen mit Orten usw.
	geburtsjahr		= models.IntegerField(				  blank=True, null=True											, verbose_name="Geburtsjahr")
	bioGesch		= models.IntegerField(				  blank=True, null=True											, verbose_name="biologisches Geschlecht")
	beruf			= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="Beruf")
	wohnort			= models.ForeignKey('ort', related_name='rn_wohnort', blank=True, null=True	, on_delete=models.SET_NULL, verbose_name="Wohnort")
	wohnortLeben	= models.ForeignKey('ort', related_name='rn_wohnortLeben', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Wohnort Leben")
	sprachenDialekte = models.CharField(max_length=255	, blank=True, null=True											, verbose_name="Sprachen / Dialekten aufgewachsen")
	dsgvo			= models.BooleanField(default=False																	, verbose_name="DSGVO")
	weitere			= models.BooleanField(default=False																	, verbose_name="Weitere Angaben?")
	wohnortVater	= models.ForeignKey('ort', related_name='wohnortVater', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Wohnort")
	wohnortMutter	= models.ForeignKey('ort', related_name='wohnortMutter', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Wohnort")
	sprachlichErzogenVater = models.IntegerField(		  blank=True, null=True											, verbose_name="sprachlich Erzogen Vater")
	sprachlichErzogenMutter = models.IntegerField(		  blank=True, null=True											, verbose_name="sprachlich Erzogen Mutter")
	dialektSelbst	= models.NullBooleanField(default=None, blank=True, null=True										, verbose_name="Dialekt selbst?")
	dialektSelbstWelcher = models.CharField(max_length=255, blank=True, null=True										, verbose_name="Eigener Dialekt")
	dialektSprechen	= models.IntegerField(				  blank=True, null=True											, verbose_name="Dialekt sprechen")
	dialektNutzen	= models.IntegerField(				  blank=True, null=True											, verbose_name="Dialekt nutzen")
	hochdeutschSprechen = models.IntegerField(			  blank=True, null=True											, verbose_name="Hochdeutsch sprechen")
	hochdeutschNutzen = models.IntegerField(			  blank=True, null=True											, verbose_name="Hochdeutsch nutzen")
	alltagSprechen = models.IntegerField(				  blank=True, null=True											, verbose_name="Alltag sprechen")
	bezeichnungSprechweise = models.CharField(max_length=255, blank=True, null=True										, verbose_name="Sprechweise")
	anmerkungen		= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="Anmerkungen")
	# Spracheinstellung
	dialektSympathisch = models.CharField(max_length=255, blank=True, null=True											, verbose_name="Dialekt sympathisch")
	dialektSympathischWarum = models.CharField(max_length=255, blank=True, null=True									, verbose_name="Warum Dialekt sympathisch")
	dialektUnsympathisch = models.CharField(max_length=255, blank=True, null=True										, verbose_name="Dialekt unsympathisch")
	dialektUnsympathischWarum = models.CharField(max_length=255, blank=True, null=True									, verbose_name="Warum Dialekt unsympathisch")
	gehoerteDialekte = models.CharField(max_length=255, blank=True, null=True											, verbose_name="gehörte Dialekte")
	# Cach
	richtigeKlasse	= models.IntegerField(				  blank=True, null=True											, verbose_name="Richtig (1 = 0%-20%, 2 = 20%-40%, ...)")
	richtigeKlasseBl = models.IntegerField(				  blank=True, null=True											, verbose_name="Richtig Bundesland (1 = 0%-20%, 2 = 20%-40%, ...)")
	richtigeKlasseDr = models.IntegerField(				  blank=True, null=True											, verbose_name="Richtig Dialektregion (1 = 0%-20%, 2 = 20%-40%, ...)")

	def __str__(self):
		return '{} [{}] ({} - {})'.format(self.pk, 'X' if self.weitere else ' ', self.zeit, self.uuid)

	class Meta:
		verbose_name = "Spieler"
		verbose_name_plural = "Spieler"
		ordering = ('zeit', )


class ort(models.Model):
	plz				= models.IntegerField(				  blank=True, null=True											, verbose_name="Plz")
	ort				= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="Ort")

	def __str__(self):
		return '{} ({})'.format(self.plz, self.ort)

	class Meta:
		verbose_name = "Ort"
		verbose_name_plural = "Orte"
		ordering = ('plz', 'ort', )
