# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function


from doctor_service.core.tests import BaseTestCase
from version import VERSION


class UserApiTestCase(BaseTestCase):
    def setUp(self):
        super(UserApiTestCase, self).setUp()

    def test_status(self):
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.json.get('version'), VERSION)
