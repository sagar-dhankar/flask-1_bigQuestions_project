# sqllite3 to create a database
import sqlite3

db_locale = 'users.db'

connie = sqlite3.connect(db_locale)
c = connie.cursor() #use to create commands

#command
c.execute(""" 
SELECT * FROM questions
""")

#command to print the result
user_info = c.fetchall()
print(user_info)

#commit the changes
connie.commit()
#close the database
connie.close()
