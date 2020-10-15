import gi

gi.require_version('Astroid', '0.2')
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import GObject, Astroid, Gtk, WebKit2

import base64
import pydenticon


class IdenticonPlugin(GObject.Object, Astroid.ThreadViewActivatable):
    object = GObject.property(type=GObject.Object)
    thread_view = GObject.property(type=Gtk.Box)
    web_view = GObject.property(type=WebKit2.WebView)

    def do_activate(self):
        self.generator = pydenticon.Generator(5, 5)

    def do_deactivate(self):
        pass

    def do_get_avatar_uri(self, email, _type, size, _message):
        img = self.generator.generate(email, size, size, output_format="jpeg")
        img_base64 = base64.urlsafe_b64encode(img).decode("utf-8")
        img_uri = f"data:image/jpeg;base64,{img_base64}"

        return img_uri

    def do_get_allowed_uris(self):
        return []
