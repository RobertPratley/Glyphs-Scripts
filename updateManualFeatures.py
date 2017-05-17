#MenuTitle: Update manual features for Remove/Keep Glyphs 
# -*- coding: utf-8 -*-
__doc__="""
Updates manual feature code for glyphs in 'Remove/Keep Glyphs' custom parameters.
"""

import re
import GlyphsApp

font = Glyphs.font
glyphs = [g.name for g in font.glyphs]

def rebuildManualFeatures(glyphlist):
	for glyph in glyphlist:
			for feature in font.features:
				if not feature.automatic:
					if glyph in feature.code:
						fName = feature.name
						newFeatureCode = ""
						for line in feature.code.splitlines():
							if line.find(glyph)<0:
								newFeatureCode = newFeatureCode + line + "\n"
						if len(newFeatureCode) == 0:
							feaToRemove.append(fName)	
						else:
							rgx = re.compile(r".*{\s*}.*")
							newFeatureCode = re.sub(rgx, '', newFeatureCode)
							newFeatureCode = fName + "; " + newFeatureCode
							print newFeatureCode
							cP = GSCustomParameter('Replace Feature', newFeatureCode)
							iParam.append(cP)		

for instance in font.instances:
	iParam = instance.customParameters
	rG = iParam['Remove Glyphs']
	kG = iParam['Keep Glyphs']
	feasToRemove = []
	if rG:
		rebuildManualFeatures(rG)
	elif kG:
		nonkG = [i for i in glyphs if i not in kG]
		rebuildManualFeatures(nonkG)
	else:
		continue
		
	if len(feasToRemove) != 0:
		iParam.append(GSCustomParameter('Remove Features', feasToRemove))
							