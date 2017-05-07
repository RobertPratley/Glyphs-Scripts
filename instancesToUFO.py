#MenuTitle: export instances as UFO
# -*- coding: utf-8 -*-
__doc__="""Exports instances as UFOs to a directory chosen at runtime"""

import GlyphsApp

UFODir = GetFolder()

for i in Glyphs.font.instances:	
	iF = i.interpolatedFont
	iF.save("{0}/{1} {2}.ufo".format(UFODir, iF.familyName, i.name)) 
