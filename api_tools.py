import requests
import os
import urllib, urllib.parse

class Data_Source:
    """Create a data source linking to an API, including the appropriate API key."""
    def __init__(self, source, path, values):
        self.source = source
        self.path = path
        self.values = values

    def build_url(self)
        urlvals = ''
        if values:
            urlvals = {urllib.parse.urlencode(self.values)}
        return f"{self.source}{self.path}{urlvals}"

    def get_response(self)
        url = self.build_url()
        return requests.get(url)


