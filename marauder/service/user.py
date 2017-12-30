# -*- coding: utf-8 -*-

from marauder.service.request import rqs, api_url, handle_response


def signin(subdomain, username, password):
    url = api_url(subdomain, 'signin')
    response = rqs.post(
        url, json={'identity': username,
                   'password': password,
                   'remember_me': True})
    return handle_response(response)


def get_members(subdomain):
    url = api_url(subdomain, 'member')
    response = rqs.post(url, params={'all': 'true'})
    return handle_response(response)
