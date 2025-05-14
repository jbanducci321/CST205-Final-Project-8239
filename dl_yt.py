'''
Function to download videos given a url.
CST-205
Developed two functions, download_video and download_audio that utilize the yt_dlp library.
Using the os library it will download videos to the users' 'Downloads' path.
5/13/25
Joshua Sumagang
'''
import yt_dlp
import os
import time

def download_video(url):
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    print(f"Saving to: {downloads_path}")  # Confirm path

    def on_progress(d):
        if d['status'] == 'finished':
            filename = d['filename']
            print(f"Download completed: {filename}")
            # Touch the file to update its timestamp
            current_time = time.time()
            os.utime(filename, (current_time, current_time))

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        'progress_hooks': [on_progress]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])



def download_audio(url):
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    print(f"Saving to: {downloads_path}")  # Confirm path

    def on_progress(d):
        if d['status'] == 'finished':
            filename = d['filename']
            print(f"Download completed: {filename}")
            # Touch the file to update its timestamp
            current_time = time.time()
            os.utime(filename, (current_time, current_time))

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        'progress_hooks': [on_progress]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
