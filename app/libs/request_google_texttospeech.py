#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import base64
from google.cloud import texttospeech
__author__ = 'caijinxu'


class google_text2speech:
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()

    def create_voice(self, text, lang='en-US', gender='MALE'):
        synthesis_input = texttospeech.types.SynthesisInput(text=text)
        if gender == "MALE":
            voice = texttospeech.types.VoiceSelectionParams(language_code=lang,
                                                            ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
        elif gender == "FEMALE":
            voice = texttospeech.types.VoiceSelectionParams(language_code=lang,
                                                            ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)
        elif gender == "NEUTRAL":
            voice = texttospeech.types.VoiceSelectionParams(language_code=lang,
                                                            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
        else:
            voice = texttospeech.types.VoiceSelectionParams(language_code=lang,
                                                            ssml_gender=texttospeech.enums.SsmlVoiceGender.
                                                            SSML_VOICE_GENDER_UNSPECIFIED)
        audio_config = texttospeech.types.AudioConfig(audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)
        response = self.client.synthesize_speech(synthesis_input, voice, audio_config)
        if response.audio_content:
            # print(base64.b64encode(response.audio_content))
            return json.dumps((base64.b64encode(response.audio_content).decode()))
        else:
            return ''

    def supported_voices(self):
        voices = self.client.list_voices()
        result = list()
        ssml_voice_genders = ['SSML_VOICE_GENDER_UNSPECIFIED', 'MALE', 'FEMALE', 'NEUTRAL']
        for voice in voices.voices:
            r = {
                'name': voice.name,
                'gender': ssml_voice_genders[voice.ssml_gender]
            }
            result.append(r)
        return result

