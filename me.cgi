#!/usr/bin/python

import sys, os
import Cookie
import HTML
from Utils import redirect
from User import Member, checkLoggedIn
import cgitb; cgitb.enable()

cookie = HTML.getCookies()
checkLoggedIn()

u = Member(cookie['uid'].value)

redirect("profile.cgi?id=" + u.getID())
