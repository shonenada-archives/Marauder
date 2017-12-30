# -*- coding: utf-8 -*-

from marauder.model.team import Team
from marauder.model.user import User
from marauder.model.channel import Channel


def id_as_key(x):
    return x['id']


class ListObject(object):

    def __init__(self, cls, key_func):
        if not callable(key_func):
            raise ValueError('key_func is not callable')

        self.cls = cls
        self.key_func = key_func
        self.data = {}

    def add(self, v):
        if isinstance(v, self.cls):
            key = self.key_func(v)
            if key is not None:
                self.data[key] = v

    def flush(self):
        self.data = {}


class Store(object):

    def __init__(self):
        self.team = Team()
        self.current_user = User()
        self.members = ListObject(User, id_as_key)
        self.channels = ListObject(Channel, id_as_key)
