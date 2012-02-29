#!/usr/bin/python

import sys, os, cgi
import Cookie
import HTML, Utils, Pics
from Database import DB
from User import Member, checkLoggedIn
from FormHelper import Clean
import cgitb; cgitb.enable()

cookie = HTML.getCookies()
checkLoggedIn()

u = Member(cookie['uid'].value)

db = DB()
db.connect()
row = db.getRow("SELECT username FROM users WHERE uid = '"+u.getID()+"'")
u.setName(row[0])

print HTML.headers()
print HTML.startDoc("My Albums")
print "<div id=\"the-void\">"
print HTML.headerGroup("%s's Albums" % u.getName())
print HTML.navigation()

print HTML.dashNav("albums")

albums = Pics.getAlbums(db, u.getID())
if albums:
	print "<ul id='albumList'>"
	for album in albums:
		print "<li><a href='album.cgi?id=%s'>%s</a> (%s)</li>" % (album['aid'],album['title'],album['numPics'])
	print "</ul>"
else:
	print "<p class='notify'><strong>You haven't made any albums yet.</strong>"
	print "<br /><br /><a href='new-album.cgi'>create one now</a></p>"

print "</div>"

print HTML.endDoc()
