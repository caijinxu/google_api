#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.exceptions import HTTPException
from app.libs.errors import APIException
from gevent import monkey
from app.libs.error_code import ServerError
monkey.patch_all()
from app import create_app

__author__ = 'caijinxu'

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # TODO log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True, threaded=True)
