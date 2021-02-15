#!/usr/bin/python
# outputs list of keywords (one per line, sorted alphabetically),
#and then outputs the list but sorted alphabetically in reverse.
import keyword

keywords=keyword.kwlist

#print in alphabetic order
for eachkey in keywords:
    print eachkey
    
#print in reverse order
keywords.reverse()
for eachkey in keywords:
    print eachkey

