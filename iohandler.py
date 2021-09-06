import requests
import sys

class iohandler:
    def take_input(self):
        sentence = sys.argv[1]
        return sentence

    def make_request(self,sentence):
        raw_data = requests.get(sentence).text
        return raw_data