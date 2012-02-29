#!/usr/bin/python

import sys, cgi
#import DBHelper
from HTML import startDoc, endDoc
from FormHelper import Clean
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
error = False

# HTTP Headers
print "Content-Type: text/html"
print

print startDoc("Login")

print "<div id=\"the-void\">"
print "<h1>Login to RU PictCloud</h1>\n\n"

print "<!--[if IE]><p style='font-size:larger;font-weight:bold;text-align:center;'>While this site will <em>display</em> in Internet Explorer, it will not do it well.<br />"
print "For the full RU PictCloud experience, we recommend a modern browser like <a href='http://www.google.com/chrome'>Google Chrome</a> or" 
print "<a href='http://www.mozilla.org/en-US/firefox/new/'>Mozilla Firefox</a>.</p><![endif]-->"

if "auth" in form.keys():
	print "<p class='error'>You are unauthorized to access this page.</p>"
elif "cook" in form.keys():
	print "<p class='error'>You must have cookies enabled to use this site.</p>"
elif "wrong" in form.keys():
	print "<p class='error'>Incorrect username and/or password.</p>"
elif "logged" in form.keys():
	print "<p class='msg'>You have been logged out.</p>"
	
print "<form action=\"login.cgi\" method=\"post\">"
print "\t<div class='field'><div class='label'>Username</div><div class='input'><input type='text' name='username' /></div></div>"
print "\t<div class='field'><div class='label'>Password</div><div class='input'><input type='password' name='password' /></div></div>"
print "\t<div class='field'><input type='submit' value='Login' /></div>"
print "</form>"

print "</div>"

print endDoc()
