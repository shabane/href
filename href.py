#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import re
import argparse

# creating CLI
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, required=True, help='the url of the page')
parser.add_argument('-p', '--pattern', type=str, required=False, help='regex pattern(case sensitive)')

args = parser.parse_args()

url = args.url

pattern = args.pattern
if(pattern == None):
    pattern = '.*'

# finding the all tag a and link's
def GetAllTags(url: str, pattern: str):
    site = requests.get(url)
    if(site.status_code != 200):
        print('err:', site.status_code)
    else:
        site = bs(site.content, 'html.parser')
        site = site.find_all('a')
        for i in site:
            if(re.search(f'{pattern}', i['href'], re.IGNORECASE)):
                print(re.search(f'{pattern}', i['href'], re.IGNORECASE).string)

GetAllTags(url, pattern)