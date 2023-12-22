import sqlite3
import csv  # If your data is in a CSV file

# Connect to the SQLite database
conn = sqlite3.connect('../db/blog.db')
cursor = conn.cursor()

# Read content from CSV file and insert into the 'blog' table
with open('../csvs/blog3.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row if exists
    for row in reader:
        date, title, article = row
        cursor.execute('''
            INSERT INTO blog (date, title, article)
            VALUES (?, ?, ?)
        ''', (date, title, article))

# Commit changes and close connection
conn.commit()
conn.close()
