import bs4
import requests
import os
from time import sleep

# 画像が載ってるURL
URL = "https://projectpokemon.org/home/docs/spriteindex_148/switch-sv-style-sprites-for-home-r153/"

# ファイルパスの取得
base = os.path.dirname(os.path.abspath(__file__))
destdir = os.path.join(base, '.\\sprites_SV_Home')

html = requests.get(URL)
sleep(1)
soup = bs4.BeautifulSoup(html.content, 'html.parser')

images = soup.find_all('img')

imagelinks = []

for image in images:
    imagelink = image.get('src')
    if '_f' in imagelink:
        continue
    elif 'sprites-models' not in imagelink:
        continue
    else:
        imagelinks.append(imagelink)

for imagelink in imagelinks:
    response = requests.get(imagelink)
    image = response.content
    sleep(1)
    imgname = imagelink.removeprefix('https://projectpokemon.org/images/sprites-models/sv-sprites-home/')
    imgpath = os.path.join(destdir, '.\\' + imgname)
    with open(imgpath, 'wb') as f:
        f.write(image)
    print(f'Downloaded {imgname}.')