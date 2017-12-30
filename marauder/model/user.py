# -*- coding: utf-8 -*-

from marauder.model.base import Base


class User(Base):

    fields = ('id', 'name', 'full_name')
