import os

from flask import Flask, request
from telebot import types

import telebot

TOKEN = '5247457206:AAFAMn-l0VUmGxNYjq5USBAdGVMhqSVLVtQ'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


#КОД ТЕЛЕБОТА
from IPython.lib.display import Audio
import telebot
import random
from telebot import types
from gtts import gTTS # импорт библиотеки, которую мы скачали
bot = telebot.TeleBot("5247457206:AAFAMn-l0VUmGxNYjq5USBAdGVMhqSVLVtQ")

anekdot=["Новогодняя ночь. На операционном столе орёт благим матом парень с аппендицитом. Бьют куранты, доктор надевает марлевую маску: — Ну-с, коллеги, с Новым годом, прошу всех к столу!",
"— Доктор, наша маленькая дочь стабильно теряет в весе. Мы и физические упражнения с ней делаем, и много на воздухе бываем.. — А как она ест? — Ах, черт подери, я чувствовала что мы что-то забываем!",
"Врачи делятся на три категории: Врач от Бога    Врач — ну, с Богом!,    Врач — не дай Бог!",
"У меня два кота. Утром, когда они хотят жрать, они не орут, а просто рассаживаются вокруг меня на спинке дивана, как гаргульи, и тупо смотрят на меня, пока я глаза не открою.",
"Понты — это когда в руке айфон, а в квартире последний раз ремонт в 80-е делали.",
"Дочь олигарха приводит простого парня знакомиться с родителями! Отец парню: квартира есть? Парень: Бог даст, будет! Отец: машина есть? Парень: Бог даст, будет! Отец: дочь мою обеспечить сможешь? Парень: Бог даст, обеспечу! Мать: ну, как он тебе? Отец: лох лохом, НО МНЕ ТАК НРАВИТСЯ, КАК ОН МЕНЯ НАЗЫВАЕТ!",
"Фраза: « Ну, не будем Вам мешать! » означает, что помогать Вам никто не собирается...",
"Один товарищ рассказывал. Шел он с работы, нес в сумке баллончик с золотой краской — оформлял стенд на работе. И вот подходит к нему цыганка и нагло требует: А позолоти ручку!    Думаю, что было дальше, и так ясно...",
"Маленький мальчик приходит из десткого сада весь исцарапаный. Папа спрашивает: — В чём дело? — Да хороводы вокруг ёлки водили. — Ну и что? — Ёлка большая, а детей мало!",
"Приезжие туристы в одном отеле на побережье: — Скажите, а вот медузы или там морские ежи на пляжах встречаются? — Да ну что вы! Какие там ежи! Акулы съедают все подчистую",
"Полицейские приедут намного быстрее, если вы начнете их оскорблять по телефону.",
"Американцы собираются на Марс... У них почти всё готово - съёмочная группа, декорации... Осталось лишь выпилить ракету и натереть кирпича...",
"К сожалению, Ольга Бузова сообщила, что не приостановит свою деятельность на территории РФ.",
"В кофейне сидит за столом человек без смартфона, без ноутбука, просто пьет кофе: короче, выглядит, как психопат!",
"ПРОКУРОР: Доктор, перед тем, как начать вскрытие, Вы проверили пульс? ОБВИНЯЕМЫЙ: Нет. ПРОКУРОР: Вы проверили кровяное давление? ОБВИНЯЕМЫЙ: Нет. ПРОКУРОР: Вы убедились, что нет дыхания? ОБВИНЯЕМЫЙ: Нет. ПРОКУРОР: Тогда возможно, что пациент был жив, когда Вы начали вскрытие?! ОБВИНЯЕМЫЙ: Нет. ПРОКУРОР: Почему Вы так уверены? ОБВИНЯЕМЫЙ: Потому, что его мозги были в банке на моем письменном столе. ПРОКУРОР: Понятно... Но тем не менее – мог ли пациент еще быть жив??! ОБВИНЯЕМЫЙ: Да. Возможно, что он был еще жив и даже практиковал в области юриспруденции..."
]

mem=["mem1.jpg","mem2.jpg","mem3.jpg","mem4.jpg","mem5.jpg","mem6.jpg","mem7.jpg","mem8.jpg","mem9.jpg","mem10.jpg","mem11.jpg","mem12.jpg","mem13.jpg",]




@bot.message_handler(commands=['start'])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add('Привет')
    keyboard.add('анекдот')
    keyboard.add('мем')
    keyboard.add('random 100')
    keyboard.add('random ot do')
    bot.send_message(message.chat.id,"обработкААА", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет": 
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
  elif message.text == "анекдот":
    ankd= random.choice(anekdot)
    text = ankd # текст, который мы хотим перевести в речь
    audio = gTTS(text, lang = 'ru') # функция, которая переводит текст в речь
    audio.save('audio.mp3')
    audio = open("audio.mp3","rb") 
    bot.send_voice(message.from_user.id, audio)
    audio.close()
  elif message.text == "мем":
    me= open(random.choice(mem),"rb")
    bot.send_photo(message.from_user.id, me)
    me.close()
  elif message.text == "random 100":
    rand = random.randint(0,100)
    bot.send_message(message.from_user.id, "ваше число: "+ str(rand))
  else:
    bot.send_message(message.from_user.id, "МОЯ ТВОЯ НЕПОНИМАТ")

ot = 0
do = 0

@bot.message_handler(commands=['random ot do'])
def get_random(message):
  bot.send_message(message.from_user.id, "от? ")
  bot.register_next_step_handler(message, get_random2)

def get_random2(message):
  global ot
  ot = int(message.text)
  bot.send_message(message.from_user.id, "до? ")
  bot.register_next_step_handler(message, random_out)

def random_out(message):
  global do
  do = int(message.text)
  bot.send_message(message.from_user.id, random.randint(ot, do))

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
    
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://<test5252573636>.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
bot.polling(none_stop = True)
