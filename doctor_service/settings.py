# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function


class Core(object):
    DEBUG = True

class Development(Core):
    pass

class Test(Core):
    pass

class Production(Core):
    pass
