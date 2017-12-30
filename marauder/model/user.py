# -*- coding: utf-8 -*-

from marauder.model.base import Model


class User(Model):

    fields = ('id', 'name', 'full_name')
