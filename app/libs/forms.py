# -*- coding: utf-8 -*-
from wtforms import Form, StringField
from wtforms.validators import DataRequired
from app.libs.error_code import ParameterException
__author__ = 'caijinxu'


class BaseForm(Form):
    def __init__(self, request):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        formdata = request.form
        super(BaseForm, self).__init__(formdata=formdata, data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self


class TranslationData(BaseForm):
    text = StringField('需要翻译的文本', validators=[DataRequired()])
    target = StringField('目标语言代码', default='en')
