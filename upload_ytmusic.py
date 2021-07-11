""" This script uploads created music files in directories to youtube music library """

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from ytmusicapi import YTMusic
import music_tag
from datetime import date
import os

directories = ["D:\Kwan\Desktop", "D:\Kwan\내 음악"]
# torrent folder is not allowed due to slow download (> 60 s)
ytmusic = YTMusic("ytmusic_auth.json")  # Authentication file
filetypes = [".mp3", "flac", ".wma", ".m4a", ".ogg"]  # only last four elements


def set_tag(fn):
    """ This function sets music tags if empty """
    f = music_tag.load_file(fn)
    title = os.path.splitext(os.path.basename(fn))[0]
    title = title.split("-",1)  # Assumes 'artist - song name' format

    if f["year"].value == 0:
        f["year"] = int(date.today().strftime("%Y"))

    if f["title"].value == "":
        f["title"] = title[-1]

    if f["artist"].value == "":
        f["artist"] = title[0]

    f.save()


def on_created(event):
    """ This function gets executed when a file is created in directories being monitored """
    fn = event.src_path
    print(f"fn is {fn} and extension is {fn[-4:]}")
    if fn[-4:] in filetypes:
        time.sleep(30)  # Wait until download is done
        try:
            set_tag(fn)
            ytmusic.upload_song(fn)
        except:
            print("File does not exist")
            pass


if __name__ == "__main__":

    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive
    )

    my_event_handler.on_created = on_created

    my_observer = Observer()
    for path in directories:
        my_observer.schedule(my_event_handler, path, recursive=True)

    my_observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
