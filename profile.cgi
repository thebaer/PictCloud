#!/usr/bin/python

import sys, os, cgi
import Cookie
import HTML, Pics
from Database import DB
from User import Member, checkLoggedIn
from FormHelper import Clean
import cgitb; cgitb.enable()

cookie = HTML.getCookies()
checkLoggedIn()

form = cgi.FieldStorage()
u = Member(cookie['uid'].value)
p = Member(form.getvalue("id"))

db = DB()
db.connect()
row = db.getRow("SELECT username, bio FROM users WHERE uid = '"+p.getID()+"'")
if row:
	p.setName(row[0])
	bio = row[1]
	username = p.getName()

	# this was fudged a little due to time.
	if bio:
		bio = "'>" + bio
	else:
		bio = " notify'>" + username + " hasn't filled out his/her profile yet."
else:
	username = "User not found"
	bio = "Not found."

print HTML.headers()
print HTML.startDoc(username)


print "<div id=\"the-void\">"
print HTML.headerGroup(username)

print HTML.navigation()

print "<p class='bio" + bio + "</p>"
if u.getID() == p.getID():
	print "<p style='font-size:smaller'><a href='edit-pro.cgi'>Edit this</a></p>"

print "<h2>Latest Uploads</h2>"
res = db.query("SELECT filename, album_id, (SELECT title FROM albums WHERE aid=album_id) AS album_title FROM photos WHERE author_id = '%s' LIMIT 5" % p.getID())
if res:
	print "<div class='quack'>"
	for row in res:
		print "<div style='float:left'>"
		print Pics.getLinkPic(row['filename'])
		print "<p>from <a href='album.cgi?id=%s'>%s</a></p>" % (row['album_id'], row['album_title'])
		print "</div>"
	print "</div>"
else:
	print "<p>No uploaded photos."
	if u.getID() == p.getID():
		print " <a href='upload.cgi'>upload one now</a>"
	print "</p>"


print "</div>"

print HTML.endDoc()
