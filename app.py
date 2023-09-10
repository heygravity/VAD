from flask import Flask, render_template, request
from main import search_videos, download_and_extract_audio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        videos = search_videos(query)
        return render_template('index.html', videos=videos)
    return render_template('index.html', videos=[])

@app.route('/play/<video_id>')
def play(video_id):
    audio_filename = download_and_extract_audio(video_id)
    return render_template('play.html', audio_filename=audio_filename)

@app.route('/download/<video_id>')
def download(video_id):
    audio_filename = download_and_extract_audio(video_id)
    return render_template('index.html', videos=[], audio_filename=audio_filename)

if __name__ == '__main__':
    app.run(debug=True)
