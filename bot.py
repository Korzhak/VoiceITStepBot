from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from voice_recognition import sample_long_running_recognize

TOKEN = "<your_token>"                             # Токен для доступу до вашого бота



updater = Updater(token=TOKEN, use_context=True)   # Робимо перший запит до телеграму і створюємо об'єкт, який буде приймати зміни від телеграму
dispatcher = updater.dispatcher                    # Створюємо об'єкт диспетчера, що буде розподіляти повідомлення по типу


def start(update, context):
    # Функція, що реагує на команду "/start"
    context.bot.send_message(chat_id=update.message.chat_id, text="Привіт. Я твій перший бот")

def echo(update, context):
    # Функція, що відповідає на невідомі повідомлення тим же текстом
    response = "Ваше повідомлення: " + update.message.text
    context.bot.send_message(chat_id=update.message.chat_id, text=response)

def speech(update, context):
    # Функція, що розпізнає голос та переводить його в текст і відправляє користувачу
    file = context.bot.getFile(update.message.voice)                          # Витягуємо файл аудіоповідомлення
    file.download("saved/voice.ogg")                                          # Зберігаємо його в проекті в папці "saved/"

    import argparse  
    # Викликаємо бібліотеку, що працює з Google Speech-to-Text
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local_file_path", type=str, default="saved/voice.ogg"              # Передаємо файл з голосом користувача для розпізнавання
    )
    args = parser.parse_args()

    response = sample_long_running_recognize(args.local_file_path)[0]         # Отримуємо текст зі звукозапису
    context.bot.send_message(chat_id=update.message.chat_id, text=response)   # Відправляємо текст користувачу

def main():
    start_handler = CommandHandler("start", start)                            # Створюємо об'єкти-хендлери, які відповідають
    echo_handler = MessageHandler(Filters.text, echo)                         # за конкретний тип повідомлень, і передаємо їм
    speech_handler = MessageHandler(Filters.voice, speech)                    # посилання на функцію, яку потрібно викликати

    dispatcher.add_handler(echo_handler)                                      # Додаємо ці хендлери в диспетчер, який буде реагувати 
    dispatcher.add_handler(start_handler)                                     # на вхідні повідомлення і викликати потрібний 
    dispatcher.add_handler(speech_handler)                                    # хендлер при конкретному типі повідомлень

    updater.start_polling()                                                   # Запускаємо нашого бота типом "полінг". 
                                                                              # ^ раще це робити через веб-хуки, але воно складніше в реалізації


if __name__ == '__main__':
    # Запускаємо на виконання головну функцію
    main()   
