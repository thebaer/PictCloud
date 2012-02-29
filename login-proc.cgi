#!/usr/bin/python

import sys, cgi
import MySQLdb
#import DBHelper
from HTML import startDoc, endDoc
from FormHelper import Clean
import cgitb
cgitb.enable()

def login(user, passw):
	db = MySQLdb.connect("php.radford.edu", "mbaer2","moldycheese","mbaer2")
	cur = db.cursor()
	cur.execute("SELECT uid FROM users WHERE username = '"+user+"' AND password = PASSWORD('"+passw+"')")
	row = cur.fetchone()
	if row == None:
		return False
	else:
		return row[0]


form = cgi.FieldStorage()

error = False
if form:
	if "username" in form.keys():
		username = form.getvalue("username")
		password = form.getvalue("password")
		uid = login(username, password)
		if uid:
			print "Set-Cookie: user="+username
			print "Location: dashboard.cgi"
			print
			sys.exit()
		else:
			error = True

# HTTP Headers
print "Content-Type: text/html"
print

print startDoc("Login")

print "<div id=\"the-void\">"
print "<h1>Login to RU PictCloud</h1>\n\n"

if "auth" in form.keys():
	print "<p class='error'>You are unauthorized to access this page.</p>"
elif "cook" in form.keys():
	print "<p class='error'>You must have cookies enabled to use this site.</p>"
elif error:
	print "<p class='error'>Incorrect username and/or password.</p>"
elif "logged" in form.keys():
	print "<p class='msg'>You have been logged out.</p>"
	
print "<form action=\"login.cgi\" method=\"post\">"
print "\t<input type='text' name='username' />"
print "\t<input type='password' name='password' />"
print "\t<input type='submit' value='Login' />"
print "</form>"

print "</div>"

print endDoc()
