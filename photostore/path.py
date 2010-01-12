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
"""Filelist Handling/Building."""

from os import path, walk, mkdir
from itertools import chain, ifilter


IMAGE_EXTENSIONS = ['jpg', 'png', 'gif']


def iterfiles(image_paths, extensions=IMAGE_EXTENSIONS):
    """Walk given paths and yield files matching extensions."""
    # fn for pattern match
    is_match = lambda x: any(x.endswith("." + ext) for ext in extensions)

    for image_path in image_paths:
        if path.isdir(image_path):
            for root, dirs, dir_files in walk(image_path):
                for file in ifilter(is_match, dir_files):
                    yield path.join(root, file)
        elif path.isfile(file_path) and is_match(file_path):
            yield file_path
    
