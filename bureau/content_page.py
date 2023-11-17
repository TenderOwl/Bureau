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
from gi.repository import Gtk, GObject, Adw

from bureau.components.sidebar.column import SidebarColumn
from bureau.providers.app_state import AppStateProvider


@Gtk.Template(resource_path='/com/tenderowl/bureau/ui/content_page.ui')
class ContentPage(Gtk.Box):
    __gtype_name__ = 'ContentPage'

    outer: Adw.OverlaySplitView = Gtk.Template.Child()
    sidebar_column: SidebarColumn = Gtk.Template.Child()
    toggle_sidebar_btn: Gtk.ToggleButton = Gtk.Template.Child()

    app_state: AppStateProvider

    @inject.autoparams()
    def __init__(self, app_state: AppStateProvider, **kwargs):
        super().__init__(**kwargs)
        self.app_state = app_state

        self.app_state.bind_property('sidebar_collapsed', self.outer, 'collapsed', GObject.BindingFlags.BIDIRECTIONAL)
        self.toggle_sidebar_btn.bind_property('visible', self.app_state, 'sidebar_collapsed',
                                              GObject.BindingFlags.BIDIRECTIONAL)
        self.toggle_sidebar_btn.bind_property('active', self.outer, 'show-sidebar', GObject.BindingFlags.BIDIRECTIONAL)
        # self.sidebar_column.connect('notify::show-sidebar', self._on_sidebar_collapsed)

    # @Gtk.Template.Callback()
    # def _on_sidebar_collapsed(self, state: bool):
    #     print('Collapsed ', state)
    #     self.app_state.sidebar_collapsed = state
    #     self.toggle_sidebar_btn.set_visible(state)
