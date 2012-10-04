#! /usr/bin/env python

"""2007-06-28 : lzirkel@cendev.com

I've modified this and cleaned a number of things up.  This thing now saves
the files using the same name they are posted with, as well as saving them 
to a directory named with the date the script was run.

So the process that follows is:
- make a directory with today's date
- get the RSS feed
- loop over the IMG tags in the html feed (this could be done better, but 
  works for now).
- download the images in the RSS feed, saving them to the afore mentioned 
  directory.
"""

__revision__ = 0.1

import os
import re
from datetime import date
from urllib import urlopen

import feedparser


VERBOSE = False


RE = re.compile(r'.*?<img src="(?P<url>.*?)"(?P<rest>.*)')
URL = 'http://feeds.feedburner.com/Postsecret'

feeds = feedparser.parse(URL)
c = feeds.entries[0].content[0].value

today = date.today()
os.mkdir(str(today))

m = RE.match(c)
while m:
    m = RE.match(c)

    if m:
        url = m.group('url')
        c = m.group('rest')
        imgfp = urlopen(url)
        img = imgfp.read()
        imgfp.close()

        fname = url.split(os.sep)[-1:][0]
        if VERBOSE:
            print "getting %s" % (fname)
        ofp = open("%s%c%s" % (today, os.sep, fname), "wb")
        ofp.write(img)
        ofp.close()
