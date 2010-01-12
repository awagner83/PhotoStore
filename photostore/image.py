#------------------------------------------------------------------------#
# PhotoStore - Photo Collection Storage
# Copyright (C) 2010 Adam Wagner <awagner83@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#------------------------------------------------------------------------#
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

