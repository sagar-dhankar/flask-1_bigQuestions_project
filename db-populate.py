# sqllite3 to create a database
import sqlite3

db_locale = 'users.db'

connie = sqlite3.connect(db_locale)
c = connie.cursor() #use to create commands

#command
c.execute(""" 
INSERT INTO questions (title, name, details) VALUES
('WHAT IS THE USE OF QUORA', 'MR. THINKER', 'I AM HUGE EXCITED TO KNOW THE PURPOSE TO USING QUORA'),
('IS HISTORY MATTERS','MR. YOGI','MODERN HISTORY IS DIFFERENT FROM ACTUAL HISTORY, IS YOUTH OF INDIA IS THINKING OF IT OR GOVERNMENT IS NOT ALLOWING THE REVOLUTION')
""")

#commit the changes
connie.commit()
#close the database
connie.close()
