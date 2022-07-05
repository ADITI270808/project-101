import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)


def main():
    access_token ='sl.BK1_BzRdudbaMhKjO_wWz0hbzFoxXiEzOhV__goVK2Z-QZfSk46wAi42FSH7kzYl91SwshOuqC-YeGB4lPMsb569G2WzL3tjND9bX2Y6iYYJe_iCofHnuiXsiqqvis4vGotov_WLj7E_'
    
    transferData = TransferData(access_token)
    file_from ='abcd.txt'
    file_to = '/test_dropbox/abcd.txt'


    transferData.upload_file(file_from, file_to)

main()