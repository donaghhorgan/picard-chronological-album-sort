PLUGIN_NAME = 'Album Sorting'
PLUGIN_AUTHOR = 'Donagh Horgan'
PLUGIN_DESCRIPTION = 'Sorts albums chronologically.'
PLUGIN_VERSION = "1.0"
PLUGIN_API_VERSIONS = ["0.12", "0.15"]

from picard.metadata import register_album_metadata_processor
import re
    
def add_albumsort(tagger, metadata, release):
    metadata["albumsort"] = metadata["originaldate"] + " " + metadata["album"]

register_album_metadata_processor(add_albumsort)
