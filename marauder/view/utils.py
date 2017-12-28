# -*- coding: utf-8 -*-

import sys


def get_screen_size(screen):
    return (screen.height * 2 // 3, screen.width * 2 // 3)


def exit_normally():
    sys.exit(0)
