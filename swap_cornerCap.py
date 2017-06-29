#MenuTitle: Swap corner/cap hint components
# -*- coding: utf-8 -*- 


from vanilla import *

class hintSwitch(object):
	def __init__( self ) :
		font = Glyphs.font
		corners = []
		caps = []
		for g in font.glyphs:
			if '_corner' in g.name:
				corners.append(g.name)
			if '_cap' in g.name:
				caps.append(g.name)
		components = corners + caps
		
		self.w = FloatingWindow((10, 10, 300, 140))
		self.w.hintToReplace = TextBox((10, 10, -10, 23), 'Target hint to change:')
		self.w.glyphHintList = PopUpButton((10, 35, -10,23 ), components)
		
		self.w.replacmentHint = TextBox((10, 70, -10, 23), 'Replacement hint:')
		self.w.replacementHintList = PopUpButton((10, 95, -10,23 ), components, callback=self.swapHint)

		self.w.open()
		
	def swapHint(self, sender):
		targetHint = self.w.glyphHintList.getTitle()
		for glyph in Glyphs.font.selectedLayers:
			for i in glyph.hints:
				if i.name == targetHint:
					i.name = sender.getTitle()
		
		
hintSwitch()