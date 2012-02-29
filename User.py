#!/usr/bin/python
import os

class Member:

	def __init__(self, uid):
		self.uid = uid
		self.uname = ""
	
	def getName(self):
		return self.uname

	def setName(self, newName):
		self.uname = newName

	def getID(self):
		return self.uid

def isLoggedIn():
	import sys, os, Cookie
	# http://www.dreamincode.net/forums/topic/166789-simple-cookie-program-cookie-not-identified/
	cookie = Cookie.SimpleCookie()
	if 'HTTP_COOKIE' in os.environ:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	return "uid" in cookie

def checkLoggedIn():
	import HTML
	# Make sure this is a valid logged in user.
	if not isLoggedIn():
		print "Location: " + HTML.baseURL + "index.cgi?auth=no"
		print
		sys.exit()
