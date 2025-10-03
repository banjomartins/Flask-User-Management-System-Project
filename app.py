from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# ✅ Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="", # Enter your database username
    password="", # Enter your database password
    database="user_management" # Create your own database
)
cursor = db.cursor(dictionary=True)

# ----------------------
# 1. Home Page
# ----------------------
@app.route('/')
def home():
    return render_template('home.html')

# ----------------------
# 2. Add User
# ----------------------
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        city = request.form['city']
        hobby = request.form['hobby']

        cursor.execute("INSERT INTO users (user_name, email, city, hobby) VALUES (%s, %s, %s, %s)",
                       (name, email, city, hobby))
        db.commit()
        return redirect(url_for('list_users'))

    return render_template('add_user.html')

# ----------------------
# 3. List Users
# ----------------------
@app.route('/users')
def list_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return render_template('users.html', users=users)

# ----------------------
# 4. View Profile
# ----------------------
@app.route('/user/<int:id>')
def view_user(id):
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    return render_template('profile.html', user=user)

# ----------------------
# 5. Delete User
# ----------------------
@app.route('/delete/<int:id>')
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('list_users'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
