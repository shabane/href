#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import re
import argparse
import json
import sys

# creating CLI
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", type=str, required=True, help="the url of the page")
parser.add_argument(
    "-p", "--pattern", type=str, required=False, help="regex pattern(case sensitive)"
)
parser.add_argument("-l", "--load-headers", help="load header from file")

args = parser.parse_args()

url = args.url

pattern = args.pattern
if pattern == None:
    pattern = ".*"

if args.load_headers != None:
    with open("headers", "r") as fli:
        fli = json.load(fli)
        if type(fli) != dict:
            print("err: the header file should be a json file", file=sys.stderr)
        elif type(fli) == dict:
            headers = fli
else:
    headers = {}


# finding the all tag a and link's
def GetAllTags(url: str, pattern: str):

    site = requests.get(url, headers=headers)

    if site.status_code != 200:
        print("err:", site.status_code, file=sys.stderr)
    else:
        site = bs(site.content, "html.parser")
        site = site.find_all("a")
        for i in site:
            try:
                if re.search(f"{pattern}", i["href"], re.IGNORECASE):
                    print(re.search(f"{pattern}", i["href"], re.IGNORECASE).string)
            except:
                pass


GetAllTags(url, pattern)
