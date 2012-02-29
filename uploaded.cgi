#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()
import os, sys
import Cookie
import HTML
import Utils
from Database import DB
from User import Member, checkLoggedIn

cookie = HTML.getCookies()
checkLoggedIn()

u = Member(cookie['uid'].value)

form = cgi.FieldStorage()

def makeRandStr(len):
	from string import letters
	from random import choice
	ret = ""
	for i in xrange(len):
		ret += choice(letters)
	return ret

def validExtension(ext):
	validExts = ['png', 'jpg', 'jpeg', 'tiff', 'gif', 'bmp']
	return ext in validExts

def save_uploaded_file (form_field, upload_dir, form):
	if not form.has_key(form_field): 
		return
	fileitem = form[form_field]
	if not fileitem.file: 
		return
	uploadedfname = fileitem.filename
	fileParts = uploadedfname.split(".")  # fileParts = uploadedfname.rpartition('.')
	ext = fileParts[len(fileParts)-1]
	if not validExtension(ext):
		return
	fname = makeRandStr(29) + "." + ext   # fname = os.urandom(29) + fileParts[1]  + fileParts[2]
	fout = file(os.path.join(upload_dir, fname), 'wb')
	while 1:
		chunk = fileitem.file.read(100000)
		if not chunk: 
			break
		fout.write(chunk)
	fout.close()
	return fname

filename = save_uploaded_file("img-1", HTML.UPLOAD_DIR, form)

if filename:
	aid = form.getvalue("album")

	# check for a caption
	if form.has_key("caption") and form['caption'].value != "":
		caption = form.getvalue("caption")
	else:
		caption = 'NULL'

	# check for tags
	if form.has_key("tags") and form['tags'].value != "":
		tags = form.getvalue("tags")
	else:
		tags = 'NULL'

	db = DB()
	db.connect()
	if db.insert("photos", {'author_id':u.getID()
		, 'album_id':aid
		, 'filename':filename
		, 'caption':caption
		, 'tags':tags}):
		Utils.redirect("photo.cgi?file=%s" % filename)
	else:
		print HTML.headers()
		print HTML.startDoc("Upload Failed")

		print "<div id=\"the-void\">"
		print HTML.headerGroup("Error")

		print HTML.navigation()
		print "<p>Sorry, there was an error with the database. Please try again later.</p>"
		print "</div>"

		print HTML.endDoc()
else:
	Utils.errorRedirect("Could not upload file", "upload.cgi")

