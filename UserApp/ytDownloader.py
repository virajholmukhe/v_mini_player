from pytube import YouTube
from pytube.request import filesize


def downloadSong(link):
    yt = YouTube(link)
    yt_stream = yt.streams.filter(
        progressive=False, only_audio=True).get_by_itag('251').download(output_path='static/files/webm', filename='audio.mp3')
    return (f'static/files/webm/audio.mp3')


""" link = 'https://www.youtube.com/watch?v=JRfuAukYTKg'
downloadSong(link) """
