from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
app.static_folder = 'static'
DATABASE = 'db/blog.db'

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Route for the index/main page
@app.route('/')
def index():
    conn = get_db_connection()
    blogs = conn.execute('SELECT id, date, title FROM blog').fetchall()
    conn.close()
    return render_template('index.html', blogs=blogs)

# Route for displaying individual blog post
@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    conn = get_db_connection()
    blog = conn.execute('SELECT * FROM blog WHERE id = ?', (blog_id,)).fetchone()
    conn.close()
    return render_template('blog.html', blog=blog)

if __name__ == '__main__':
    app.run(debug=True)
