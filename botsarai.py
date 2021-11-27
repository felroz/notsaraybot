import telebot;
bot = telebot.TeleBot('2145284613:AAHRPfaLDW_jPgNoD9aE7pgkmxDENPhAZ8U');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "salam":
        bot.send_message(message.from_user.id, "alekum")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "pomosh")
    else:
        bot.send_message(message.from_user.id, "izvinis")
    bot.polling(none_stop=True, interval=0)