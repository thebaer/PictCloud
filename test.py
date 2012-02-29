#!/usr/bin/python

import MySQLdb

def login(user, passw):
	db = MySQLdb.connect("php.radford.edu", "mbaer2","moldycheese","mbaer2")
	cur = db.cursor()
	cur.execute("SELECT uid FROM users WHERE username = '"+user+"' AND password = PASSWORD('"+passw+"')")
	row = cur.fetchone()
#	cur.close()
#	db.close()
	if row == None:
		return False
	else:
		return row[0]
#	return cur.rowcount > 0

print login("admin", "cheese")

#db = MySQLdb.connect("php.radford.edu", "mbaer2","moldycheese","mbaer2")
#cur = db.cursor()
#cur.execute("SELECT * FROM users")
#row = cur.fetchone()
#print "result: ", row[1]
#cur.close()
#db.close()
