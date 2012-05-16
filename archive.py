import os

#Use xcode-select -switch <xcode_folder_path> to set your Xcode folder path
XCODEBUILD = '/usr/bin/xcodebuild'
XCRUN = '/usr/bin/xcrun'
PLISTBUDDY = '/usr/libexec/PlistBuddy'

class Archive(object):
	options = {}
	def __init__(self):
		self.options = {
			'generate_dSYM':True,
			'clean_build':True,
			'ipa_path':'',
			'developer_identity':'',
			'mobile_provision':'',
			'xcodeproj':'',
			'zip_dSYM':True
		}

	def archive_project(self):
		if self.options['zip_dSYM']:
			self.zip_archive_symbols()

	def zip_archive_symbols(self):
		pass