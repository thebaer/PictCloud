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

u = Member(cookie['uid'].value)

print HTML.headers()
print HTML.startDoc("Search")

form = cgi.FieldStorage()
search = form.getvalue("q")
dbSearch = '%' + search + '%'

print "<div id=\"the-void\">"
print HTML.headerSearchGroup("Search", search)

print HTML.navigation()

db = DB()
db.connect()
row = db.getRow("SELECT username FROM users WHERE uid = '"+u.getID()+"'")
u.setName(row[0])

print HTML.dashNav('search')

res = db.query("SELECT uid, username, bio FROM users WHERE username LIKE '"+dbSearch+"' OR bio LIKE '"+dbSearch+"' LIMIT 10")
print "<h2>Users</h2>"
if res:
	#print "<p>Found <strong>%s</strong> results.</p>" % db.rowcount
	print "<div id='results'>"
	for row in res:
		print "<div>\n\t<a href='profile.cgi?id=" + str(row['uid']) + "'>" + row['username'] + "</a>"
		if row['bio'] is not None:
			print "\t<p>" + row['bio'] + "</p>"
		print "</div>"
	print "</div>"
else:
	print "<p>No users found.</p>"

res = db.query("SELECT pid, (SELECT username FROM users WHERE uid = author_id) AS author_name, filename, caption, author_id FROM photos WHERE tags LIKE '"+dbSearch+"' OR caption LIKE '"+dbSearch+"' LIMIT 10")
print "<h2>Images</h2>"
if res:
	print "<div id='gallery' class='quack'>"
	for row in res:
		print "<div class='quack'>"
		print Pics.getLinkPic(row['filename'])
		print "<p>by <a href='profile.cgi?id=%s'>%s</a>" % (row['author_id'], row['author_name'])
		if row['caption'] is not None:
			print "\t<p>" + row['caption'] + "</p>"
		print "</div>"
	print "</div>"
else:
	print "<p>No images found.</p>"


print "</div>"

print HTML.endDoc()
