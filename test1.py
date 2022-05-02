from pytube import YouTube


SAVE_PATH = "dowloaded"
#ask for the link from user
link = "https://www.youtube.com/watch?v=6cB6oJWqwo4"
yt = YouTube(link)

#highest Resolution
ys = yt.streams.get_highest_resolution()
ys.download(SAVE_PATH)
print("fin du procecus...")