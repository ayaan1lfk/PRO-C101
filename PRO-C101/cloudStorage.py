import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from,"rb") as f:
            dbx.files_upload(f.read(),file_to)
def main():
    access_token = "sl.A3lVx92664aQxmDTl_7t6puvnOfpWJYWAMFE5_YiRG0gqokzSzZL0oaZGv2ZnsbeoCK6E7tFWI-q7IiJM0g69wXo1qojsNIJI2Jf1KBjf4xPpgNiPk2zwkEnSnFSStCR9dfgxcI"
    transferData = TransferData(access_token)
    file_from = "C:/Users/sdaga/Desktop/Python/c101/sample.txt"
    file_to = "/Apps app/sample.txt"
    transferData.upload_file(file_from,file_to)
    print("file has been moved")

main()