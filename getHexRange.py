#MenuTitle: Get hex range
# -*- coding: utf-8 -*-
__doc__="""Writes a specified range of hex values to a text file on the Desktop."""

import GlyphsApp
import vanilla
import os.path

class getHexRange( object ):
	def __init__ ( self ):
		self.w = vanilla.Window((400, 280), "Get hex range")
		self.w.text_1 = vanilla.TextBox((20,20,-30,-10), "Starting hex:", sizeStyle="regular")
		self.w.startHex = vanilla.EditText((110,20-4,-20,22),placeholder="0000", sizeStyle="regular")
		self.w.text_2 = vanilla.TextBox((20,50,-30,-10), "Ending hex:", sizeStyle="regular")
		self.w.endHex = vanilla.EditText((110,50-4,-20,22),placeholder="0001", sizeStyle="regular")
		self.w.text_3 = vanilla.TextBox((20,80,-30,-10), "Output type:", sizeStyle="regular")
		self.w.format = vanilla.ComboBox((110, 80,-20,21),["One per line", "Comma separated", "Space separated", "Python list"], sizeStyle="regular")
		self.w.generate = vanilla.Button((20,110,-20,30), "Get hex range", sizeStyle="regular", callback=self.getRange)
		self.w.pane = vanilla.Box((20,160,-20,-20))
		self.w.pane.message = vanilla.TextBox((10, 10, -10, -10))
		self.w.open()
	def getRange(self, sender):
		start = int(self.w.startHex.get(), 16)
		end = int(self.w.endHex.get(), 16)
		for i in xrange(start, end + 1):
			hexes.append(str(format(i, 'X')))
		self.export()
	def formatChoice(self, x):
		if x == "One per line":
			format = "\n"
		elif x == "Comma separated":
			format = ", "
		elif x == "Space separated":
			format = " " 
		elif x == "Python list":
			format= None
		return format		
	def export(self):
		format = self.w.format.get()
		format = self.formatChoice(format)
		fileName = "hexRange_%s-%s.txt" % (self.w.startHex.get(), self.w.endHex.get())
		dirPath = filepath = os.path.expanduser(("~/") + 'Desktop')
		filePath = os.path.abspath(dirPath+"/"+fileName)
		with open(filePath, 'w+') as file:
			if format:
				file.write(format.join(hexes))
			else:
				file.write(str(hexes))
		message = "%s values found from %s to %s.\n\n%s written to Desktop" % (len(hexes), self.w.startHex.get().upper(), self.w.endHex.get().upper(), fileName)
		self.w.pane.message.set(message)
		hexes[:] = []
hexes = []
getHexRange()

