#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis
import threading
from hashlib import md5
from .request_google_translation import google_translation
from werkzeug.contrib.cache import RedisCache
import time
from app.secure import REDISPOSSWORD, REDISHOST, REDISTIMEOUT
import json

__author__ = 'caijinxu'

cache = RedisCache(host=REDISHOST, password=REDISPOSSWORD, default_timeout=REDISTIMEOUT)


def translation_text(tempname, index, targetlang):
    r = redis.Redis(host=REDISHOST, password=REDISPOSSWORD, port=6379, db=3)
    text = r.lindex(tempname, index)
    text = text.decode('utf8')
    result = cache.get("translation" + text + targetlang)
    if result:
        print("cache is work")
        try:
            r.lset(tempname, index, result)
            exit()
        except Exception as e:
            print(e)
    tran = google_translation()
    result = tran.translation(text, targetlang)
    cache.set("translation" + text + targetlang, result.get('translatedText'))
    r.lset(tempname, index, result.get('translatedText'))


def textlist_translation(textlist, targetlang):
    r = redis.Redis(host=REDISHOST, password=REDISPOSSWORD, port=6379, db=3)
    md = md5()
    te = str(textlist) + targetlang
    md.update(te.encode('utf8'))
    tempname = md.hexdigest()
    if r.exists(tempname):
        time.sleep(6)
        if r.exists(tempname):
            time.sleep(15)
            try:
                r.delete(tempname)
            except Exception as e:
                print(e)
        return 2
    for text in textlist:
        r.rpush(tempname, text)
    thread_list = []
    for i in range(len(textlist)):
        t = threading.Thread(target=translation_text, args=(tempname, i, targetlang))
        thread_list.append(t)
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    result = []
    for _ in range(len(textlist)):
        res = r.lpop(tempname)
        result.append(res.decode('utf8'))
    return result

