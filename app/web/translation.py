#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, abort, jsonify, current_app
import json
from app.libs.request_google_translation import google_translation
from . import web
from functools import wraps
from flask import make_response
from werkzeug.contrib.cache import RedisCache
from app.libs.textlist_process import textlist_translation
import html
from app.libs.ip_to_langcode import ip_to_lancode
from app.libs.create_langs import LangsWithTarget, Langs
from app.libs.error_code import NotFound, Forbidden, DeleteSuccess
from app.libs.forms import TranslationData
from app.secure import REDISHOST,  REDISPOSSWORD, REDISTIMEOUT
cache = RedisCache(host=REDISHOST, password=REDISPOSSWORD,
                   default_timeout=REDISTIMEOUT)


def allow_cross_domain(fun):
    """允许跨域访问装饰器"""
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'POST,GET'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun


@web.route("/get_languages", methods=['get'])
@allow_cross_domain
def get_languages():
    res = {}
    ip = request.remote_addr
    target = ip_to_lancode(ip)
    res['target'] = target
    result = cache.get("get_languages")
    if not result:
        result = Langs()
        if result:
            cache.set("get_languages", result, timeout=0)
        else:
            return NotFound()
    res['get_languages'] = result
    return jsonify(res)


@web.route("/translation_list",  methods=['POST'])
@allow_cross_domain
def translation_list():
    """接收一段以‘\’符号分割的字符串，以list传入需要翻译的对象"""
    form = TranslationData(request)
    res = cache.get("translation" + form.text.data + form.target.data)
    if res:
        return jsonify(res)
    textlist = form.text.data.split("|")
    resultlist = textlist_translation(textlist, form.target.data)
    if resultlist == 2:
        res = cache.get("translation" + form.text.data + form.target.data)
    else:
        res = "|".join(resultlist)
        cache.set("translation" + form.text.data + form.target.data, res, timeout=3600)
    return jsonify(html.unescape(res))


@web.route("/delcache",  methods=['get'])
def delcache():
    form = TranslationData(request)
    cache.delete("translation" + form.text.data + form.target.data)
    return DeleteSuccess()



