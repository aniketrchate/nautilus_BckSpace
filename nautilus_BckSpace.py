#!/usr/bin/env python3

import os, gi
gi.require_version('Nautilus', '3.0')
from gi.repository import Nautilus, Gtk, GObject

def start():
    nautilus = Gtk.Application.get_default()
    nautilus.set_accels_for_action( "win.back", ["BackSpace"] )

class Bckspace(GObject.GObject, Nautilus.LocationWidgetProvider):
    def __init__(a):
        pass
    
    def get_widget(a, uri, window):
        start()
        return None
