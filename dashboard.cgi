#!/usr/bin/python

import sys, os
import Cookie
import HTML, Utils, Pics
from Database import DB
from User import Member, checkLoggedIn
from FormHelper import Clean
import cgitb; cgitb.enable()

cookie = HTML.getCookies()
checkLoggedIn()

u = Member(cookie['uid'].value)

error = Utils.getError()

db = DB()
db.connect()
row = db.getRow("SELECT username FROM users WHERE uid = '"+u.getID()+"'")
u.setName(row[0])

print HTML.headers()
print HTML.startDoc("Dashboard")

print "<div id=\"the-void\">"
print HTML.headerGroup("Welcome to RU PictCloud")
print HTML.navigation()

print HTML.dashNav('home')

if error:
	print error

print "<p>Welcome, <strong>" + u.getName() + "</strong>! (<a href='edit-pro.cgi'>Edit Profile</a>)</p>"

print "<h2>Recently Uploaded</h2>"
res = db.query("SELECT filename, album_id FROM photos WHERE author_id = '%s' LIMIT 5" % u.getID())

if res:
	print "<div id='gallery' class='quack'>"
	for row in res:
		print Pics.getLinkPic(row['filename'])
	print "</div>"
else:
	print "<p>No uploaded photos. <a href='upload.cgi'>upload one now</a>"

print "</div>"

print HTML.endDoc()
