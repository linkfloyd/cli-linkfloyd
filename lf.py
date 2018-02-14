#!/usr/bin/env python3

import argparse
import requests

from urllib.parse import urljoin
from tabulate import tabulate

API_URL = 'http://api-linkfloyd.appspot.com/'

def list_links(options):
    resp = requests.get(API_URL)
    return tabulate([(r['title'], r['url']) for r in resp.json()])

def insert_link(options):
    url = urljoin(API_URL, 'create/')
    resp = requests.post(url, data={'title': options.title,
                                    'url': options.url})
    return resp

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers()

    list_parser = subparsers.add_parser(
        'list', parents=[parser], add_help=False)
    list_parser.set_defaults(func=list_links)

    create_parser = subparsers.add_parser(
        'create', parents=[parser])
    create_parser.add_argument('-t', '--title', type=str, required=True)
    create_parser.add_argument('-u', '--url', type=str, required=True)
    create_parser.set_defaults(func=insert_link)
    
    options = parser.parse_args()
    print(options.func(options))