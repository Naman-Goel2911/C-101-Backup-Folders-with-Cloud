import dropbox
import os
import shutil

from dropbox.files import WriteMode

class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for rootFolder, folders, files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(rootFolder, fileName)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, fileName)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite')) 

def main():
    access_token = 'sl.A4NXMsNNZd0Zr1pzsVR3sleOMaNNAxARK8vu5dV_nUH4X6ZLTrG3At2cvgGdv_fLLtNziHxnVEf9PJlhpwc9baWo_OKO7hLbEw1w0VO1ma9BKXQ1WfjTdMjVLvXy1rRbRBY4NXs'
    transferData = TransferData(access_token)

    file_from = str(input('Enter the file/folder you to be backed up: '))
    file_to = input('Enter the full path to upload to Dropbox: ')


    transferData.upload_file(file_from, file_to)
    print('Files/Folders have been backed up!')

main()