"""Database and File Storage."""

from os import path, mkdir
import shutil
import json
import warnings


class Storage(object):
    """Image storage and db."""

    db = None
    basepath = None
    dbname = None

    def __init__(self, basepath):
        """Initialize storage object."""
        self.basepath = basepath
        self.dbname = path.join(basepath, 'db.json')

    def __enter__(self):
        """Open db connection."""
        try:
            self.db = json.load(open(self.dbname))
        except IOError:
            self.db = {}
        except ValueError:
            warnings.warn(
                    "Database '%s' was corrupt or incomplete, rebuilding" % 
                    self.dbname)
            self.db = {}

        if 'images' not in self.db:
            self.db['images'] = {}
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Close connection to db."""
        json.dump(self.db, open(self.dbname, "w"))
        self.db = None
        self.images = {}

    def insert(self, image):
        """Insert new image."""
        if image.id in self.db['images']:
            print "skipped (duplicate)."
            return
        print "done."
        fullpath = path.join(self.basepath, image.new_path)

        # Create dest dir
        imagedir = path.join(self.basepath, path.split(image.new_path)[0])
        if not path.isdir(imagedir):
            mkdir(imagedir)

        # Copy to dest
        shutil.copy(image.old_path, path.join(self.basepath, image.new_path))

        # Store in db
        self.db['images'][image.id] = image.old_path

