# -*- coding: utf-8 -*-
#
#  Plugin Code
#
#  Coded/Modified/Adapted by örlgrey
#  Based on teamBlue image source code
#
#  This code is licensed under the Creative Commons 
#  Attribution-NonCommercial-ShareAlike 3.0 Unported 
#  License. To view a copy of this license, visit
#  http://creativecommons.org/licenses/by-nc-sa/3.0/ 
#  or send a letter to Creative Commons, 559 Nathan 
#  Abbott Way, Stanford, California 94305, USA.
#
#  If you think this license infringes any rights,
#  please contact me at ochzoetna@gmail.com

from Plugins.Plugin import PluginDescriptor
from Components.config import config
from Components.Language import language
from os import environ
import gettext
from Tools.Directories import resolveFilename, SCOPE_LANGUAGE, SCOPE_PLUGINS
import STekEBWeather

lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("STekEBWeather", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/STekEBWeather/locale/"))

def _(txt):
	t = gettext.dgettext("STekEBWeather", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

def main(session, **kwargs):
	reload(STekEBWeather)
	try:
		session.open(STekEBWeather.STekEBWeather)
	except:
		import traceback
		traceback.print_exc()

def Plugins(**kwargs):
	if config.skin.primary_skin.value == "GigablueSTekEBV2/skin.xml":
		list = []
		list.append(PluginDescriptor(name="STekEBWeather", description=_("STekEBWeather-Settings"), where = PluginDescriptor.WHERE_PLUGINMENU, icon='plugin.png', fnc=main))
		return list
	else:
		list = []
		return list
