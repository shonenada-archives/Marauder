# -*- coding: utf-8 -*-

from marauder.model.base import Base


class Team(Base):

    fields = ('id', 'name', 'subdomain')
