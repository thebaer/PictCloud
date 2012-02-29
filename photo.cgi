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
imgName = form.getvalue("file")
db = DB()
db.connect()

imgInfoRow = db.getRow("SELECT author_id, album_id, caption, tags, (SELECT title FROM albums WHERE aid = album_id) AS album FROM photos WHERE filename = '%s'" % imgName)
if imgInfoRow:
	authorID = imgInfoRow[0]
	albumID = imgInfoRow[1]
	caption = imgInfoRow[2]
	spaceTags = imgInfoRow[3]
	if spaceTags is not None:
		splitTags = spaceTags.split(" ")
		tags = ", ".join(splitTags)
	else:
		tags = "None"
	albumTitle = imgInfoRow[4]
else:
	Utils.errorRedirect("This photo doesn't exist.", "dashboard.cgi")

a = Member(authorID)

row = db.getRow("SELECT username FROM users WHERE uid = '%s'" % a.getID())
if row:
	a.setName(row[0])

print HTML.headers()
print HTML.startDoc("View Photo")
print "<div id=\"the-void\">"
print HTML.headerGroup("View Photo")
print HTML.navigation()
print "<nav id='sub'><a href='album.cgi?id=%s'>&laquo; %s album</a></nav>" % (albumID, albumTitle)

print "<div id='showcase'>"
print "\t<img class='main' src='view.cgi?file=%s' />" % imgName
print "\t<div id='insights'>"
print "\t\t<p class='author'>by <a href='profile.cgi?id=%s'>%s</a></p>" % (a.getID(), a.getName())
print "\t\t<p>%s</p>" % caption
print "\t\t<p id='tags'>Tags: <span>%s</span></p>" % tags
print "\t</div>"
print "</div>"


print "</div>"

print HTML.endDoc()
