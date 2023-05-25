from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import os

window = Tk()
window.geometry("700x350")
window.title("Youtube Downloader")
window.iconbitmap(
    r"D:\Working_Material\python_dev\Python_Projects\15YoutubeDownloader\logo.ico")


e = Entry(window, width=50)
e.pack()


def linkinput():
    link = e.get()
    yt = YouTube(link)

    def radioClicked(op):
        if op == 1:
            data = yt.streams.filter(only_audio=True).first()
            video = data.download()
            base, ext = os.path.splitext(video)
            # print("Downloading...")
            audio = base + '.mp3'
            os.rename(video, audio)
            response = messagebox.askyesno("Downlaoding Status",
                                           "Downloading Successfull.")
            if response:
                # window.destroy()
                window.quit()

        if op == 2:
            data = yt.streams.filter(progressive=True, file_extension='mp4')
            if len(data) < 1:
                print("No Format found that can be downloaded!!!")
            elif len(data) > 1:

                def radioQuality(quality):
                    ys = yt.streams.get_by_itag(data[quality].itag)
                    # print("Downloading...")
                    ys.download()
                    response = messagebox.askyesno("Downlaoding Status",
                                                   "Downloading Successfull.")
                    if response:
                        # window.destroy()
                        window.quit()

                s = IntVar()
                # s.set(2)

                for i, v in enumerate(data):
                    Radiobutton(window, text=f'{i}. Resolution = {v.resolution} | codec = {v.codecs}', variable=s, value=i,
                                command=lambda: radioQuality(s.get())).pack()
            else:
                ys = yt.streams.get_by_itag(data[0].itag)
                # print("Downloading...")
                ys.download()
                response = messagebox.askyesno("Downlaoding Status",
                                               "Downloading Successfull.")
                if response:
                    # window.destroy()
                    window.quit()

    r = IntVar()
    # r.set(2)

    Radiobutton(window, text="1. Audio", variable=r, value=1,
                command=lambda: radioClicked(r.get())).pack()
    Radiobutton(window, text="2. Video", variable=r, value=2,
                command=lambda: radioClicked(r.get())).pack()
    print("1. Audio")
    print("2. Video")


getLinkbtn = Button(
    window, text="Enter Copied YouTube Link", command=linkinput)
getLinkbtn.pack()

window.mainloop()
