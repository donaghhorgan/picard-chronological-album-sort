# albumsort.py

A chronological album sorting plugin for MusicBrainz Picard.

## Installation

To install the script, run Picard and select *Options* → *Options...* → *Plugins* → *Install plugin...* and select `albumsort.py`. Check the box next to the plugin to enable it.

## Usage

The plugin modifies track metadata in three ways:

- The `date` field is set to the earliest available date (i.e. `date` or `originaldate`, whichever is chronologically first).
- The `originaldate` field is also set to the earliest available date.
- The `albumsort` field is set to the album title prefixed with the earliest available date.

If an earliest date is not available, the metadata for the track is not modified.
