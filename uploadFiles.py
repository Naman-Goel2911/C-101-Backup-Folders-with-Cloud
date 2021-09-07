import dropbox
import os
import shutil

from dropbox.files import WriteMode

class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        local_path = 'C:/Users/goeln/Desktop/School'

        for rootFolder, folders, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite')) 

def main():
    access_token = 'sl.A4CFXvFCJrfQbIXklUa1O_xgZrcc9VocelHiOHS3ybnKEOaCM_ChkeCx27pt4qX7m4phZTQr65KpWo5JnKOX6GmCW5TtHzxUDQK4_tLSB_Moy2weeDr-lJ5v9NHMmgOkVUCt_lQ'
    transferData = TransferData(access_token)

    file_from = input('Enter the file/folder you to be backed up: ')
    file_to = input('Enter the full path to upload to Dropbox: ')


    transferData.upload_file(file_from, file_to)
    print('Files/Folders have been backed up!')

main()