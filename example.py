from fileinput import filename
from src.finder import *

FILENAME = "" # on windows make sure to use \\ for directories.
SEARCH_QUERY = ""


finder = ImageFinder(FILENAME)
finder.createImageList()
finder.scanAllImages()

print(finder.searchWords(SEARCH_QUERY)) # returns all of the search queries and the number of matched words per image
