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
"""Package installer."""

from sys import version_info, stderr

from setuptools import setup


if not (version_info[0] >= 3 and version_info[1] >= 1):
    stderr.write("Python 3.1 or greater is required to install.\n")
    exit(1)

setup(
        name='PhotoStore',
        version='0.1',
        description='Photo Collection Storage.',
        author='Adam Wagner',
        author_email='awagner83@gmail.com',
        packages=['photostore']
)

