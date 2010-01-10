"""Image handling functionality."""

from os import path
import hashlib


class Image(object):
    """Photo object representation."""

    id = None
    old_path = None
    new_path = None
    hash = None
    size = None

    def __init__(self, filename):
        """Image constructor."""
        self.old_path = filename
        self.hash = gethash(open(filename))
        self.size = path.getsize(filename)
        self.id = "%s-%d" % (self.hash, self.size)
        self.new_path = "%s/%s%s" % (
                self.id[:2], self.id[2:], getext(filename))
        

def getext(filename):
    """Retrieve file extension.
    
    Example:
    >>> getext('test.png')
    '.png'
    >>> getext('test')
    ''
    """
    root, ext = path.splitext(filename)
    return ext


def gethash(filehandle):
    """Generate hash of file contents."""
    return hashlib.new('ripemd160', filehandle.read()).hexdigest()

