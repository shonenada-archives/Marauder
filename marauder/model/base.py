# -*- coding: utf-8 -*-


class Model(object):

    def __init__(self, **kwargs):
        self.populate(kwargs)

    def populate(self, data):
        fields = getattr(self, 'fields', ())
        for f in fields:
            setattr(self, f, data.get(f, None))
