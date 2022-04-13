import pytube, os

link = input("Provide a youtube link to download: ")
try:
  url = pytube.YouTube(str(link))
except:
  print(f"I could not fetch that video")
  os._exit(0)
video = url.streams.get_highest_resolution()
try:
  video.download(filename = f"videos/{url.title}.mp4")
except Exception as e:
  print(f"I couldnt download this video: {e}")
  os._exit(0)