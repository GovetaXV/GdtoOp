from openload import OpenLoad
import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def upload(file):
    ol = OpenLoad(idx, key)
    
    uploaded_file_info = ol.upload_file(file)
    return uploaded_file_info



#file_id = input('Gdrive ID: ')
#destination = input('Filename: ')


file_id = '15XoMFI_2R8e0iDHx8b313Zv3whyEQuES'
destination = 'Summer Wars.mkv'

print('Download has started')
download_file_from_google_drive(file_id, destination)
print('Upload has started')
print(upload(destination))
