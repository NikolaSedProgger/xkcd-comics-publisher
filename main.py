from doctest import ELLIPSIS
import os
from sys import api_version
from tokenize import group

from dotenv import load_dotenv
from random import randint

from requests import get, post


def get_comic(image_id):
    url = f'https://xkcd.com/{image_id}/info.0.json'
    response = get(url).json()

    filename = response['title']
    image = get(response['img']).content

    with open(f'{os.path.join("images/", filename)}.png', 'wb') as file:
        file.write(image)

    return response


def get_upload_url(image_title):
    with open(f'{os.path.join("images/", image_title)}.png', 'rb') as file:
        url = 'https://api.vk.com/method/photos.getWallUploadServer'
        params = {
            'access_token': access_token,
            'v': api_version
        }
    response = post(url, params)
    response.raise_for_status()
    return response.json()['response']['upload_url']


def upload_comic_server(image_title, url):
    with open(f'{os.path.join("images/", image_title)}.png', 'rb') as file:
        files = {
            'photo': file,
        }
        response = post(url, files=files).json()
    return response['photo'], response['server'], response['hash']


def save_wall_photo(photo, server, hash):
    
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'access_token': access_token,
        'photo': photo,
        'server': server,
        'hash': hash,
        'v': api_version
    }
    response = post(url, params=params)
    response.raise_for_status()
    return response.json()['response'][0]


def post_comic(message, photo_id, group_id, owner_id):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'access_token': access_token,
        'group_id': group_id,
        'owner_id': f'-{group_id}',
        'from_group': 1,
        'attachment': f"photo{owner_id}_{photo_id['id']}",
        'message': message,
        'v': api_version
    }
    response = post(url, params=params)
    response.raise_for_status()


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    access_token = os.getenv('VK_ACCESS_TOKEN')
    group_id = os.getenv('VK_GROUP_ID')
    owner_id = os.getenv('VK_OWNER_ID')
    api_version = os.getenv('API_VERSION')


    first_comics_id = 1
    response = get('https://xkcd.com/info.0.json')
    if response.status_code == 200:
        last_comics_id = response.json()['num']
    else:
        last_comics_id = 2682
    image_id = randint(first_comics_id, last_comics_id)
    
    comics = get_comic(image_id)
    upload_url = get_upload_url(comics['title'])
    uploaded_comics = upload_comic_server(comics['title'], upload_url)
    photo_id = save_wall_photo(uploaded_comics['photo'], uploaded_comics['server'], uploaded_comics['hash'])

    post_comic(comics['alt'], photo_id, group_id, owner_id)