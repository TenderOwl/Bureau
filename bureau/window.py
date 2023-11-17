# MIT License
#
# Copyright (c) 2023 Andrey Maksimov
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# SPDX-License-Identifier: MIT
import inject
from gi.repository import Adw, Gio, GObject
from gi.repository import Gtk

from bureau.content_page import ContentPage
from bureau.providers.db import DbProvider


@Gtk.Template(resource_path='/com/tenderowl/bureau/ui/window.ui')
class BureauWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'BureauWindow'

    db_provider: DbProvider | None

    connectivity_banner: Adw.Banner = Gtk.Template.Child()
    content_page: ContentPage = Gtk.Template.Child()

    @inject.autoparams()
    def __init__(self, db_provider: DbProvider, **kwargs):
        super().__init__(**kwargs)

        self.db_provider = db_provider
        self.db_provider.connect('initialized', self._on_db_initialized)

        nm: Gio.NetworkMonitor = Gio.NetworkMonitor.get_default()
        nm.connect('network-changed', lambda x, y: self.connectivity_banner.set_revealed(not y))

    def _on_db_initialized(self, sender: GObject.GObject = None):
        print(sender)
        print('Db Initialized')
