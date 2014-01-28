#!/usr/bin/env python
import pickle
import os

class Cacheable:
    def __init__(self, name):
        self.name = name
        self.data = None

    def __cache_data(self, fxn, *args):
        if not os.path.isfile(self.name + '.pkl'):
            self.data = fxn(*args)
            pickle.dump(self.data, open(self.name + '.pkl', 'wb'))
        else:
            self.data = pickle.load(open(self.name + '.pkl', 'rb'))

    def load(self, fxn, *args):
        self.__cache_data(fxn, *args)
        return self.data
