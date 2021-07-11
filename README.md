# How to run script in Windows

1. Install required packages by `pip install -r requirements.txt`
2. Create a folder where the files will be stored (e.g. Documents)
3. Copy paste upload_ytmusic.py, upload_ytmusic.cmd, and ytmusic_auth.json into the created folder
4. Create a shortcut to the cmd file and paste into the startup folder

# Creating ytmusic_auth.json
- See https://ytmusicapi.readthedocs.io/en/latest/setup.html#authenticated-requests
- Note setup command should be called as `YTMusic.setup(filepath='ytmusic_auth.json')`