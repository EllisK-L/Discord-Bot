import requests
import base64
import os

async def getImage(text):
    url = "http://172.29.253.125:8080/dalle"
    save_folder = "dalle_imgs"

    obj = {
        "text":text,
        "num_images":1
    }
    headers = {
        'Bypass-Tunnel-Reminder': "go",
        'mode': 'no-cors'
    }
    x = requests.post(url, json=obj, headers=headers)
    if save_folder is not None:
        if not os.path.exists(save_folder):
            os.mkdir(save_folder)
        filename = os.path.join(save_folder, ''.join(e for e in text if e.isalnum()) + ".png" )
        decodeit = open(filename, 'wb')
        decodeit.write(base64.b64decode((x.json()[0])))
        decodeit.close()
    return filename

if __name__ == "__main__":
    getImage("counterstrike")