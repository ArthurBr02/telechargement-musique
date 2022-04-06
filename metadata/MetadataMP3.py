import eyed3, os, sys

SEPARATOR = str(input("Separator: "))
playlist = bool(input("Playlist ('True' or 'False'): "))

if playlist:
    path = input("Path of the playlist directory: ")
else:
    path = input("Path of the file: ")

    if not path.__contains__(SEPARATOR):
        sys.exit(0)

if not playlist:

    audiofile = eyed3.load(path)

    author = ""

    if path.__contains__(".mp3"):
        sys.exit(0)

    file_name = path.replace(".mp3", "")

    len_path = len(file_name) - 1

    for i in range(0, len_path):

        if file_name[len_path - i] == SEPARATOR:
            break

        author = file_name[len_path - i] + author

    title = file_name.replace(SEPARATOR + author, "")
    print(title)

    audiofile.tag.artist = author.replace(".Mp3", "")
    audiofile.tag.title = title.split("/")[len(title.split("/")) - 1]
    audiofile.tag.save()

    os.rename(path, path.replace(SEPARATOR + author, ""))
else:
    files = os.listdir(path)
    print(files)
    for f in files:

        if path.endswith("/"):
            p = path + f.title()
        else:
            p = path + "/" + f.title()

        audiofile = eyed3.load(p)

        author = ""

        if p.__contains__(".mp3"):
            file_name = p.replace(".mp3", "")
        elif p.__contains__(".Mp3"):
            file_name = p.replace(".mp3", "")
        else:
            continue

        len_path = len(file_name) - 1

        for i in range(0, len_path):

            if file_name[len_path - i] == SEPARATOR:
                break

            author = file_name[len_path - i] + author

        title = file_name.replace(SEPARATOR + author, "")
        print(title)

        audiofile.tag.artist = author.replace(".Mp3", "")
        audiofile.tag.title = title.split("/")[len(title.split("/")) - 1]
        audiofile.tag.save()

        os.rename(p, p.replace(SEPARATOR + author, "") + ".mp3")
