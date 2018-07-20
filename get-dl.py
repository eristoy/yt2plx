#!/usr/bin/env python3

from __future__ import unicode_literals
import youtube_dl,sys,os,shutil,re

if len(sys.argv) == 1:
    print ('Usage: get-dl.py youtubeurl')
    sys.exit(1)
yURL=sys.argv[1]

class MyLogger(object):
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting...')

ydl_opts = {
    'writethumbnail': True,
    'restrictfilesnames': True,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }, {
        'key': 'EmbedThumbnail',
        'already_have_thumbnail': True
    }, {
        'key': 'MetadataFromTitle',
        'format_to_regex': False
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],

}

workingDir ='/Users/eric/working'
plxDir = '/Volumes/Media'
os.chdir(workingDir)
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([yURL])

mFile=''
tFile=''
dirList = os.listdir(workingDir)
mySrc=''
myDst=''
for file in dirList:
    if file.endswith('.mp3'):
        #mFile=file
        #mySrc = workingDir + "/" + mFile
        #myDst = plxDir +"/" + mFile
        shutil.move(file,plxDir)
    if file.endswith('.jpg'):
        tFile = file
        os.remove(tFile)

