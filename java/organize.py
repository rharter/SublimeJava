import os
import re

import sublime_plugin

from util import logger, get_setting

log = logger(__name__)

RE_IMPORT_SECTION = "(^import[^;\n]+;[^\n]*\n)+"

class OrganizeJavaImportsCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		sections = self.view.find_all(RE_IMPORT_SECTION, 0)
		section_imports = [self.view.substr(section) for section in sections]
		for i in range(len(sections)):
			# TODO pass func to organize as java, 3rd party, project
			imports = section_imports[i][:-1].split("\n")
			imports.sort()
			imports = "\n".join(imports) + "\n"

			self.view.replace(edit, sections[i], imports)

	# def run(self, edit):
	# 	order = get_setting("sublimejava_import_order")
	# 	order_re = ["(^import %s[^;\n]+;[^\n]*\n)+" % c for c in order]

	# 	all_imports = []
	# 	for reg in order_re:
	# 		section = self.view.find(reg, 0)
	# 		log.debug("got section: %s" % section)
	# 		imports = self.view.substr(section).split("\n")
	# 		imports.sort()
	# 		imports = "\n".join(imports) + "\n"

	# 		self.view.replace(edit, section, imports)