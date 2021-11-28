import telebot;
bot = telebot.TeleBot('2145284613:AAHRPfaLDW_jPgNoD9aE7pgkmxDENPhAZ8U');
@bot.message_handler(commands=['start'])
def start_message(message):

    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет', 'Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока','Пока')
    bot.send_message(message.chat.id,"Здравствуйте.", reply_markup=keyboard)
    
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,"/////////////")
@bot.message_handler(commands=['week'])
def start_message(message):
    bot.send_message(message.chat.id,"\\\\\\\\\\\\")
    
    
    
    
    
    
    
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "салам")
    else:
        bot.send_message(message.from_user.id, "Извините, вас плохо слышно, повторите пожалуйста еще раз")
        
bot.polling(none_stop=True, interval=0)