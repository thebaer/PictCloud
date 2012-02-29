#!/usr/bin/python

import os.path
import sys
import cgi
import HTML
import cgitb; cgitb.enable()
from StringIO import StringIO


form = cgi.FieldStorage()
file = form.getvalue("file")
filename = HTML.UPLOAD_DIR + "/" + file

if not os.path.exists(filename):
	print "Content-type: text/html"
	print
	print "<h1>RU PictCloud</h1><p>No file!</p>"
	sys.exit()

print "Content-type: image/jpeg"
print

f = open(filename, 'rb')
output = StringIO()
img = f.read()
output.write(img)
print output.getvalue()
f.close()
