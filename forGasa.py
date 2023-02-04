from telebot import types,telebot
import api

bot = telebot.TeleBot(api.API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Oz hesabina basvuru") 
    btn2 = types.KeyboardButton("Guz donemi")
    btn3 = types.KeyboardButton("Burs icin gerekli belgeler")
    btn4 = types.KeyboardButton("Dim senedleri ucun")
    btn5 = types.KeyboardButton("Çin")
    btn6 = types.KeyboardButton("Gasa")
    
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
    
    send_mess = f"<b>Salam {message.from_user.first_name}!</b>\nNe lazimdii"

    bot.send_message(message.chat.id, send_mess, parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    finalMessage = ""

    get_message_bot = message.text.strip()
    if get_message_bot == "Oz hesabina basvuru":
        finalMessage='https://gasacompany.com/bahar-donem-basvuru-icin-gerekli-belgeler/'
    elif get_message_bot == 'Guz donemi':
        finalMessage='https://gasacompany.com/bahar-donem-basvuru-icin-gerekli-belgeler'
    elif get_message_bot=="Burs icin gerekli belgeler":
        finalMessage='https://docs.google.com/document/d/1D42xwi2uvDn5f4K6YQPkeVTUF5w9belq/edit'
    bot.send_message(message.chat.id, finalMessage, parse_mode='html')        
bot.polling(none_stop=True)

print(bot)