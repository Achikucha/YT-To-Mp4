from pytubefix import YouTube
#Input Youtube URL that you want to download

url = input('')
YouTube(url).streams.first().download()
