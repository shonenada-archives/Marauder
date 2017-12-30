# -*- coding: utf-8 -*-

from asciimatics.widgets import Frame, Layout, Text

from marauder.view.utils import get_screen_size


class TipView(Frame):

    def __init__(self, screen, client):
        title = 'Error'
        height, width = get_screen_size(screen)
        super(TipView, self).__init__(
            screen, height, width, hover_focus=True, title=title)
        self.client = client
        self.setup_layout()

    def setup_layout(self):
        error_text = Text('Error:', self.client.get_error())

        self.layout = layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(error_text)
        self.fix()
