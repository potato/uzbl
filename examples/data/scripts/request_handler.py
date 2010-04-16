#!/usr/bin/python
import sys, os, re

if(len(sys.argv) == 9):
    uri = sys.argv[8]
    if re.search(".js", uri):
        print "BLOCK"
