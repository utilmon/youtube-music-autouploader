from ytmusicapi import YTMusic

if __name__ == "__main__":

    ytmusic = YTMusic('ytmusic_auth.json')

    ytmusic.upload_song('./Snow Patrol - Chasing cars.mp3')