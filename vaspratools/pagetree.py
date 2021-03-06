# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 14:51:00 2018
@author: Doug Lawrence - Github: Vaspra

A shortcut for getting an xpath-able tree from a URL. Typical usage involves
simply importing this module and using:
    
    > tree = pagetree.get_tree('YOUR_URL')

This will create a tree of the nodes contained in the web page, ready for
xpathing using:
    
    > tree.xpath('//NODES[@class="SOME_CLASS"]')
"""

from requests import get as _get
from requests.exceptions import RequestException as _RequestException
from contextlib import closing as _closing
from lxml import html as _html


def get_page(url:str, user_agent='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content as bytes, otherwise return None.
    """
    
    headers = {
    'User-Agent': user_agent
    }
    
    try:
        with _closing(_get(url, stream=True, headers=headers)) as resp:
            if _is_good_response(resp):
                return resp.content
            else:
                return None

    except _RequestException as e:
        _log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def _is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def _log_error(e):
    """
    Log errors, at the moment a simple print.
    """
    print(e)
    
    
def get_tree(url, isPageBytes=False):
    """
    Requests the url to retrieve an html page, and converts that into
    an xpath-able tree.
    
    Can alternatively instruct the function to take a raw (bytes-like) page
    instead of a url as input.
    """
    
    if not isPageBytes:
        page = get_page(url)
    
    else:
        page = url
    
    if not page:
        print("get_tree returned a no-tree")
        return None
    
    if type(page) != bytes:
        raise Exception('Expected page to be bytes-like, but was %s-like'
                        % str(type(page)))
        
    tree = _html.fromstring(page)
    
    return tree
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    