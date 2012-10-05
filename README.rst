========
Overview
========

The postsecret project consists of scripts intended to download and archive 
the images found on the http://www.postsecret.com/ blog.  This blog posts
images weekly and makes only the current week's images available with no 
archive ability baked in.  Thus these scripts, run on a weekly basis, will 
gather those images and place them all in a directory as an archive.

-------
Scripts
-------

There are multiple scripts present in this project.  The intent of each of 
these is outlined below.

get-post-secret.py
------------------
The original script, provided here for historical reasons, simply grabbed
the page and then processed each img element.  Little to no error checking
was done in the process of this script running, yet it ran without major 
issue for around 5 years.

image-gatherer
--------------
This script is basically a rewrite of the original get-post-secret.py with
error checking and such baked in.  The intent is that this is more of a
generic app that can work on other sites.  There is work to be done to make
this as generic as it should be, but initially it replicates the behavior 
of the original script.

