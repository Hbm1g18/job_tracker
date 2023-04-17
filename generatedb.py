import sqlite3

# Create a connection to the database
conn = sqlite3.connect('task_database.db')

# Create a cursor object
c = conn.cursor()

# Create the tasks table
c.execute('''CREATE TABLE tasks
             (job_code text, chargeable text, work_description text, urgency text, status text)''')

# Commit changes and close the connection
conn.commit()
conn.close()
