import os

from dotenv import load_dotenv
from random import randint

from requests import get, post


def get_comics(image_id):
    url = f'https://xkcd.com/{image_id}/info.0.json'
    response = get(url)
    response.raise_for_status()

    filename = response.json()['title']
    image = get(response.json()['img']).content

    with open(f'images/{filename}.png', 'wb') as file:
        file.write(image)

    return response.json()


def get_upload_url(image_title):
    with open(f'images/{image_title}.png', 'rb') as file:
        url = 'https://api.vk.com/method/photos.getWallUploadServer'
        params = {
            'access_token': os.getenv('ACCESS_TOKEN'),
            'v': os.getenv('API_VERSION')
        }
    response = post(url, params)
    response.raise_for_status()
    return response.json()['response']['upload_url']


def upload_comics_server(image_title, url):
    with open(f'images/{image_title}.png', 'rb') as file:
        files = {
            'photo': file,
        }
        response = post(url, files=files)
        response.raise_for_status()
    return response.json()


def save_wall_photo(image_title, url):
    uploaded_comics = upload_comics_server(image_title, url)
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'access_token': os.environ['ACCESS_TOKEN'],
        'photo': uploaded_comics['photo'],
        'server': uploaded_comics['server'],
        'hash': uploaded_comics['hash'],
        'v': os.environ['API_VERSION']
    }
    response = post(url, params=params)
    response.raise_for_status()
    return response.json()['response'][0]


def post_comics(message, photo_id, group_id):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'access_token': os.environ['ACCESS_TOKEN'],
        'group_id': int(group_id),
        'owner_id': -int(group_id),
        'from_group': 1,
        'attachment': f"photo519047993_{photo_id['id']}",
        'message': message,
        'v': os.environ['API_VERSION']
    }
    response = post(url, params=params)
    response.raise_for_status()


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    first_comics_id = 1
    last_comics_id = get('https://xkcd.com/info.0.json').json()['num']
    image_id = randint(first_comics_id, last_comics_id)
    
    comics = get_comics(image_id)
    image_title = comics['title']
    upload_url = get_upload_url(image_title)
    photo_id = save_wall_photo(image_title, upload_url)

    post_comics(comics['alt'], photo_id, os.getenv('GROUP_ID'))