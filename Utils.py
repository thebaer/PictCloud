#!/usr/bin/python
import sys

def setCookies(cookies):
	for cname, cval in cookies.items():
		cval = cval.replace(" ", "%20")
		print "Set-Cookie: "+cname+"="+cval+"; Domain=php.radford.edu; Secure" # % (cname, cval)

def removeCookies(cookies):
	for cname in cookies:
		print "Set-Cookie: "+cname+"=expired; expires=Sun, 02-Oct-2011 00:00:00 GMT; Domain=php.radford.edu; Secure"

def redirect(toPage):
	print "Location: %s" % toPage
	print

def errorRedirect(msg, toPage):
	setCookies({"error":msg})
	redirect(toPage)
	sys.exit()

def getError():
	import HTML
	cookie = HTML.getCookies()
	try:
		err = cookie['error'].value
		err = err.replace("%20", " ")
		removeCookies(['error'])
		return "<p class='error'>" + err + "</p>"
	except:
		return

