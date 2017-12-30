# -*- coding: utf-8 -*-

import requests

rqs = requests.Session()
DEFAULT_SCHEME = 'https'
DEFAULT_BASE_URL = 'bearychat.com'


def api_url(subdomain, path, scheme=DEFAULT_SCHEME, base_url=DEFAULT_BASE_URL):
    return '{scheme}://{subdomain}.{base_url}/api/{path}'.format(
        scheme=scheme, subdomain=subdomain, base_url=base_url, path=path)


def handle_response(response):
    if response.status_code == 200:
        data = response.json()
        if data['code'] == 0:
            return True, data['result']
        else:
            return False, data['error']
    else:
        try:
            data = response.json()
            return False, data['error']
        except Exception:
            return False, None
