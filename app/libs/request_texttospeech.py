#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import subprocess
__author__ = 'caijinxu'


class RequestsTextToSpeech:
    def __init__(self):
        self.__gettoken()

    def __gettoken(self):
        token = subprocess.check_output('gcloud auth application-default print-access-token', shell=True)
        self.token = token.decode('utf-8').rstrip('\n')

    def create_audio(self, text, voice, gender):
        """
        参考https://cloud.google.com/text-to-speech/docs/create-audio
        Authorization 验证内容 'Bearer ' + gcloud命令‘gcloud auth application-default print-access-token’值
        :return 返回音频bytes的base64编码
        """
        url = "https://texttospeech.googleapis.com/v1/text:synthesize"
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = {
            'input': {
                'text': text
            },
            'voice': {
                'languageCode': voice[:5].lower(),
                'name': voice,
                'ssmlGender': gender
            },
            'audioConfig': {
                'audioEncoding': 'LINEAR16'
            }
        }
        try:

            r = requests.post(url, headers=headers, data=json.dumps(data))
            if r.status_code == 200:
                res = json.loads(r.text)
                if 'audioContent' in res:
                    return res.get('audioContent')
                else:
                    print(res)
                    raise Exception("some err:", res)
            else:
                raise Exception("some err:", r.text)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    tx = "Android is a mobile operating system developed by Google,based on the Linux kernel and designed primarily for touchscreen mobile devices such as smartphones and tablets.Android is a mobile operating system developed by Google,based on the Linux kernel and designed primarily for touchscreen mobile devices such as smartphones and tablets.Android is a mobile operating system developed by Google,based on the Linux kernel and designed primarily for touchscreen mobile devices such as smartphones and tablets.Android is a mobile operating system developed by Google,based on the Linux kernel and designed primarily for touchscreen mobile devices such as smartphones and tablets."
    voicename = 'en-GB-Standard-A-FEMALE'
    voice, gender = voicename.rsplit('-', maxsplit=1)

    ca = RequestsTextToSpeech()
    print(ca.create_audio(tx, voice, gender))