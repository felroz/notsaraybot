import telebot

token = '2145284613:AAHRPfaLDW_jPgNoD9aE7pgkmxDENPhAZ8U'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'salam!')

bot.polling()