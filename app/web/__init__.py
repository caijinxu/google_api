#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, url_for
__author__ = 'caijinxu'

web = Blueprint('web', __name__, template_folder='templates')

from app.web import translation
from app.web import textspeech