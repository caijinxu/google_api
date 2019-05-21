#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'caijinxu'
from werkzeug.contrib.cache import RedisCache
from app.libs.request_google_translation import google_translation
from app.secure import REDISHOST, REDISPOSSWORD, REDISTIMEOUT

cache = RedisCache(host=REDISHOST, password=REDISPOSSWORD,
                   default_timeout=REDISTIMEOUT)


def LangsWithTarget(target):
    """
    :param target: 'en' ISO 639-1 language code
    :return:
    """
    result = cache.get("get_languages" + target)
    if result:
        print("cache is work")
        return result
    tran = google_translation()
    result = tran.get_languages(target)
    for res in result:
        if "language" in res:
            cache.set("get_languages" + target, result, timeout=0)
            return result
        else:
            return False


def Langs():
    result = []
    zhlangs = LangsWithTarget('zh')
    if zhlangs:
        print("Creating Redis kye 'get_languages'")
        for langname in zhlangs:
            echolangs = LangsWithTarget(langname['language'])
            if echolangs:
                for l in echolangs:
                    if l['language'] == langname['language']:
                        result.append(l)
                        break
            else:
                return False
    else:
        return False
    return result
