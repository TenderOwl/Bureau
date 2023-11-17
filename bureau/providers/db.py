from typing import Any

from gi.repository import GObject, Gio
from gi.repository import Gom

from bureau.models.mailbox import MailboxResource


class DbProvider(GObject.GObject):
    __gtype_name__ = 'DbProvider'

    adapter: Gom.Adapter | None
    repository: Gom.Repository | None

    initialized = GObject.Property(type=bool, default=False)

    __gsignals__ = {
        'open-done': (GObject.SIGNAL_RUN_LAST, None, ()),
        'open-failed': (GObject.SIGNAL_RUN_LAST, None, ()),
        'initialized': (GObject.SIGNAL_RUN_LAST, None, ()),
    }

    def __init__(self, uri: str = ':memory:'):
        super().__init__()

        self.adapter = Gom.Adapter()
        self.adapter.open_async(uri, self._on_open)

    def _on_open(self, source_object: GObject.GObject, result: Gio.AsyncResult, data: Any = None):
        try:
            if self.adapter.open_finish(result):
                self.emit('open-done')
                self.init_db()
        except Exception as e:
            print('Failed to open database: ', e)
            self.emit('open-failed')

    def init_db(self):
        # Create the table
        self.repository = Gom.Repository(adapter=self.adapter)
        self.repository.automatic_migrate_sync(1, [MailboxResource])

        self.initialized = True
        self.emit('initialized')
