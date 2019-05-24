#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This progran can be used to get movie rating.
"""

DOCUMENTATION = '''
---
short_description: Get movie rating
description:
  This program can be used to get a movie rating.
  Underneath, it uses the OMDB API to get rating
  information about movies from the OMDB database.
author:
  - "ppetit(@opennext.io)"
'''

import sys
import getopt
from omdb import OMDBClient

omdb_key = '2c26532a'

def usage():
  print ('movie-rating -t <movie title> [-h]')

def get_movie(title):
  
  client = OMDBClient(apikey=omdb_key)
  response = client.get(title=title, timeout=5, tomatoes='true') 
  return response
    
def get_rating(movie, source):
  ratings = movie.get('ratings')
  for rating in ratings:
    if rating.get('source') == source:
      return(rating.get('value'))
  return('N/A')

def main(argv):

  title = ''
  try:
    opts, args = getopt.getopt(argv,"ht:", ["title=", "help"])
  except getopt.GetoptError:
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ('-h', "--help"):
      usage()
      sys.exit()
    elif opt in ("-t", "--title"):
      title = arg.strip()
    else:
      usage()

  if len(title) == 0:
    print("You must provide a movie title!")
    sys.exit(2)

  movie = get_movie(title)
  if movie.get("response") == 'True':
    print("{}:\n\tReleased: {}\n\tRated: {}".format(movie.get('title'), movie.get('released'), movie.get('rated')))
    print("\tRotten Tomatoes rating: %s" % (get_rating(movie, 'Rotten Tomatoes')))
  else:
    print("Sorry, your title '{}' is not known".format(title))

if __name__ == '__main__':
    main(sys.argv[1:])
