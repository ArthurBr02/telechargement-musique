from __future__ import unicode_literals

import os

import yt_dlp as youtube_dl
import platform


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
    # if d['status'] == 'downloading':
    #    print("Speed: ", float(d['speed'])/8/1000)
    #    time.sleep(1)
    #    cls()


# ydl_opts = {
#    'format': 'bestaudio/best',
# 'postprocessors': [{
#    'key': 'FFmpegExtractAudio',
# 'preferredcodec': 'mp3',
# 'preferredquality': '192',
# }],
# 'logger': MyLogger(),
# 'progress_hooks': [my_hook],
# }


# ignoreerrors
# nooverwrites

def downloadYt(url="", output="", choix=0):
    ydl_opts = {}

    # print("DEBUG: choix = ", choix)

    if platform.system() == "Windows":
        if choix == 0:
            ydl_opts = {
                'format': 'bestaudio/best',
                'ignoreerrors': True,
                'overwrites': False,
                'continuedl': True,
                'default_search:': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'logger': MyLogger(),
                'progress_hooks': [my_hook],
                'outtmpl': output,
                'ffmpeg_location': 'ffmpeg/ffmpeg.exe'
            }
        elif choix == 1:
            ydl_opts = {
                'format': 'bestvideo+bestaudio',
                'ignoreerrors': True,
                'overwrites': False,
                'continuedl': True,
                'default_search:': True,
                # 'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': 'mp4',
                }],
                'logger': MyLogger(),
                'progress_hooks': [my_hook],
                'outtmpl': output,
                'ffmpeg_location': 'ffmpeg/ffmpeg.exe'
            }
        else:
            if choix == 0:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'ignoreerrors': True,
                    'overwrites': False,
                    'continuedl': True,
                    'default_search:': True,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'logger': MyLogger(),
                    'progress_hooks': [my_hook],
                    'outtmpl': output,
                }
            elif choix == 1:
                ydl_opts = {
                    'format': 'bestvideo+bestaudio',
                    'ignoreerrors': True,
                    'overwrites': False,
                    'continuedl': True,
                    'default_search:': True,
                    # 'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4',
                    }],
                    'logger': MyLogger(),
                    'progress_hooks': [my_hook],
                    'outtmpl': output,
                }

    youtube_dl.YoutubeDL(ydl_opts).download([url])

    #info_dict = youtube_dl.YoutubeDL(ydl_opts).extract_info(url, download=False)

    #video_title = info_dict.get('title', None)
    #video_author = info_dict.get('channel', None)
    #playlist_name = ""

    #if url.__contains__("playlist"):
    #    playlist_name = info_dict.get('playlist_title', None)

    #output_formatted = output.replace("%(title)s", video_title).replace("%(channel)s", video_author).replace("%(playlist_title)s", playlist_name);

    # if platform.system() == "Windows":
    #     if choix == 0:
    #         os.rename(output_formatted.replace("%(ext)s", "webm"), output_formatted.replace("%(ext)s", "mp3"))
    #     if choix == 1:
    #
    #         video = output_formatted.replace(".%(ext)s", ".f248.webm").replace("|", "-")
    #         audio = output_formatted.replace(".%(ext)s", ".f251.webm").replace("|", "-")
    #
    #         output_mp4 = output_formatted.replace(".%(ext)s", ".mp4")
    #
    #         os.system(f"ffmpeg/ffmpeg.exe ffmpeg -i \"{video}\" -i \"{audio}\" -c:v copy -c:a aac \"{output_mp4}\"")

            #os.rename(output_formatted.replace("%(ext)s", "webm"), output_formatted.replace("%(ext)s", "mp4"))



# downloadYtToMP3('https://www.youtube.com/watch?v=BaW_jenozKc')
