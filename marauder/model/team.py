# -*- coding: utf-8 -*-

from marauder.model.base import Model


class Team(Model):

    fields = ('id', 'name', 'subdomain')
