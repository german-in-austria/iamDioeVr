"""Spezielle Tags für templates."""
from django.conf import settings
from django.utils.module_loading import import_module
from django import template
from operator import itemgetter
import json
from webpack_loader import utils
from webpack_loader.exceptions import WebpackBundleLookupError
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def render_bundle(bundle_name, extension=None, config='DEFAULT', attrs=''):
	try:
		tags = utils.get_as_tags(bundle_name, extension=extension, config=config, attrs=attrs)
	except WebpackBundleLookupError as e:
		return''
	return mark_safe('\n'.join(tags))


@register.filter(name='toJson')
def toJson(value):
	"""Verwandelt Wert in Json > {{ value|toJson }} ."""
	return json.dumps(value)


@register.assignment_tag(takes_context=True)
def navbarMaker(context):
	"""Erstellt Navigation."""
	anavbar = []
	for value in settings.INSTALLED_APPS:  # Alle Installierten Apps durchgehen und nach navbar.py suchen.
		try:
			anavbar.extend(import_module("%s.navbar" % value).navbar(context.request))
		except ImportError:
			pass
	return sorted(anavbar, key=itemgetter('sort'))


@register.assignment_tag
def to_list(*args):
	"""Wandelt Aufzählung in Liste um."""
	return args


@register.assignment_tag
def add_to_list(alist, add):
	"""Fügt Wert zu Liste."""
	if alist:
		return alist + [add]
	else:
		return [add]


@register.simple_tag
def getFeldVal(alist, val):
	"""Liest Wert aus einer Liste von Dictonarys aus."""
	if alist:
		for aDict in alist:
			if 'name' in aDict and aDict['name'] == val:
				if 'value' in aDict:
					return aDict['value']
				else:
					return
	return


@register.simple_tag
def obj_getattr(aobj, val):
	"""Für kategorienListeFXData."""
	def pObj_getattr(aobj, val):
		if 'all()' in val:  # Der "all()" Teil ist Expermintell! Ungetestet!
			bAll, pAll = val.split('all()', 1)
			if pAll[:2] == '__':
				pAll = pAll[2:]
			if bAll[-2:] == '__':
				bAll = bAll[:-2]
			aData = []
			for aktObj in pObj_getattr(aobj, bAll).all():
				aData.append(pObj_getattr(aktObj, pAll))
			return aData
		if '__' in val:
			avals = val.split('__')
		else:
			avals = [val]
		for aval in avals:
			if '()' in aval:
				aobj = getattr(aobj, aval[:-2])()
			else:
				aobj = getattr(aobj, aval)
		return aobj
	try:
		return pObj_getattr(aobj, val)
	except Exception as e:
		# print(e)
		# print(aobj)
		# print(dir(aobj))
		return ''


@register.filter
def get_item(dictionary, key):
	"""Wert aus Dictionary auslesen."""
	return dictionary.get(key)


@register.simple_tag(takes_context=True)
def render(context, value):
	"""Inline Template rendern."""
	return template.engines['django'].from_string(value).render(context)


# settings value
@register.simple_tag
def settings_value(name):
	"""Einstellung auslesen."""
	if name in getattr(settings, 'ALLOWED_SETTINGS_IN_TEMPLATES', ''):
		return getattr(settings, name, '')
	return ''
