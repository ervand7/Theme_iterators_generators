import requests

WIKI_API_URL = 'https://en.wikipedia.org/w/api.php'
BASE_REQUEST_PARAMS = {
    'action': 'opensearch',
    'search': '',
    'prop': 'info',
    'format': 'json',
    'inprop': 'url'
}


class Wiki:
    api_url = WIKI_API_URL
    request_params = BASE_REQUEST_PARAMS

    def __init__(self, find_name=''):
        self.find_name = find_name
        self.request_params['search'] = find_name

    def get_wiki_data(self):
        response = requests.get(self.api_url, params=self.request_params)
        return response.json()[-1][0]
