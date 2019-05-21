#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request, abort, jsonify, send_file, current_app
import json
from app.libs.request_google_texttospeech import google_text2speech
from app.libs.request_texttospeech import RequestsTextToSpeech
from . import web
from werkzeug.contrib.cache import RedisCache
from app.secure import REDISHOST,  REDISPOSSWORD, REDISTIMEOUT
cache = RedisCache(host=REDISHOST, password=REDISPOSSWORD,
                   default_timeout=REDISTIMEOUT)

__author__ = 'caijinxu'


@web.route("/texttospeech", methods=['POST'])
def texttospeech():
    if not request.data:
        abort(500)
    jtext = json.loads(request.data)
    if not jtext.get("text"):
        abort(500)
    lang = jtext.get('lang') if jtext.get('lang') else "en_US"
    gender = jtext.get('gender') if jtext.get('gender') else "MALE"
    gt2s = google_text2speech()
    return jsonify(gt2s.create_voice(jtext['text'], lang=lang, gender=gender))


@web.route("/supported_voices",  methods=['Get'])
def supported_voices():
    res = cache.get("/supported_voices")
    if res:
        return jsonify(res)
    gt2s = google_text2speech()
    res = gt2s.supported_voices()
    cache.set("/supported_voices", res)
    return jsonify(res)


@web.route("/text2speech", methods=['POST'])
def text2speech():
    if not request.data:
        abort(500)
    jtext = json.loads(request.data)
    if not jtext.get("text") and not jtext.get('voice') and not jtext.get('gender'):
        abort(403)
    ca = RequestsTextToSpeech()
    audiobase = ca.create_audio(jtext.get("text"), jtext.get('voice'), jtext.get('gender'))
    if audiobase:
        return jsonify(audiobase)
    else:
        abort(500)
