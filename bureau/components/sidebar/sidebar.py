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
from gi.repository import Gtk

from bureau.providers.account_provider import AccountProvider


@Gtk.Template(resource_path='/com/tenderowl/bureau/ui/sidebar/sidebar.ui')
class SideBar(Gtk.Box):
    __gtype_name__ = 'SideBar'

    account_provider: AccountProvider

    accounts_list: Gtk.ListBox = Gtk.Template.Child()

    @inject.autoparams()
    def __init__(self, account_provider: AccountProvider, **kwargs):
        super().__init__(**kwargs)

        accounts = account_provider.get_accounts()
        for account in accounts:
            account_row = Gtk.Label(label=account,
                                    margin_start=8, margin_end=8, margin_top=4, margin_bottom=4,
                                    halign=Gtk.Align.START,
                                    )
            account_row.add_css_class('heading')
            self.accounts_list.append(account_row)
