import eyed3, os, random
from eyed3.id3.frames import ImageFrame

SEPARATOR = "!_!_!"


# def set_metadata(path):
#     audiofile = eyed3.load(path)
#
#     author = ""
#
#     if path.__contains__(".mp3"):
#         sys.exit(0)
#
#     file_name = path.replace(".mp3", "")
#
#     len_path = len(file_name) - 1
#
#     for i in range(0, len_path):
#
#         if file_name[len_path - i] == SEPARATOR:
#             break
#
#         author = file_name[len_path - i] + author
#
#     title = file_name.replace(SEPARATOR + author, "")
#     print(title)
#
#     audiofile.tag.artist = author.replace(".Mp3", "")
#     audiofile.tag.title = title.split("/")[len(title.split("/")) - 1]
#
#     with open("coverart.png", "rb") as cover_art:
#         audiofile.tag.image.set(3, cover_art.read(), "image/png")
#
#     audiofile.tag.save()
#
#     os.rename(path, path.replace(SEPARATOR + author, ""))

def set_metadata(path, filename, title, author):

    print(f"path={path}, filename={filename}, title={title}, author={author}")

    if not filename.__contains__(".mp3"):
        return

    for c in ["|", "\\", "//", "/", "*"]:

        if filename.endswith(c):
            filename = filename[-1:]

        if filename.__contains__(c):
            filename = filename.replace(c, "_")

    if filename.__contains__(":"):
        filename = filename.replace(":", " -")

    filename = filename.replace("\"", "'")

    if not os.path.exists(path + os.sep + filename):
        print('Erreur, annulation...')
        print(f"Fichier {path + os.sep + filename} non trouvé...")
        return

    audiofile = eyed3.load(path + os.sep + filename)

    if audiofile.tag is None:
        audiofile.initTag()

    audiofile.tag.artist = author
    audiofile.tag.title = title

    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open("coverart.jpg", "rb").read(), "image/jpeg", description=u"Covert art")
    #audiofile.tag.images.set(ImageFrame.ILLUSTRATION, open("coverart.jpg", "rb").read(), "image/jpeg", description=u"Covert art")

    audiofile.tag.save()

    #os.rename(path + os.sep + filename, path + os.sep + title + ".mp3")

if __name__ == '__main__':
    set_metadata("C:\\Users\\arthu\\Music\\test", "Unity (Acoustic) - Alan x Walkers | Sapphire.mp3", "Unity (Acoustic) - Alan x Walkers", "Sapphire")