PLUGIN_NAME = 'Album Sorting'
PLUGIN_AUTHOR = 'Donagh Horgan'
PLUGIN_DESCRIPTION = 'Sorts albums chronologically, according to the earliest available date.'
PLUGIN_VERSION = "1.01"
PLUGIN_API_VERSIONS = ["0.12", "0.15"]

from picard.metadata import register_album_metadata_processor
    
def add_albumsort(tagger, metadata, release):
    try:
        original = metadata["originaldate"]
        if len(original) == 4:
            original += "-01-01"
        elif len(original) == 7:
            original += "-01"
    except:
        original = None
    
    try:
        date = metadata["date"]
        if len(date) == 4:
            date += "-01-01"
        elif len(date) == 7:
            date += "-01"
    except:
        date = None
    
    if original and date:
        earliest = sorted([original, date])[0]
    elif original:
        earliest = original
    elif date:
        earliest = date
    else:
        earliest = None
    
    if earliest:
        metadata["date"] = earliest
        metadata["originaldate"] = earliest
        metadata["albumsort"] = earliest + " " + metadata["album"]

register_album_metadata_processor(add_albumsort)
