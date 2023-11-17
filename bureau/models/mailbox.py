# Need a metaclass until we get something like _gclass_init_
#     https://bugzilla.gnome.org/show_bug.cgi?id=701843
import enum

from gi.repository import Gom, GObject
from gi.types import GObjectMeta


class MailboxType(enum.Enum):
    IMAP = 1
    POP3 = 2


class MailboxResourceMeta(GObjectMeta):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls.set_table("mailboxes")
        cls.set_primary_key("id")
        cls.set_notnull("address")
        cls.set_notnull("host")
        cls.set_notnull("username")
        cls.set_notnull("password")


class MailboxResource(Gom.Resource, metaclass=MailboxResourceMeta):
    id = GObject.Property(type=int)
    name = GObject.Property(type=str)
    address = GObject.Property(type=str)
    mailbox_type = GObject.Property(type=int)
    host = GObject.Property(type=str)
    port = GObject.Property(type=int)
    username = GObject.Property(type=str)
    password = GObject.Property(type=str)
