from fastlog import log
from gi.repository import GObject
from imapclient import IMAPClient


class ImapProvider(GObject.GObject):
    __gtype_name__ = "ImapProvider"

    server: IMAPClient

    # Props

    # Signals
    __gsignals__ = {
    }

    def __init__(self, server_host: str):
        super().__init__()

        self.server = IMAPClient(server_host, use_uid=True)

    def login(self, username: str, password: str):
        self.server.login(username, password)

    def list_folders(self, directory: str = '', pattern: str = '*'):
        if not self.server:
            return

        folders = self.server.list_folders(directory, pattern)
        log.debug('FOLDERS:')
        with log.indent():
            [log.debug(folder) for folder in folders]
