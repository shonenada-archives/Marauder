# -*- coding: utf-8 -*-

from marauder.error import MarauderError
from marauder.service.request import rqs


def signin(subdomain, username, password):
    url = 'https://%s.bearychat.com/api/signin' % subdomain
    resp = rqs.post(
        url, json={'identity': username,
                   'password': password,
                   'remember_me': True})

    data = resp.json()

    if resp.status_code != 200:
        raise MarauderError(data.get('error') or 'Failed to request %s' % url)

    if data['code'] == 0:
        return data['result']

    raise MarauderError(data['error'])
