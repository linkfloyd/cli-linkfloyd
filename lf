#!/usr/bin/env python3
from shutil import get_terminal_size
from urllib.parse import urljoin
from random import choice

import argparse
import requests

API_URL = 'http://api-linkfloyd.appspot.com/'
terminal_size = get_terminal_size((80, 20))


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def padded_print(text, plist):
    cursor = 0
    idx = 0
    while cursor <= len(text):
        left = plist[idx][0]
        right = plist[idx][1]
        width = terminal_size.columns - (left + right)
        part = text[cursor:cursor + width]
        print((' ' * left) + part)
        cursor += width
        if idx < len(plist) - 1:
            idx += 1


def list_links(options):
    resp = requests.get(API_URL)
    for i, r in enumerate(resp.json()):
        kind = choice(['Resim', 'Müzik', 'Sinema', 'Yazılım', 'Gündem'])
        padded_print('{}) {}{}{}: {}'.format(
            i, Color.WARNING, kind, Color.ENDC, r['title']), [[0, 0],[3, 0]])
        padded_print('{}{}{}'.format(Color.OKBLUE, r['url'], Color.ENDC),
                     [[3, 0], ])
        print()

def insert_link(options):
    url = urljoin(API_URL, 'create/')
    resp = requests.post(url, json={'title': options.title, 'url': options.url})
    return resp


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    subparsers = parser.add_subparsers()

    list_parser = subparsers.add_parser(
        'list', parents=[parser], add_help=False)
    list_parser.set_defaults(func=list_links)

    create_parser = subparsers.add_parser('create', parents=[parser])
    create_parser.add_argument('-t', '--title', type=str, required=True)
    create_parser.add_argument('-u', '--url', type=str, required=True)
    create_parser.set_defaults(func=insert_link)

    options = parser.parse_args()
    options.func(options)
