import logging
import os
import re

import sublime

def logger(name, level=logging.DEBUG):
	sh = logging.StreamHandler()
	sh.setLevel(logging.DEBUG)
	sh.setFormatter(logging.Formatter('%(levelname)s:%(name)s:%(message)s'))
	log = logging.getLogger(name)
	log.setLevel(level)
	log.addHandler(sh)
	return log

log = logger(__name__)

_settings = None

def get_setting(key, default=None):
	global _settings
	try:
		s = sublime.active_window().active_view().settings()
		if s.has(key):
			return s.get(key)
	except:
		pass
	if _settings is None:
		_settings = sublime.load_settings("SublimeJava.sublime-settings")
	return _settings.get(key, default)

def check_settings(*settings):
	"""Decorator that checks given settings to affirm they're True.

	Returns:
		Wrapped function
	"""
	def _decor(fn):
		def _fn(*args, **kwargs):
			for setting in settings:
				if not get_setting(setting):
					return
			return fn(*args, **kwargs)
		return _fn
	return _decor