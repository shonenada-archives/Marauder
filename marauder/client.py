# -*- coding: utf-8 -*-

from asciimatics.exceptions import NextScene

from marauder.store import Store
from marauder.error import MarauderError
from marauder.service.team import get_team
from marauder.service.user import signin, get_members
from marauder.service.channel import get_channels
from marauder.view.name import Names


class Client(object):

    def __init__(self, store=None):
        self.store = store or Store()
        self._error = None

    def get_error(self):
        return self._error

    def get_team(self, subdomain):
        is_ok, data = get_team(subdomain)
        if data is None:
            raise MarauderError('Failed to get team data')

        if is_ok is False:
            self._error = data
            raise NextScene(Names.TipView)

        self.store.team.populate(data)
        return self.store.team

    def _ensure_subdomain(self):
        if self.store.team.subdomain is None:
            raise MarauderError('Sign in Team first')

    def signin(self, username, password):
        self._ensure_subdomain()

        is_ok, data = signin(self.store.team.subdomain, username, password)
        if data is None:
            raise MarauderError('Failed to signin account')

        if is_ok is False:
            self._error = data
            raise NextScene(Names.TipView)

        self.store.current_user.populate(data['user'])
        return self.store.current_user

    def get_members(self, flush=True):
        self._ensure_subdomain()

        is_ok, data = get_members(self.store.team.subdomain)
        if data is None:
            raise MarauderError('Failed to get members')

        if is_ok is False:
            self._error = data
            raise NextScene(Names.TipView)

        if flush is True:
            self.store.members.flush()

        for m in data:
            self.store.members.add(m)

        return self.store.members

    def get_channels(self, flush=True):
        self._ensure_subdomain()

        is_ok, data = get_channels(self.store.team.subdomain)
        if data is None:
            raise MarauderError('Failed to get channels')

        if is_ok is False:
            self._error = data
            raise NextScene(Names.TipView)

        if flush is True:
            self.store.channels.flush()

        for m in data:
            self.store.channels.add(m)

        return self.store.channels
