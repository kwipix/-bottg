from email import message
import telebot
import webbrowser
from telebot import types
import requests
from bs4 import BeautifulSoup


bot = telebot.TeleBot("6401961519:AAGhsgJq5x4ICBpMqnWe_TG38B_6xujAPFg")

selected_day = ""


@bot.message_handler(commands=["site", 'website'])
def site(message):
    webbrowser.open('https://kipt.sumdu.edu.ua/uk/')


# Декораток message_heandler and параметр commands
@bot.message_handler(commands=['start'])
def start(message):
    # resize_keyboard для маленького розміру кнопок
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Розклад")
    button2 = types.KeyboardButton("Заміни")
    markup.add(button1, button2)

    bot.send_message(message.chat.id, f"Привіт! {message.from_user.first_name}", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Розклад')
def roklad(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pn = types.KeyboardButton("Понеділок")
    vt = types.KeyboardButton("Вівторок")
    sr = types.KeyboardButton("Середа")
    ch = types.KeyboardButton("Четвер")
    pt = types.KeyboardButton("П\'ятниця")
    markup.row(pn,vt,sr)
    markup.row(ch,pt)
    bot.send_message(message.chat.id, f'Виберіть день неділі', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in ['Понеділок','Вівторок','Середа','Четвер','П\'ятниця'])
def roklad(message):
    global selected_day
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kyrs1 = types.KeyboardButton("1 курс")
    kyrs2 = types.KeyboardButton("2 курс")
    markup.row(kyrs1,kyrs2)
    kyrs3 = types.KeyboardButton("3 курс")
    kyrs4 = types.KeyboardButton("4 курс")
    markup.row(kyrs3,kyrs4)
    selected_day = message.text
    bot.send_message(message.chat.id, f'Виберіть курс', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text   == '1 курс')
def kyrs1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    group911 = types.KeyboardButton('911')
    group711 = types.KeyboardButton('711')
    group5611 = types.KeyboardButton('511/611')
    group311 = types.KeyboardButton('311')
    group8111 = types.KeyboardButton('111/811')
    markup.row(group911,group711,group311)
    markup.row(group8111,group5611)
    bot.send_message(message.chat.id, f'Вибери группу', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '911')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs1/911/911pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs1/911/911vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs1/911/911sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs1/911/911ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs1/911/911pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '711')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs1/711/711pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs1/711/711vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs1/711/711sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs1/711/711ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs1/711/711pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '311')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs1/311/311pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs1/311/311vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs1/311/311sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs1/311/311ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs1/311/311pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '511/611')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs1/5611/5611pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs1/5611/5611vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs1/5611/5611sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs1/5611/5611ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs1/5611/5611pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '111/811')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs1/811/811pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs1/811/811vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs1/811/811sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs1/811/811ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs1/811/811pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '2 курс')
def kyrs2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    group121 = types.KeyboardButton('121')
    group122 = types.KeyboardButton('122')
    group221 = types.KeyboardButton('221')
    group321 = types.KeyboardButton('321')
    group322 = types.KeyboardButton('322')
    group421 = types.KeyboardButton('421')
    group5621 = types.KeyboardButton('521/621')
    group702 = types.KeyboardButton('702')
    group821 = types.KeyboardButton('821')
    markup.row(group121,group122,group221)
    markup.row(group321,group322,group421)
    markup.row(group5621, group702, group821)
    bot.send_message(message.chat.id, f'Вибери группу', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '121')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs2/121/121pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs2/121/121vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs2/121/121sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs2/121/121ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs2/121/121pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '122')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs2/122/122pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs2/122/122vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs2/122/122sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs2/122/122ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs2/122/122pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '221')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs2/221/221pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs2/221/221vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs2/221/221sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs2/221/221ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs2/221/221pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '321')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs2/321/321pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs2/321/321vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs2/321/321sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs2/321/321ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs2/321/321pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '322')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs2/322/322pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs2/322/322vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs2/322/322sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs2/322/322ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs2/322/322pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '421')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs2/421/421pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs2/421/421vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs2/421/421sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs2/421/421ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs2/421/421pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '702')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs2/702/702pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs2/702/702vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs2/702/702sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs2/702/702ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs2/702/702pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '721')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs2/721/721pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs2/721/721vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs2/721/721sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs2/721/721ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs2/721/721pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '821')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs2/821/821pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs2/821/821vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs2/821/821sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs2/821/821ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs2/821/821pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

    @bot.message_handler(func=lambda message: message.text == '521/621')
    def on_click(message):
        global selected_day
        if selected_day == 'Понеділок':
            file = open('kyrs2/5621/5621pn.png', 'rb')
            bot.send_photo(message.chat.id, file)
        elif selected_day == 'Вівторок':
            file = open('kyrs2/5621/5621vt.png', 'rb')
            bot.send_photo(message.chat.id, file)
        elif selected_day == 'Середа':
            file = open('kyrs2/5621/5621sr.png', 'rb')
            bot.send_photo(message.chat.id, file)
        elif selected_day == 'Четвер':
            file = open('kyrs2/5621/5621ch.png', 'rb')
            bot.send_photo(message.chat.id, file)
        elif selected_day == 'П\'ятниця':
            file = open('kyrs2/5621/5621pt.png', 'rb')
            bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '3 курс')
