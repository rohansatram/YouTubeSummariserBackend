from flask import Flask, request, render_template, jsonify, url_for
from main import main, question
import sqlite3
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__, 
    template_folder='path/to/templates',
    static_folder='path/to/static')

connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS CONTENT (video_id TEXT, video_title TEXT, summary TEXT)')

@app.route('/')
def index():
    connect = sqlite3.connect('database.db') 
    cursor = connect.cursor() 
    cursor.execute('SELECT video_title, summary FROM CONTENT') 
    data = cursor.fetchall()
    return render_template('index.html', data = data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/process', methods=['POST'])
def process():
    url = request.form['url'] 
    result, link, video_id, video_title = main(url)   # get video title. then put video title, result, video_id and date into the db. then make a query to get everything from the db
    with sqlite3.connect("database.db") as users:
        cursor = users.cursor()
        cursor.execute('INSERT INTO CONTENT (video_id, video_title, summary) VALUES (?,?,?)', (video_id, video_title, result))
    return render_template('result.html', result=result, link = link)

@app.route('/result', methods=['POST'])
def result():
    text = request.form['ytfollowup']
    result, link = question(text)
    return render_template('result.html', result = result, link = link)

if __name__ == '__main__':
    app.run(debug=True)
