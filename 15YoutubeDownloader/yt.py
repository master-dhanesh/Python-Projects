from pytube import YouTube
import os

link = input("enter youtube link here -  ")
yt = YouTube(link)
print("1. Audio")
print("2. Video")
op = int(input())
if op == 1:
    data = yt.streams.filter(only_audio=True).first()
    video = data.download()
    base, ext = os.path.splitext(video)
    print("Downloading...")
    audio = base + '.mp3'
    os.rename(video, audio)

if op == 2:
    data = yt.streams.filter(progressive=True, file_extension='mp4')
    if len(data) < 1:
        print("No Format found that can be downloaded!!!")
    elif len(data) > 1:

        for i, v in enumerate(data):
            print(f'{i}. Resolution = {v.resolution} | codec = {v.codecs}')

        quality = int(input("Enter Quality option: "))
        ys = yt.streams.get_by_itag(data[quality].itag)
        print("Downloading...")
        ys.download()
    else:
        ys = yt.streams.get_by_itag(data[0].itag)
        print("Downloading...")
        ys.download()
