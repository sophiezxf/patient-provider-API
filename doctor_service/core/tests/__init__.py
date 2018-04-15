# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

from flask.ext.testing import TestCase

from doctor_service.app import create_app
from doctor_service.settings import Test


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app(config=Test)
        return app

    def setUp(self):
        pass
