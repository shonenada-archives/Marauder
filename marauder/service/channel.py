# -*- coding: utf-8 -*-

from marauder.service.request import rqs, api_url, handle_response


def get_channels(subdomain):
    url = api_url(subdomain, 'channels')
    return handle_response(rqs.get(url))
