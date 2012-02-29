#!/usr/bin/python

import sys, os, cgi
import Cookie
import HTML, Utils
from Database import DB
from User import Member, checkLoggedIn
from FormHelper import Clean
import cgitb; cgitb.enable()

cookie = HTML.getCookies()
checkLoggedIn()

u = Member(cookie['uid'].value)
error = Utils.getError()

print HTML.headers()
print HTML.startDoc("New Album")


print "<div id=\"the-void\">"
print HTML.headerGroup("New Album")

print HTML.navigation()

db = DB()
db.connect()

row = db.getRow("SELECT username FROM users WHERE uid = '"+u.getID()+"'")
if row:
	u.setName(row[0])

print HTML.dashNav('new-album')

if error:
	print error

print "<form action='make-album.cgi' method='post'>"
print "<div class='field'><div class='label'>Album title:</div><div class='input'><input type='text' name='title' maxlength='120' /></div></div>"
print "<input type='submit' name='submitted' value='Make Album' />"
print "</form>"

print "</div>"

print HTML.endDoc()
