import warnings

warnings.warn("""
This module is for backwards compatibility only!

Please use the authentication module found in sgtk.authentication for
new code. This compatibility wrapper will be removed at some point in the future.
""", DeprecationWarning, stacklevel=2)

from tank.authentication import *

def get_logger():
    # This is present for backwards compatibility with older tk-core's.
    # Lazy import to avoid poluting the module's namespace.
    import tank.authentication
    from tank.log import LogManager
    return LogManager.get_logger(tank.authentication.__name__)
