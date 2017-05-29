#import the urlopen function. We need this to read in HTML
from urllib2 import urlopen

#set a url that we'll try and grab some HTML from
url = "https://en.wikipedia.org/wiki/Web_scraping"

#open the url and read the html content into a string variable
html_page = urlopen(url)
html_text = html_page.read()

#set the range that we want filter on
#in this instance everything between the <title></title> tags'
start_tag = "<title>"
end_tag = "</title>"

"""
Search for the tags.

The html_text.find() function will give us the index of the the very
first '<' character that matches the string that we pass through.
We want to search for everything from the end of the tag -
i.e. ">This text"
To achieve this we'll add the length of 'start_tag' to the index of '<'
character.

This won't be necessary for the end tag. We just need the index for the '<'
character
"""
start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

#print html_test string
print html_text[start_index:end_index]