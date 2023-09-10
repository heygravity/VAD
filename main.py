import os
import googleapiclient.discovery
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Set your YouTube API Key here
YOUTUBE_API_KEY = 'AIzaSyBRv4TpS5c3HK_P5aL3z0XXAdVWHdiLJU0'

# Create a YouTube API client
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Function to search for videos
def search_videos(query):
    request = youtube.search().list(
        q=query,
        type='video',
        part='id,snippet',
        maxResults=10  # You can adjust this number
    )
    response = request.execute()
    return response.get('items', [])

# Function to download and extract audio from a video
def download_and_extract_audio(video_id):
    yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    video_stream = yt.streams.get_highest_resolution()
    video_filename = f"static/video/video.mp4"
    video_stream.download(filename=video_filename)

    video_clip = VideoFileClip(video_filename)
    audio_clip = video_clip.audio

    audio_filename = f"static/audio/audio.mp3"
    audio_clip.write_audiofile(audio_filename)

    video_clip.close()
    audio_clip.close()
    video_clip.reader.close()
    video_clip.audio.reader.close_proc()
    video_clip.reader = None
    video_clip.audio.reader = None
    yt.close()

    print("Audio extraction complete.")
    return audio_filename
