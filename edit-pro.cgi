#!/usr/bin/python

import sys, os, cgi
import Cookie
import HTML
from Database import DB
from User import Member, checkLoggedIn
from FormHelper import Clean
import cgitb; cgitb.enable()

cookie = HTML.getCookies()
checkLoggedIn()

u = Member(cookie['uid'].value)

print HTML.headers()
print HTML.startDoc("Edit Profile")


print "<div id=\"the-void\">"
print HTML.headerGroup("Edit Your Profile")

print HTML.navigation()

db = DB()
db.connect()

form = cgi.FieldStorage()
saved = False
if "submitted" in form.keys():
	newbio = form.getvalue("bio")
	db.update('users', {'bio':newbio}, 'uid = '+u.getID())
	saved = True

row = db.getRow("SELECT username, bio FROM users WHERE uid = '"+u.getID()+"'")
if row:
	u.setName(row[0])
	bio = row[1]
	if not bio:
		bio = ""

print HTML.dashNav('edit-pro')

if saved:
	print "<p class='msg'>Looks nice! <a href='me.cgi'>View Profile</a></p>"

print "<form action='edit-pro.cgi' method='post'>"
print "<p>Enter a bio:</p>"
print "<textarea name='bio'>" + bio + "</textarea>"
print "<input type='submit' name='submitted' value='Save Changes' />"
print "</form>"

print "</div>"

print HTML.endDoc()
