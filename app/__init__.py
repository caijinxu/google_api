#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask

__author__ = 'caijinxu'


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object('app.settings')
    app.config.from_object('app.secure')

    register_web_blueprint(app)

    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)
    return app

