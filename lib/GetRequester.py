import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        with requests.get(self.url) as response:
            response.raise_for_status()
            return response.content

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
