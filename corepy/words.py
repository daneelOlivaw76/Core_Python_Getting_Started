#!/usr/bin/env python3

"""Retrieve and print words from a URL.
Usage:
    python3 words.py <URL>
"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.
      Args:
          url: The URL of a UTF-8 text document.
      Returns:
          A list of strings containing the words from
          the document
    """

    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Print items in a paragraph
        Args:
            items: An iterable series of printable items;
            converts the input to strings for printing.
    """

    string = '\n'
    for word in items:
        string += str(word) + ' '
    string = string.rstrip() + '.'
    print(string)


def main(url):
    """Print each word from a text document gotten from a URL.
        Args:
            url: The URL of a UTF-8 text document.
    """

    words = fetch_words(url)
    print_items(words)

if __name__ == '__main__':
    # The 0th arg is the module filename.
    main(sys.argv[1])


# mock url: 'http://sixty-north.com/c/t.txt'
