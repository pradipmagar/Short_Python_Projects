import yt_dlp

#Enter the url for the download
url = input("Enter Video url:")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
                
print("Video Downloaded Successfully!")