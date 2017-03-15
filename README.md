# filterRSS
Filter RSS feeds for use in feedreaders

This script is intended to be used with the [Liferea](https://lzone.de/liferea/) feed reader,
but might work with other feed readers as well. It reads the content of an rss feed file from stdin, removes some
items and prints the remaining feed to stdout.


## Usage
This is a Python script that was developed with Python 3.5, but should still work with Python 2.7.

It reads from standard input and writes to standard output. If you want to work on files, you can do this on Linux with
`./filterRSS.py [options] < inputfile > outputfile`.
The first option must be the name of a python file (without the `.py` extension) that implements the actual filter function. All
further Options are passed to the filter function.

### Filter the Tagesschau.de - news feed
As an example a filter for the [Tagesschau-Feed](http://www.tagesschau.de/xml/rss2) is implemented in `filterTagesschau.py`.
To use it, call the script with
`./filterRSS.py filterTagesschau [categories]`
with categories being a list of space separated keywords from
* Inland
* Ausland
* Kultur
* Regional
* Videoblog
* Wirtschaft
* anderes (does not match any of the above criteria)
* alles (show all news)

sport is always removed from the feed (even when choosing *anderes* or *alles*)


## Configuration
The script consists of the `filterRSS.py` file as a frame and a python file, that implements the 
`filter_item`-function.

`filter_item(item_string, criteria)` gets the content of the `item` tag of every feed item (without the tags itself) 
as a string as the first argument
and a list of all options that were passed to `filterRSS.py` (except the first one as this is the name of the file
implementing the filter) as the second argument.

It is expected to return `True` if the item shall stay in the rss feed or `False` if it shall be removed.

As you might wish to have different filter functions for different rss feeds, you have to select the file implementing the
desired filter function as the first option to `filterRSS.py`.

## Usage with Liferea
For the feed that you want to modify select *Properties* -> *Source* -> *Use conversion filter*
and enter the command as described above, for example
`path/to/filterRSS.py filterTagesschau Wirtschaft Kultur` will remove everything from the
[Tagesschau-Feed](http://www.tagesschau.de/xml/rss2)
except the "Wirtschaft" (economy) and "Kultur" (culture) section.


## Remarks and limitations
For the sake of simplicity this script does not do a complete parsing or syntax checking of the rss file and does not
treat the rss file as a tree datastructure. Instead it does some search-and-replace operations on the plain string.
It is likely that there are rss files out there that brake the script. Feel free to open an issue if you find a problem.

The filtering of Atom-Feeds is in principle quite similar and should be possible with a few changes in the script, but will
not work out of the box.