def kyrs2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    group131 = types.KeyboardButton('131')
    group132 = types.KeyboardButton('132')
    group231 = types.KeyboardButton('231')
    group331 = types.KeyboardButton('331')
    group332 = types.KeyboardButton('332')
    group431 = types.KeyboardButton('431')
    group531 = types.KeyboardButton('531')
    group631 = types.KeyboardButton('631')
    group703 = types.KeyboardButton('703')
    group731 = types.KeyboardButton('731')
    markup.row(group131, group132, group231)
    markup.row(group331, group332, group431)
    markup.row(group531,group631, group703, group731)
    bot.send_message(message.chat.id, f'Вибери группу', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '131')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs3/131/131pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs3/131/1311vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs3/131/131sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs3/131/131ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs3/131/131pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '132')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs3/132/132pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs3/132/1321vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs3/132/132sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs3/132/132ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs3/132/132pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '231')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs3/231/231pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs3/231/2311vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs3/231/231sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs3/231/231ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs3/231/231pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '331')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs3/331/331pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs3/331/331vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs3/331/331sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs3/331/331ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs3/331/331pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '332')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs3/332/332pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs3/332/332vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs3/332/332sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs3/332/332ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs3/332/332pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '431')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs3/431/431pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs3/431/431vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs3/431/431sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs3/431/431ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs3/431/431pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '531')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs3/531/531pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs3/531/531vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs3/531/531sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs3/531/531ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs3/531/531pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '631')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs3/631/631pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs3/631/631vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs3/631/631sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs3/631/631ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs3/631/631pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '703')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs3/703/703pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs3/703/703vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs3/703/703sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs3/703/703ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs3/703/703pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '731')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs3/731/731pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs3/731/731vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs3/731/731sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs3/731/731ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs3/731/731pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == '4 курс')
def kyrs1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    group142 = types.KeyboardButton('142')
    group342 = types.KeyboardButton('342')
    group741 = types.KeyboardButton('741')
    group941 = types.KeyboardButton('941')
    markup.row(group142,group342)
    markup.row(group741,group941)
    bot.send_message(message.chat.id, f'Вибери группу', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '142')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs4/142/142pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs4/142/142vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs4/142/142sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs4/142/142ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs4/142/142pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '342')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs4/342/342pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs4/342/342vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs4/342/342sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs4/342/342ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs4/342/342pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '741')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs4/741/741pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs4/741/741vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs4/741/741sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs4/741/741ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs4/741/741pt.png', 'rb')
        bot.send_photo(message.chat.id, file)

@bot.message_handler(func=lambda message: message.text == '941')
def on_click(message):
    global selected_day
    if selected_day == 'Понеділок':
        file = open('kyrs4/941/941pn.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Вівторок':
        file = open('kyrs4/941/941vt.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Середа':
        file = open('kyrs4/941/941sr.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'Четвер':
        file = open('kyrs4/941/941ch.png', 'rb')
        bot.send_photo(message.chat.id, file)
    elif selected_day == 'П\'ятниця':
        file = open('kyrs4/941/941pt.png', 'rb')
        bot.send_photo(message.chat.id, file)


# Функция для извлечения данных о заменах
def scrape_replacements():
    url = 'https://kipt.sumdu.edu.ua/uk/zaminy-na-zavtra'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        data = []

        for row in table.find_all('tr')[1:]:
            cells = row.find_all('td')
            group = cells[0].text.strip()
            lesson_number = cells[1].text.strip()
            subject_old = cells[2].text.strip()
            subject_new = cells[3].text.strip()
            classroom = cells[4].text.strip()

            if group:  # Перевіряємо, що значення групи не є порожнім
                data.append(
                    f"*Група:* {group}\n*Номер пари:* {lesson_number}\n*Предмет (старий):* {subject_old}\n*Предмет (новий):* {subject_new}\n*Аудиторія:* {classroom}\n")

        message = '\n\n'.join(data)
        return message
    else:
        return "Помилка при отриманні сторінки. Спробуйте пізніше."



@bot.message_handler(func=lambda message: message.text == 'Заміни')
def get_replacements(message):
    replacements = scrape_replacements()
    bot.send_message(message.chat.id, replacements, parse_mode='Markdown')



bot.polling(none_stop=True)