from flask import Flask, request, render_template, send_file
from main import main, question
import sqlite3
import os
import yt_dlp

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
    global url
    global video_title
    url = request.form['url'] 
    result, link, video_id, video_title = main(url)
    with sqlite3.connect("database.db") as users:
        cursor = users.cursor()
        cursor.execute('INSERT INTO CONTENT (video_id, video_title, summary) VALUES (?,?,?)', (video_id, video_title, result))
    return render_template('result.html', result=result, link = link)

@app.route('/result', methods=['POST'])
def result():
    text = request.form['ytfollowup']
    result, link = question(text)
    return render_template('result.html', result = result, link = link)

@app.route('/download')
def download():
    download_dir = "downloads"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    global url
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4',  
        'outtmpl': os.path.join(download_dir, '%(title)s.mp4')  
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)  # Extract video info and download
        file_path = os.path.join(download_dir, f"{info['title']}.{info['ext']}")
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
