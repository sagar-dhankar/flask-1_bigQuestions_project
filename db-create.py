# sqllite3 to create a database
import sqlite3

db_locale = 'users.db'

connie = sqlite3.connect(db_locale)
c = connie.cursor() #use to create commands

#command
c.execute(""" 
CREATE TABLE questions
(
	id integer primary key autoincrement,
	title text,
	name text,
	details text
)
""")

#commit the changes
connie.commit()
#close the database
connie.close()
