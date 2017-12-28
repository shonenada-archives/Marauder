# -*- coding: utf-8 -*-

import sys
from functools import partial

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError

from marauder.view.name import Names
from marauder.view.home import HomeView
from marauder.view.signin import SignInView
from marauder.view.hello import HelloView


def create_scene(screen, store, cls, name):
    dont_stop = -1
    return Scene(
        [cls(screen, store)],
        duration=dont_stop,
        name=name)


def marauder(screen, scene):
    store = {}
    Scene = partial(create_scene, screen, store)
    scenes = [
        Scene(HomeView, Names.HomeView),
        Scene(SignInView, Names.SignInView),
        Scene(HelloView, Names.HelloView),
    ]
    screen.play(scenes, stop_on_resize=True, start_scene=scene)


def start():
    last_scene = None
    while True:
        try:
            Screen.wrapper(marauder,
                           catch_interrupt=False,
                           arguments=[last_scene])
            sys.exit(0)
        except ResizeScreenError as e:
            last_scene = e.scene
