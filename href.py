#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import re

def GetAllTags(url: str, pattern: str):
    site = requests.get(url)
    if(site.status_code != 200):
        print('err:', site.status_code)
    else:
        site = bs(site.content, 'html.parser')
        site = site.find_all('a')
        for i in site:
            if(re.search(f'{pattern}', i['href'])):
                print(re.search(f'{pattern}', i['href']).string)

url = input('url: ')
pattern = input('regex pattern(case sensitive): ')
GetAllTags(url, pattern)
