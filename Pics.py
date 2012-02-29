#!/usr/bin/python

def getAlbums(dbObj, author_id):
	return dbObj.query("SELECT aid, title, (SELECT COUNT(*) FROM photos WHERE album_id = aid) AS numPics FROM albums WHERE author_id = %s" % author_id)

def getLinkPic(filename):
	# should be inside <div id='gallery'[ class='quack']>
	# if including more info (don't want this floated, don't put in div#gallery
	return "<a href='photo.cgi?file=%s'><img class='moment' src='view.cgi?file=%s' /></a>" % (filename, filename)

