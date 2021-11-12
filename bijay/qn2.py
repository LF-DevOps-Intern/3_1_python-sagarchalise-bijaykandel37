#!/usr/bin/python3.8
import argparse
import requests
from typing import Text
parser = argparse.ArgumentParser(description='url')
parser.add_argument('--url', type=Text, help='download link')
args= parser.parse_args()

def download(url):
    responses = requests.get(url)
    file = open("thisfile.html", "wb")
    file.write(responses.content)
    file.close()
    print('the file has been saved')

if __name__ == '__main__':
    download(args.url)



