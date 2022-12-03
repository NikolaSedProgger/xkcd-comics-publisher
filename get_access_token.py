from requests import get
from dotenv import load_dotenv
import os


def get_access_token(client_id):
    url = 'https://oauth.vk.com/authorize'
    params = {
        'client_id': client_id,
        'scope':'photos,groups,wall',
        'response_type': 'token'
    }
    response = get(url, params)
    return response.url


if __name__ == '__main__':
    load_dotenv()
    client_id = os.getenv('VK_CLIENT_ID')
    print(get_access_token(client_id))