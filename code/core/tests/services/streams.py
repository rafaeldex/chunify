import os, sys
from chalicelib.services.streams import Streams
import unittest

class TestStreams(unittest.TestCase): 
  # Tests listing a table streams
  def list_streams_from_musics_table(self):
    response = Streams().list_streams('chunify-musics')
    self.assertEqual(response, 'FOO')

if __name__ == '__main__':
  unittest.main()
