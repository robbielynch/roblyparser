import requests
import re
from tokeniser import Tokens
from html_object import HTMLObject

class RoblyParser(object):

    def __init__(self):
        pass

    def get_html(self, url):
        """
        Function to return the HTML content of a url
        """
        headers = {'Accept':'text/css,*/*;q=0.1',
            'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding':'gzip,deflate,sdch',
            'Accept-Language':'en-US,en;q=0.8',
            'User-Agent':'Mozilla/5 (Windows 7) Gecko'}
        res = requests.get(url, headers=headers)
        string = str(res.content).replace('\\n', "")

        return string.rstrip()


    def get_webpage_as_object(self, url):
        html = self.get_html(url)
        tokeniser = Tokens()
        tokens = tokeniser.tokenise(html)
        objectifier = HTMLObject()
        objectifier.tokens_to_html_object(tokens)
        return objectifier