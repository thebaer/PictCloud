#!/usr/bin/python
import MySQLdb

class DB:
	# this.cur

	def __init__(self):
		return

	# connect: -> cursor
	def connect(self):
		try:
			import MySQLdb
			self.db = MySQLdb.connect("host", "user","pass","database")
			self.cur = self.db.cursor()
			return True
		except ImportError:
			print "<p style='color:red;font-style:italic'>Sorry, there was an error hooking up with the database.</p>"
		
		return False

	def getRow(self, query):
		self.cur.execute(query)
		row = self.cur.fetchone()
		return row

	def insert(self, table, fields):
		q = "INSERT INTO %s (" % table
		q += ", ".join(fields.keys())
		q += ") VALUES ("
		for field, val in fields.items():
			if val is None:
				fields[field] = 'NULL'
			elif val.isdigit() or val == "NULL":
				fields[field] = val
			else:
				fields[field] = "'" + val + "'"
		q += ", ".join(fields.values())
		q += ")"
		try:
			self.cur.execute(q)
			return True
		except:
			return False

	def update(self, table, fields, where):
		q = "UPDATE %s SET " % table
		qFields = []
		for field, val in fields.items():
			if val.isdigit() or val == "NULL":
				qFields.append(field + "=" + val)
			else:
				qFields.append(field + "='" + val + "'")
		q += ", ".join(qFields)
		q += " WHERE " + where
		self.cur.execute(q)
	
	def query(self, query):
		self.cur.close()
		self.cur = self.db.cursor(MySQLdb.cursors.DictCursor)
		self.cur.execute(query)
		return self.cur.fetchall()

	def rowcount(self):
		return self.cur.rowcount


