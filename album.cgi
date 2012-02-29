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


form = cgi.FieldStorage()
albumID = form.getvalue("id")
db = DB()
db.connect()

albumInfoRow = db.getRow("SELECT title, author_id AS author FROM albums WHERE aid = %s" % albumID)
if albumInfoRow:
	albumName = albumInfoRow[0]
	authorID = albumInfoRow[1]
else:
	Utils.errorRedirect("This album doesn't exist.", "dashboard.cgi")

a = Member(authorID)

row = db.getRow("SELECT username FROM users WHERE uid = '%s'" % a.getID())
if row:
	a.setName(row[0])

print HTML.headers()
print HTML.startDoc(albumName + " album")
print "<div id=\"the-void\">"
print HTML.headerGroup(albumName)
print HTML.navigation()
print "<h2>by %s</h2>" % a.getName()

pics = db.query("SELECT filename FROM photos WHERE album_id = %s" % albumID)
if pics:
	print "<div id='gallery' class='quack'>"
	for pic in pics:
		print Pics.getLinkPic(pic['filename'])
	print "</div>"
else:
	print "<p class='notify'><strong>There are no pictures in this album.</strong>"
	print "<br /><br /><a href='upload.cgi'>upload pictures</a></p>"


print "</div>"

print HTML.endDoc()
