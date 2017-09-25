import json
import requests
import requests_cache

requests_cache.install_cache('sfgov', backend='sqlite', expire_after=300)

class FoodTruckApi:

    def __init__(self):
        self.url = 'http://data.sfgov.org/resource/bbb8-hzi6.json'
        self.data = None

    def get(self, url = None):
        if url is not None:
            self.url = url

        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            raise Exception('API Response error')
        return self.data