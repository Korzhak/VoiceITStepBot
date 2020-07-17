# -*- coding: utf-8 -*-
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "file.json"


def sample_long_running_recognize(local_file_path):
    client = speech_v1.SpeechClient()

    language_code = "uk-UA"

    sample_rate_hertz = 16000

    encoding = enums.RecognitionConfig.AudioEncoding.OGG_OPUS
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()
    my_array = []
    for result in response.results:
        alternative = result.alternatives[0]
        my_array.append(u"{}".format(alternative.transcript))
    return my_array

