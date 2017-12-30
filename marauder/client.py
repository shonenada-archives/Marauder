# -*- coding: utf-8 -*-

from marauder.store import Store
from marauder.error import MarauderError
from marauder.service.team import get_team
from marauder.service.user import signin, get_members
from marauder.service.channel import get_channels


class Client(object):

    def __init__(self, store=None):
        self.store = store or Store()

    def get_team(self, subdomain):
        data = get_team(subdomain)
        if data is None:
            raise MarauderError('Failed to get team data')

        self.store.team.populate(data)
        return self.store.team

    def signin(self, username, password):
        data = signin(self.store.team.subdomain)
        if data is None:
            raise MarauderError('Failed to signin account')

        self.store.current_user.populate(data)
        return self.store.current_user

    def get_members(self, flush=True):
        data = get_members(self.store.team.subdomain)
        if data is None:
            raise MarauderError('Failed to get members')

        if flush is True:
            self.store.members.flush()

        for m in data:
            self.store.members.add(m)

        return self.store.members

    def get_channels(self, flush=True):
        data = get_channels(self.store.team.subdomain)
        if data is None:
            raise MarauderError('Failed to get channels')

        if flush is True:
            self.store.channels.flush()

        for m in data:
            self.store.channels.add(m)

        return self.store.channels
