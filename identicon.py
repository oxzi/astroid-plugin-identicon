# SPDX-FileCopyrightText: 2020 Alvar Penning
#
# SPDX-License-Identifier: GPL-3.0-or-later

import gi

gi.require_version('Astroid', '0.2')
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import GObject, Astroid, Gtk, WebKit2

import base64
import functools
import pydenticon


class IdenticonPlugin(GObject.Object, Astroid.ThreadViewActivatable):
    object = GObject.property(type=GObject.Object)
    thread_view = GObject.property(type=Gtk.Box)
    web_view = GObject.property(type=WebKit2.WebView)

    def do_activate(self):
        foreground = ["rgb(45,79,255)",
                      "rgb(254,180,44)",
                      "rgb(226,121,234)",
                      "rgb(30,179,253)",
                      "rgb(232,77,65)",
                      "rgb(49,203,115)",
                      "rgb(141,69,170)"]
        background = "rgba(255,255,255,0)"

        self.generator = pydenticon.Generator(
                rows=5, columns=5,
                foreground=foreground, background=background)

    def do_deactivate(self):
        pass

    @functools.lru_cache(maxsize=512)
    def _create_identicon(self, email, size):
        img = self.generator.generate(
                email, size, size, output_format="png", padding=(2, 2, 2, 2))

        img_base64 = base64.urlsafe_b64encode(img).decode("utf-8")
        img_uri = f"data:image/png;base64,{img_base64}"

        return img_uri

    def do_get_avatar_uri(self, email, _type, size, _message):
        return self._create_identicon(email, size)

    def do_get_allowed_uris(self):
        return []
