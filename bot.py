from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from voice_recognition import sample_long_running_recognize

TOKEN = "<your_token>"



updater = Updater(token="1240808732:AAEnrwFwIa98YsANRiqGv9aAiVdSt08kpsw", use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привіт. Я твій перший бот")

def echo(update, context):
    response = "Ваше повідомлення: " + update.message.text
    context.bot.send_message(chat_id=update.message.chat_id, text=response)

def speech(update, context):
    file = context.bot.getFile(update.message.voice)
    file.download("saved/voice.ogg")

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--local_file_path", type=str, default="saved/voice.ogg"
    )
    args = parser.parse_args()

    response = sample_long_running_recognize(args.local_file_path)[0]
    context.bot.send_message(chat_id=update.message.chat_id, text=response)

def main():
    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(Filters.text, echo)
    speech_handler = MessageHandler(Filters.voice, speech)

    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(speech_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
