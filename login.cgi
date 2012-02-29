#!/usr/bin/python

import sys, cgi
#import DBHelper
from HTML import startDoc, endDoc
from Database import DB
from FormHelper import Clean
import Utils
import cgitb; cgitb.enable()

ADMIN_USER = "admin"
ADMIN_PASS = "cheese"
connectedDB = False

db = DB()

if db.connect():
	def login(user, passw):
		row = db.getRow("SELECT uid FROM users WHERE username = '"+user+"' AND password = PASSWORD('"+passw+"')")
		if row == None:
			return False
		else:
			return row[0]
else:
	def login(user, passw):
		if user == ADMIN_USER and passw == ADMIN_PASS:
			return 1
		else:
			return False

form = cgi.FieldStorage()
if form:
	if "username" in form.keys() and "password" in form.keys():
		username = form.getvalue("username")
		password = form.getvalue("password")
		uid = login(username, password)
		if uid:
			Utils.setCookies({'uid':str(uid)
				, 'username':username})
			loc = "dashboard.cgi"
		else:
			loc = "index.cgi?wrong=up"
else:
	loc = "index.cgi"

if connectedDB:
	cur.close()

Utils.redirect(loc)
