from telebot import types,telebot
import os
import api
import yok
bot = telebot.TeleBot("5643056415:AAHqabQaPTc0nsv3F14eV06sIXTUWcMnt2c")
path = "./refs"




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Öz hesabına başvuru") 
    btn2 = types.KeyboardButton("Burs")
    btn3 = types.KeyboardButton("DİM sənədləri")
    btn4 = types.KeyboardButton("OTB")
    btn5 = types.KeyboardButton("Yeni qoşulanlar üçün")
    btn6 = types.KeyboardButton("Nümunələr")
    markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
    send_mess = f"<b>Salam {message.from_user.first_name}!</b>\nNə lazimdır?"

    bot.send_message(message.chat.id, send_mess, parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    finalMessage = ""
    get_message_bot = message.text.strip()
  
    if get_message_bot == "Öz hesabına başvuru":
        guz = open("./docs/senedler.pdf","rb")
        bot.send_document(message.chat.id, guz)

    elif get_message_bot == 'Burs':
        bot.send_document(message.chat.id, document=open('./docs/BursRec.docx', 'rb'))

    elif get_message_bot=="DİM sənədləri":
        finalMessage='https://eservices.dim.gov.az/sagird/indexsh.aspx?frm=egov'
    
    elif get_message_bot=="OTB":
        finalMessage=yok.message
        
        bot.send_photo(message.chat.id, photo=open('./docs/card.jpeg', 'rb'))

    elif get_message_bot=='Yeni qoşulanlar üçün':
        steps = open("./docs/addımlar.pdf","rb")
        bot.send_document(message.chat.id, steps)

    elif get_message_bot == "Nümunələr":
        filelist = os.listdir(path)
        for x in filelist:
            bot.send_document(message.chat.id,document=open(path+"/"+x,'rb'))
                        
    bot.send_message(message.chat.id, finalMessage, parse_mode='html')        
bot.polling(none_stop=True)

    