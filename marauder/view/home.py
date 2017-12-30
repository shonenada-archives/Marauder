# -*- coding: utf-8 -*-

from asciimatics.exceptions import NextScene
from asciimatics.widgets import Frame, Layout, Text, Button

from marauder.error import MarauderError
from marauder.view.utils import get_screen_size, exit_normally
from marauder.view.name import Names


class HomeView(Frame):

    def __init__(self, screen, client):
        title = 'Login BearyChat'
        height, width = get_screen_size(screen)
        super(HomeView, self).__init__(
            screen, height, width, hover_focus=True, title=title)
        self.setup_layout()

        self.client = client

    def setup_layout(self):
        team_text = Text('Team Subdomain:', 'team_subdomain')
        confirm_btn = Button('Confirm', self.do_signin_team)
        exit_btn = Button('Exit', exit_normally)

        self.layout = layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(team_text)
        layout.add_widget(confirm_btn)
        layout.add_widget(exit_btn)
        self.fix()

    def do_signin_team(self):
        self.save()
        subdomain = self.data['team_subdomain']
        team_data = get_team(subdomain)
        if team_data is None:
            raise MarauderError('Team %s not Found' % subdomain)

        raise NextScene(Names.SignInView)
