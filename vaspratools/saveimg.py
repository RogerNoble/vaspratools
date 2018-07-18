# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:50:37 2018
@author: Doug

Saves an image from a url to disk. Capable of compressing the image, respecting
the original aspect ratio.
"""

import os as _os
import urllib.request as _req
import PIL.Image as _Image
from PIL.Image import BILINEAR as _BI


def save(url:str, filename:str='', path:str=_os.getcwd(), fit_to:tuple=None):
    """
    Saves the img from the URL to either the current working directory, or
    a provided 'path' argument.
    
    Supply a tuple of the form (int, int) as an argument to fit_to= to force
    the image to be resized (in pixels). This respects aspect ratio.
    """
    
    if not path.endswith('/') or not path.endswith('\\'):
        path = str(path + '/')
        
    if not _os.path.exists(path):
        _os.makedirs(path)
        
    if not filename:
        filename = str(hash(url)) + '.png'
        
    if '.' not in filename:
        filename += '.png'
        
    filepath = _os.path.join(path, filename)
        
    _req.urlretrieve(url, filepath)
    
    # Compress image if required
    if fit_to:
        
        assert len(fit_to) == 2,\
        'Argument: \'compress_to\' needs 2 integers'
        
        w = fit_to[0]
        h = fit_to[1]
        
        assert type(w) == int, 'compress_to[0] is not an int'
        assert type(h) == int, 'compress_to[1] is not an int'
        
        # Calculate the original aspect ratio
        img = _Image.open(filepath)
        img_w, img_h = img.size
        ar = img_w / img_h
        
        # If the width is dominantly large
        if w > (h * ar):
            new_w = h * ar
            new_h = h
        # If the height is dominantly large
        else:
            new_w = w
            new_h = w / ar
            
        new_size = (int(new_w), int(new_h))
            
        # Create the new image
        img = img.resize(new_size, resample=_BI)
        
        # Save the image as the same name
        img.save(filepath, 'PNG')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        