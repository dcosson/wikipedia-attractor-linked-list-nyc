#!/usr/bin/env python
import sys
import logging
import requests
from BeautifulSoup import BeautifulSoup

logging.basicConfig(level=logging.ERROR)

# indices of the characters of "LinkedList" in the first sentence of the
# "Greek Language" wikipedia article
indices_greek = [444, 26, 27, 4, 2, 108, 444, 26, 81, 116]
BASE_URL = 'http://en.wikipedia.org'

def main(word):
    """ Query wikipedia until you hit the philosophy page
        Phrase must be a non-empty string
    """
    if not word:
        word = raw_input('First word that comes to mind: ')
    url_path = _format_phrase_for_wikipedia(word)
    phrase = _query_wikipedia_loop(url_path)
    print "\n\n{0} NYC\n".format(phrase)

def _query_wikipedia_loop(url_path):
    """ Helper to run the queries"""
    print "checking page: {0}".format(url_path)
    full_url = BASE_URL + url_path
    resp = requests.get(full_url)
    if not resp.ok:
        logging.error("sorry, broke on link: {0}".format(url_path))
        return None
    link, output = _get_link_or_output(resp.content)
    if output:
        return output 
    else:
        return _query_wikipedia_loop(link)

def _get_link_or_output(content):
    """ Find the first link in the body of text of a wikipedia page
    """
    soup = BeautifulSoup(content)
    page_body = soup.body.find(id="mw-content-text")
    first_link, content = get_first_link_and_page_content(page_body)
    # if we made it to one of the "attractor" pages, parse the entry for the
    # "linked list" string
    title = soup.body.h1.span.text 
    if title == "Greek language":
        output = _get_linked_list_from_string(content.text, indices_greek)
        return None, output 
    return first_link, None

def get_first_link_and_page_content(page_body):
    """ Returns the first link in the body of text.  You should pass in the
    #mw-content-text div from the wikipedia page
    """
    # search the paragraphs in order for the first link
    for content in page_body.findAll('p'):
        # sometimes the first link is bad, we only want ones that are
        # wikipedia pages i.e. start with "/wiki/"
        first_link = _search_links_for_first_nice_link(content.findAll('a'))
        if first_link:
            return first_link, content
    # sometimes it's a "list" page, with no links in the paragraphs
    for list_item in page_body.findAll('li'):
        first_link = _search_links_for_first_nice_link(list_item.findAll('a'))
        if first_link:
            break
    return first_link, content

def _search_links_for_first_nice_link(links):
    """ look through the list of links for the first one that is in the normal
    wikipedia format
    """
    # shuffle them for fun, and it's no longer an attractor
    #import random
    #random.shuffle(links)
    for link in links:
        href = link.get('href') or ''
        if href.startswith('/wiki/'):
            logging.debug('href starts with /wiki/')
            first_link = link.get('href')
            return first_link
    return None


def _get_linked_list_from_string(string, indices):
    """ Get the phrase "linked list" from the string
    """
    logging.debug("pulling linked list from: " + string)
    return "".join(string[i] for i in indices)


def _format_phrase_for_wikipedia(phrase):
    """ Capitalize every word and replace spaces with underscores, the way that
    wikipedia urls are formatted
    """
    formatted = '_'.join(a[0].upper() + a[1:] for a in phrase.split(' ')
            if len(a) > 0)
    return "/wiki/{0}".format(formatted)

if __name__ == "__main__":
    word = sys.argv[1] if len(sys.argv) > 1 else None
    main(word)
