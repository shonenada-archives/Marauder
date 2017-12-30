# -*- coding: utf-8 -*-

from asciimatics.widgets import Frame, Layout, Label

from marauder.view.utils import get_screen_size


class HelloView(Frame):

    def __init__(self, screen, client):
        title = 'Hello'
        height, width = get_screen_size(screen)
        super(HelloView, self).__init__(
            screen, height, width, hover_focus=True, title=title)
        self.setup_layout()

        self.client = client

    def setup_layout(self):
        label = Label('Hello')
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(label)
        self.fix()

    def reset(self):
        super(HelloView, self).reset()
        self.title = 'Hello %s' % self.client.store.current_user.name
        self.fix()
