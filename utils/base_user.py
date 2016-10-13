import requests
from base import config


class User(object):

    def get_access_token(self, username=config.EMAIL, password=config.PASSWORD):
        payload = {
            "grant_type": "password",
            "username": username,
            "password": password
        }
        r = requests.post(url=config.HOST+config.TOKEN_URL, data=payload)
        return r.json()['access_token']
