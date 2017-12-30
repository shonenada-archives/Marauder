# -*- coding: utf-8 -*-

from asciimatics.exceptions import NextScene
from asciimatics.widgets import Frame, Layout, Text, Button

from marauder.view.utils import get_screen_size, exit_normally
from marauder.view.name import Names


class SignInView(Frame):

    def __init__(self, screen, client):
        title = 'Sign in'
        height, width = get_screen_size(screen)
        super(SignInView, self).__init__(
            screen, height, width, hover_focus=True, title=title)
        self.setup_layout()

        self.client = client

    def setup_layout(self):
        username_text = Text('Username:', 'username')
        password_text = Text('Password:', 'password', hide_char='*')
        signin_btn = Button('Sign in', self.do_signin_account)
        exit_btn = Button('Exit', exit_normally)

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        layout.add_widget(username_text)
        layout.add_widget(password_text)
        layout.add_widget(signin_btn)
        layout.add_widget(exit_btn)
        self.fix()

    def do_signin_account(self):
        self.save()
        username = self.data['username']
        password = self.data['password']
        self.client.signin(username, password)
        raise NextScene(Names.HelloView)

    def reset(self):
        super(SignInView, self).reset()
        title = 'Sign in %s' % self.client.store.team.name
        self.title = title
        self.fix()
