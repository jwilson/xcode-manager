import os
from archive import Archive

class Xcode(object):
	archive = None

	def __init__(self):
		self.archive = Archive()