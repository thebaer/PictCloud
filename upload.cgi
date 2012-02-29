#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()
import os, sys
import Cookie
import HTML, Pics
from Database import DB
from User import Member, checkLoggedIn
from FormHelper import Clean

cookie = HTML.getCookies()
checkLoggedIn()

u = Member(cookie['uid'].value)
db = DB()
db.connect()

print HTML.headers()
print HTML.startDoc("Upload")

print "<div id=\"the-void\">"
print HTML.headerGroup("Upload a picture")
print HTML.navigation()

print HTML.dashNav('upload')

print "<form action='uploaded.cgi' method='POST' enctype='multipart/form-data'>"
print "<p><strong>1.</strong> Select an album:</p>"
albums = Pics.getAlbums(db, u.getID())

print "<select name='album'>"
if albums:
	for album in albums:
		print "<option value='%s'>%s</option>" % (album['aid'], album['title'])
	print "</select> &nbsp;or... <a href='new-album.cgi'>make a new one</a>"
else:
	print "<option value='-1'>No albums created!</option>"
	print "</select> &nbsp;<a href='new-album.cgi'>make one now</a>"

print "<p><strong>2.</strong> Choose a picture.</p>"
# Check if 'error' is set, and output message
print "<input name='img-1' type='file'><br />"

print "<p><strong>3.</strong> Write a little something about it...</p>"
print "<textarea name='caption'></textarea>"

print "<p><strong>4.</strong> Make it more searchable with tags. (space-separated)</p>"
print "<input type='text' name='tags' style='width:50%' />"

print "<p><strong>5.</strong> <input name='submit' type='submit' value='Upload'></p>"
print "</form>"
print "</div>"

print HTML.endDoc()

def save_uploaded_file (form_field, upload_dir):
	form = cgi.FieldStorage()
	if not form.has_key(form_field): 
		return
	fileitem = form[form_field]
	if not fileitem.file: 
		return
	fout = file (os.path.join(upload_dir, fileitem.filename), 'wb')
	while 1:
		chunk = fileitem.file.read(100000)
		if not chunk: 
			break
		fout.write(chunk)
	fout.close()

save_uploaded_file ("file_1", HTML.UPLOAD_DIR)
