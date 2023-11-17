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
from gi.repository import Adw
from gi.repository import Goa
from gi.repository import Gtk

from bureau.content_page import ContentPage
from bureau.providers.imap import ImapProvider


@Gtk.Template(resource_path='/com/tenderowl/bureau/ui/window.ui')
class BureauWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'BureauWindow'

    content_page: ContentPage = Gtk.Template.Child()

    @inject.autoparams()
    def __init__(self, imap_provider: ImapProvider, **kwargs):
        super().__init__(**kwargs)

        email_addresses = []

        goa: Goa.Client = Goa.Client.new_sync(None)
        accs = goa.get_accounts()
        for acc in accs:
            mail_proxy = acc.props.mail
            if mail_proxy:
                email_address = mail_proxy.props.email_address
                if email_address:
                    email_addresses.append(email_address)

        print(email_addresses)

        print(imap_provider)
