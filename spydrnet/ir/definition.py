''' Example base function '''
from dataclasses import dataclass


@dataclass
class Definition(object):
    ''' Definition class '''

    def __init__(self, name=None):
        ''' Creates an empty object of type definition '''
        self._library = "dummy library"
        self._name = name

    def create_port(self, name):
        ''' create_port '''
        print("Creating port %s" % name)
