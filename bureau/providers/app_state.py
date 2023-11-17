from gi.repository import GObject


class AppStateProvider(GObject.GObject):
    __gtype_name__ = "AppStateProvider"

    # Props
    sidebar_collapsed = GObject.Property(type=bool, default=True)
    mail_column_collapsed = GObject.Property(type=bool, default=True)

    # Signals
    __gsignals__ = {
        'sidebar-changed': (GObject.SIGNAL_RUN_FIRST, None, (bool,))
    }

    def __init__(self):
        super().__init__()
