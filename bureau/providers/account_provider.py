from typing import List

from gi.repository import GObject, Goa


class AccountProvider(GObject.GObject):
    __gtype_name__ = "AccountProvider"

    # Props
    goa: Goa.Client

    # Signals
    __gsignals__ = {
    }

    def __init__(self):
        super().__init__()

        self.goa = Goa.Client.new_sync()

    def get_accounts(self) -> List[str]:
        email_addresses = []

        for acc in self.goa.get_accounts():
            if mail_proxy := acc.props.mail:
                email_addresses.append(mail_proxy.props.email_address)

        return email_addresses
