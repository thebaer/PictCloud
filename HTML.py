#!/usr/bin/python
import User, Cookie, os

def getCookies():
	# Make sure logged in cookie is set
	# If not, send back to login form.
	try:
		cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		return cookie
	except (Cookie.CookieError, KeyError):
		print "Location: " + HTML.baseURL + "index.cgi?cook=no"
		print
		sys.exit()

def headers():
	# HTTP Headers
	ret = "Content-Type: text/html"
	ret = ret + "\n"
	return ret

def startDoc(title):
	# Beginning of document
	ret = "<html>\n<head>\n"
	ret += "\t<title>" + title + " | RU PictCloud</title>\n"
	ret += "\t<link rel=\"stylesheet\" href=\"main.css\" type=\"text/css\" />\n"
	ret += "</head>\n<body>\n"
	return ret

def endDoc():
	# End of document
	ret = "\n\t<footer>"
	if User.isLoggedIn():
		ret += "<a href=\"logout.cgi\">Logout</a>"
	ret += "</footer>\n"
	ret += "\n</body>\n</html>"
	return ret

def headerSearchGroup(head, searchVal):
	ret = "\t<hgroup>"
	ret += "\n\t\t<form class='search' action='search.cgi' method='get'><input type='text' name='q' value='"+searchVal+"' placeholder='Search' /><input type='submit' value='Search' /></form>"
	ret += "\n\t\t<img src='clouds_sm.png' style='float:left;margin-right: 12px;'/>"
	ret += "\n\t\t<h1>%(HEADER)s</h1>" % {'HEADER':head}
	ret += "\n\t</hgroup>\n"
	return ret
	
def headerGroup(head):
	return headerSearchGroup(head, '')

def navigation():
	ret = "\t<nav id=\"conscious\">"
	ret += "\n\t\t<h1>RUpc</h1>"
	ret += "\n\t\t<a href='dashboard.cgi'>Home</a>"
	ret += "\n\t\t<a href='upload.cgi'>Upload</a>"
	ret += "\n\t\t<a href='me.cgi'>Profile</a>"
	ret += "\n\t\t<a href='albums.cgi'>Albums</a>"
	ret += "\n\t</nav>\n"
	return ret

def dashNav(page):
	ret = "<nav id='sub'>"
	if page != "home":
		ret += "<a href='dashboard.cgi' title='home page'>Dashboard</a>"
	ret += "<a href='upload.cgi' title='upload a picture'"
	if page == "upload":
		ret += " class='selected'"
	ret += ">Upload</a>"
	ret += "<a href='albums.cgi'"
	if page == "albums":
		ret += " class='selected'"
	ret += ">My Albums</a>"
	ret += "<a href='new-album.cgi' title='new album'"
	if page == "new-album":
		ret += " class='selected'"
	ret += ">+Album</a>"
	ret += "<a href='me.cgi' title='view my profile'>Profile</a>"
	ret += "</nav>"
	return ret


baseURL = "https://php.radford.edu/~mbaer2/pictcloud/"
UPLOAD_DIR = "/home/mbaer2/dynamic_php/pictcloud/shed"
