import sys
import os


_DEFAULT = object()
PY3 = sys.version_info[0] == 3
POSIX = os.name == "posix"

ENCODING = sys.getfilesystemencoding()
if not PY3:
    ENCODING_ERRS = "replace"
else:
    try:
        ENCODING_ERRS = sys.getfilesystemencodeerrors()  # py 3.6
    except AttributeError:
        ENCODING_ERRS = "surrogateescape" if POSIX else "replace"


def _open_binary(fname, **kwargs):
    return open(fname, "rb", **kwargs)


def _open_text(fname, **kwargs):
    """On Python 3 opens a file in text mode by using fs encoding and
    a proper en/decoding errors handler.
    On Python 2 this is just an alias for open(name, 'rt').
    """
    if PY3:
        kwargs.setdefault('encoding', ENCODING)
        kwargs.setdefault('errors', ENCODING_ERRS)
    return open(fname, "rt", **kwargs)


def cat(fname, fallback=_DEFAULT, binary=True):
    """Return file content.
    fallback: the value returned in case the file does not exist or
              cannot be read
    binary: whether to open the file in binary or text mode.
    """
    try:
        with _open_binary(fname) if binary else _open_text(fname) as f_d:
            return f_d.read().strip()
    except (IOError, OSError):
        if fallback is not _DEFAULT:
            return fallback
        raise