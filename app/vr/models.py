from django.db import models


class audiodatei(models.Model):
	added			= models.DateTimeField(																				  verbose_name="Hinzugefügt")
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
	durchgang		= models.IntegerField(				  blank=True, null=True											, verbose_name="Durchgang")
	runde			= models.IntegerField(				  blank=True, null=True											, verbose_name="Runde")
	beispiel		= models.IntegerField(				  blank=True, null=True											, verbose_name="Beispiel")
	zeit			= models.DateTimeField(																				  verbose_name="Zeit")
	audiodatei		= models.ForeignKey('audiodatei'	, on_delete=models.CASCADE										, verbose_name="Audiodatei")
	wiedergaben		= models.IntegerField(				  blank=True, null=True											, verbose_name="Wiedergaben")
	gewOrt			= models.CharField(max_length=255	, blank=True, null=True											, verbose_name="gewählter Ort")
	sympathie		= models.IntegerField(				  blank=True, null=True											, verbose_name="Sympathie (0-6)")

	def __str__(self):
		return '{} ({})'.format(self.audiodatei, self.zeit)

	class Meta:
		verbose_name = "Antwort"
		verbose_name_plural = "Antworten"
		ordering = ('spiel', 'durchgang', 'runde', 'beispiel', )


class spiel(models.Model):
	spieler			= models.ForeignKey('spieler'		, on_delete=models.CASCADE										, verbose_name="Spieler")
	zeit			= models.DateTimeField(																				  verbose_name="Zeit")

	def __str__(self):
		return '{} ({})'.format(self.spieler, self.zeit)

	class Meta:
		verbose_name = "Spiel"
		verbose_name_plural = "Spiele"
		ordering = ('spieler', 'zeit', )


class spieler(models.Model):
	zeit			= models.DateTimeField(																				  verbose_name="Zeit")
	# ToDo: Fragebogen mit Orten usw.

	def __str__(self):
		return '{} ({})'.format(self.pk, self.zeit)

	class Meta:
		verbose_name = "Spieler"
		verbose_name_plural = "Spieler"
		ordering = ('zeit', )
