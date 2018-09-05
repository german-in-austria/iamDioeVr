from django.contrib import admin
from django.apps import apps
from django.utils.html import format_html

for model in apps.get_app_config('vr').models.items():
	admin.site.register(apps.get_model("vr", model[0]))
