'''
Python Challenge:
 Get Youtube video title and view count
'''
# pip install pytube

from pytube import YouTube

def get_view_count(video):
    info = YouTube(video)
    author = info.author
    title = info.title
    views = info.views
      
    return author, title, views

# test the code
video = "https://www.youtube.com/watch?v=eMmmIHG0j6w&t=326s"
channel, title, view = get_view_count(video)
print(f'Channel name:{channel}')
print(f'Title:{title}')
print(f'View count: {view}')