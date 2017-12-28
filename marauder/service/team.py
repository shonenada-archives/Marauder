# -*- coding: utf-8 -*-

from marauder.service.request import rqs


def get_team(subdomain):
    url = 'https://%s.bearychat.com/api/team' % subdomain
    resp = rqs.get(url)
    data = resp.json()
    if data['code'] == 0:
        return data['result']
