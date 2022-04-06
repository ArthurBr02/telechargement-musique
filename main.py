import os
import youtube_dl_fonctions

import requests as requests

from metadata import _metadata as metadata
import yt_dlp as youtube_dl

from PIL import Image

playlists = []

url = ""

choix = 1

exists = False

while choix == 1:

    url = str(input("URL d'une playlist: "))

    while not url.__contains__("https://www.youtube.com/playlist?list="):
        url = str(input("URL d'une playlist: "))

    playlists.append(url)

    choix = int(input("Voulez-vous saisir une autre playlist (1 = oui, 0 = non) ? : "))

    while choix not in [0, 1]:
        choix = int(input("Voulez-vous saisir une autre playlist (1 = oui, 0 = non) ? : "))

if len(playlists) > 0:
    path = str(input("Chemin où les pistes doivent être téléchargées: "))

for playlist in playlists:

    with youtube_dl.YoutubeDL({"ignoreerrors": True, "quiet": True}) as ydl:
        playlist_dict = ydl.extract_info(playlist, download=False)

    # Pretty-printing the video information (optional)
    for video in playlist_dict["entries"]:

        if not video:
            print("ERROR: Unable to get info. Continuing...")
            continue

        p = path + os.sep + video['title'] + ".mp3"

        for c in ["|", "\\", "/"]:
            if p.__contains__(c):
                p.replace(c, "_")

        files = os.listdir(path)

        exists = False

        for file in files:

            if file.title().upper() == (video['title'] + ".mp3").upper():
                exists = True
                break

        if exists is False:
            url = video['thumbnail']
            r = requests.get(url, allow_redirects=True)

            open('coverart.png', 'wb').write(r.content)
            cover_art = Image.open(r'coverart.png')
            cover_art_im = cover_art.convert('RGB')
            cover_art_im.save(r'coverart.jpg')

            # youtube_dl_fonctions.downloadYt("https://www.youtube.com/watch?v=" + video['id'], f'{path + os.sep}%(title)s{metadata.metadata.SEPARATOR}%(channel)s.%(ext)s')
            # metadata.metadata.set_metadata(path + os.sep + video['title'] + metadata.metadata.SEPARATOR + video['channel'] + ".mp3")

            youtube_dl_fonctions.downloadYt("https://www.youtube.com/watch?v=" + video['id'],
                                            f'{path + os.sep}%(title)s.%(ext)s')

            metadata.set_metadata(path,
                                  video['title'] + ".mp3",
                                  video['title'], video['channel'])

            print(
                f"La vidéo {video['title']} de {video['channel']} a bien été téléchargée et formatée, passage à la suivante...")

        else:
            print(f"La vidéo {video['title']} de {video['channel']} est déjà téléchargée, passage à la suivante...")

        print()

if os.path.exists("coverart.jpg"):
    os.remove('coverart.jpg')
    os.remove('coverart.png')
