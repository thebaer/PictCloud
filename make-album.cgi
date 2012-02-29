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
title = form.getvalue("title")

db = DB()
db.connect()
if not db.insert("albums", {'author_id':u.getID()
	, 'title':title}):
	Utils.errorRedirect("You already have an album by that name.", "new-album.cgi")

row = db.getRow("SELECT aid FROM albums WHERE author_id = %s AND title = '%s'" % (int(u.getID()), title))
if row:
	newAlbumID = row[0]
	Utils.redirect("album.cgi?id=%s" % newAlbumID)
