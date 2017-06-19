#MenuTitle: Delete node names/labels
# -*- coding: utf-8 -*- 

import GlyphsApp

Font = Glyphs.font
selectedLayers = Font.selectedLayers

for l in selectedLayers:
	for p in l.paths: 
		for n in p.nodes:
			n.name=None