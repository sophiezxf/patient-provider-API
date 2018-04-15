# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

from flask import Blueprint, jsonify
from version import VERSION

example_api = Blueprint('example_api', __name__, url_prefix='')


@example_api.route('/', methods=['GET'])
def status():
    resp = {
        'name': 'doctor_service',
        'version': VERSION
    }

    return jsonify(resp), 200
