#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.cloud import translate
import json

__author__ = 'caijinxu'


class google_translation:

    def __init__(self):
        self.translate_client = translate.Client()

    def translation(self, text, target="en"):
        return self.translate_client.translate(text, target_language=target)

    def get_languages(self, target='zh'):

        result = self.translate_client.get_languages(target_language=target)
        return result

    def detect_language(self, text):
        return self.translate_client.detect_language(text)
