from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# Landing page
@app.route("/")
def landing():
    conn = sqlite3.connect("task_database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()

    conn2 = sqlite3.connect("task_database.db")
    c2 = conn2.cursor()
    c2.execute("SELECT * FROM tasks WHERE status='pending'")
    tasks2 = c2.fetchall()
    conn2.close()

    return render_template("landing.html", tasks=tasks, tasks2=tasks2)
    

# Add a new job
@app.route('/addjob', methods=['POST'])
def addjob():
    job_code = request.form['job_code']
    chargeable = request.form['chargeable']
    work_description = request.form['work_description']
    urgency = request.form['urgency']
    status = 'pending'

    conn = sqlite3.connect('task_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (job_code, chargeable, work_description, urgency, status) VALUES (?, ?, ?, ?, ?)", (job_code, chargeable, work_description, urgency, status))
    conn.commit()
    conn.close()

    job = {'job_code': job_code, 'chargeable': chargeable, 'work_description': work_description, 'urgency': urgency, 'status': status}

    return redirect(url_for('landing'))

# Mark a job as complete
@app.route("/markcomplete", methods=["POST"])
def markcomplete():
    job_code = request.form["job_code"]
    
    conn = sqlite3.connect("task_database.db")
    c = conn.cursor()
    c.execute("UPDATE tasks SET status='completed' WHERE job_code=?", (job_code,))
    conn.commit()
    conn.close()

    job = {'job_code': job_code, 'status': 'completed'}

    return redirect(url_for('landing'))

# Job list page
@app.route("/joblist")
def joblist():
    conn2 = sqlite3.connect("task_database.db")
    c2 = conn2.cursor()
    c2.execute("SELECT * FROM tasks WHERE status='pending'")
    tasks2 = c2.fetchall()
    conn2.close()

    return render_template("joblist.html", tasks2=tasks2)

if __name__ == '__main__':
    app.run(debug=True, host="192.168.16.163", port=5000)






