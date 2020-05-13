import easygui
from moviepy.editor import *

Video_url = easygui.fileopenbox() #選擇Video檔案路徑
FileName=Video_url.split('\\') #字串切割
Music_Name=FileName[-1] 
Music_Name=Music_Name[:-4] #音樂檔名

video = VideoFileClip(Video_url)
video.audio.write_audiofile('{}.mp3'.format(Music_Name)) #Convert MP4 to MP3
