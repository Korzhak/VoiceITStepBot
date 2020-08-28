
# Коротка інструкція

Перед тим як почати роботу, нам потрібно створити проект та встановити модулі для роботи програми. 

Встановлення модуля для роботи з телеграмом
```
pip install python-telegram-bot
```

Встановлення модуля для роботи з Google-cloud-speech
```
pip install google-cloud-speech
```

Далі потрібно в файлі `bot.py` в змінну `TOKEN` занести отриманий ключ від BotFather (https://t.me/BotFather)
```python
TOKEN = "1240808732:AAEnrwFwIa98YsANRiqGv9aAiVdSt08kpsw"
```


Для отримання ключа від Google Speech To Text варто прочитати документацію за посиланням: https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries#client-libraries-usage-python

[Покроковий урок з налаштування доступу до Google Speech-to-Text](https://fspace.team/blog/5/)

В файлі `voice_recognition.py` вставляємо посилання на наш ключ з розширенням Json
```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "YourPublicKey.json"
```
І після цього запускаємо файл `bot.py` і насолоджуємося роботою бота:)

----
Код-приклад з офіційної бібліотеки google-cloud-speech: https://github.com/googleapis/python-speech/blob/master/samples/v1/speech_transcribe_async.py
