# Youtube Music Autouploader
Youtube music allows to stream uploaded local music files without subscription. This script monitores set directories and uploads created/downloaded music files in the directories to Youtube music library automatically.

# Installation
1. Install required packages by `pip install -r requirements.txt`
2. Create authentication file `ytmusic_auth.json`
    - See https://ytmusicapi.readthedocs.io/en/latest/setup.html#authenticated-requests
    - Note setup command should be called as `YTMusic.setup(filepath='ytmusic_auth.json')`
3. Open `upload_ytmusic.py` and configure line 11 and 13
    - `directories` is a list of directories to be monitored
    - `fill-empty-tag` (boolean) will decide to populate empty music tags (year, title, artist) before uploading, assuming the music file name has a form artist-title
## For Windows

4. Create a shortcut to the cmd file and paste into the startup folder

## For Mac
- See https://stackoverflow.com/questions/6442364/running-script-upon-login-mac


