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
    
