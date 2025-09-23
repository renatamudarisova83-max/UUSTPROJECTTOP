import telebot
from telebot import types
import webbrowser

bot=telebot.TeleBot('8466977919:AAH9aIL-BK6zP45iktikLGwLQ01oSCzTaj4')
@bot.message_handler(commands=['isu'])
# def ISU(message):
#     webbrowser.open('https://isu.uust.ru/')
@bot.message_handler(content_types=['photo'])
def getphotomess(message):
    bot.reply_to(message,'Классное фото, но зачем🧐')
@bot.message_handler(content_types=['voice'])
def getaudioomess(message):
    bot.reply_to(message,'не хочу слушать, эммм')
@bot.message_handler(commands=['start','привет','Привет'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton('👩‍💻 Открыть ИСУ/Open ISU 👩‍💻','https://isu.uust.ru/')
    btn2 = types.InlineKeyboardButton('📅 Расписание/Schedule 📅', callback_data='schedule')
    btn3 = types.InlineKeyboardButton('🅿️ Парковки/Parking place 🅿️',callback_data='parking')
    btn4 = types.InlineKeyboardButton('🗺️ Карта Университета/University map 🗺️', callback_data='map')
    btn5 = types.InlineKeyboardButton('🪩 Скорые мероприятия/Upcomming events 🪩',callback_data='events')
    btn6=types.InlineKeyboardButton('🍱 Где покушать/Where can go to eat 🍱',callback_data='eat')
    btn7=types.InlineKeyboardButton('🔎 Быстрый поисковик Yandex 🔍','https://dzen.ru/?clid=2233626&yredirect=true')
    btn8 = types.InlineKeyboardButton('🍽️ Доставка еды 🍽️', callback_data='food')
    btn9 = types.InlineKeyboardButton('🚗 Такси 🚗', callback_data='tax')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn4)
    markup.row(btn6)
    markup.row(btn5)
    markup.row(btn3)
    markup.row(btn7)
    markup.row(btn8)
    markup.row(btn9)
    bot.send_message(message.chat.id,'Привет!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):

    if call.data == 'schedule':
        # Создаем подменю для расписания
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1️⃣', callback_data='gr1')
        btn2 = types.InlineKeyboardButton('2️⃣', callback_data='gr2')
        btn3 = types.InlineKeyboardButton('3️⃣', callback_data='gr3')
        btn4 = types.InlineKeyboardButton('4️⃣', callback_data='gr4')
        markup.row(btn1, btn2)
        markup.row(btn3,btn4)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        # bot.send_message(message.chat.id, 'Выберите номер курса', reply_markup=markup)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите номер курса',
            reply_markup=markup
        )
    elif call.data == 'food':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('delivery club', 'https://market-delivery.yandex.ru/moscow?shippingType=delivery')
        btn2 = types.InlineKeyboardButton('Самокат', 'https://samokat.ru/?ysclid=mfwi1bbyfa848881559')
        btn3 = types.InlineKeyboardButton('Яндекс еда', 'https://eda.yandex.ru/moscow?shippingType=delivery')
        btn4 = types.InlineKeyboardButton('Купер', 'https://kuper.ru/?utm_referrer=https%3a%2f%2fyandex.ru%2f')
        markup.row(btn1, btn2)
        markup.row(btn3,btn4)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите заведение, в котором хотите покушать',
            reply_markup=markup
        )
    elif call.data == 'tax':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('🚕 Yandex GO 🚕',
                                          'https://taxi.yandex.ru/?ysclid=mfwiar5t6q617677941')
        btn2 = types.InlineKeyboardButton('🚕 Максим 🚕', 'https://ufa.taximaxim.ru/?ysclid=mfwiboxfgy828446211')
        btn3 = types.InlineKeyboardButton('🚕 Везет 🚕', 'https://vezet.ru/ufa?ysclid=mfwical2c3975498416')
        btn4 = types.InlineKeyboardButton('🚕 Поехали 🚕', 'https://ufa.taxipoehali.ru/client/?intl=ru-RU&ysclid=mfwides7rk369543506')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите заведение, в котором хотите покушать',
            reply_markup=markup
        )
    elif call.data == 'eat':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('☕️ Кафе ☕️', callback_data='kafe')
        btn2 = types.InlineKeyboardButton('🦪 Рестораны 🦪', callback_data='restor')
        btn3 = types.InlineKeyboardButton('🍲 Столовые 🍲', callback_data='stol')
        markup.row(btn1, btn2)
        markup.row(btn3)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите заведение, в котором хотите покушать',
            reply_markup=markup
        )

    elif call.data == 'kafe':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='фото'
        )
    elif call.data == 'restor':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должно быть какой-то текст'
        )
    elif call.data == 'stol':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должно быть какой-то текст'
        )

    elif call.data == 'parking':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('🅿️🆓 Бесплатная парковка 🆓🅿️', callback_data='free')
        btn2 = types.InlineKeyboardButton('🅿️💰 Платная парковка 💰🅿️', callback_data='paid')
        markup.row(btn1, btn2)

        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Информация о парковке',
            reply_markup = markup
        )
    elif call.data == 'free':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должно быть фото и какой-то текст'
        )
    elif call.data == 'paid':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должно быть фото и какой-то текст'
        )
    elif call.data == 'map':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('1️⃣', callback_data='k1')
        btn2 = types.InlineKeyboardButton('2️⃣', callback_data='k2')
        btn3 = types.InlineKeyboardButton('3️⃣', callback_data='k3')
        btn4 = types.InlineKeyboardButton('4️⃣', callback_data='k4')
        btn5 = types.InlineKeyboardButton('5️⃣', callback_data='k5')
        btn6 = types.InlineKeyboardButton('6️⃣', callback_data='k6')
        btn7 = types.InlineKeyboardButton('7️⃣', callback_data='k7')
        btn8 = types.InlineKeyboardButton('8️⃣', callback_data='k8')
        btn9 = types.InlineKeyboardButton('9️⃣', callback_data='k9')
        markup.row(btn1, btn2,btn3 ,btn4)
        markup.row(btn5,btn6,btn7,btn8,btn9)

        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)

        bot.edit_message_text(

            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=' тут должно быть фото и выберете корпус',
            reply_markup=markup

        )
    elif call.data == 'k1':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должна быть инфа о 1 корпусе'
        )
    elif call.data == 'k2':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должна быть инфа о 2 корпусе'
        )
    elif call.data == 'k3':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должна быть инфа о 3 корпусе'
        )
    elif call.data == 'k4':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должна быть инфа о 4 корпусе'
        )
    elif call.data == 'k5':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должна быть инфа о 5 корпусе'
        )
    elif call.data == 'k6':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должна быть инфа о 6 корпусе'
        )

    elif call.data == 'k7':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должна быть инфа о 7 корпусе'
        )
    elif call.data == 'k8':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должна быть инфа о 8 корпусе'
        )
    elif call.data == 'k9':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='тут должна быть инфа о 9 корпусе'
        )
    elif call.data == 'events':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Предстоящие события: https://vk.com/wall-216069379_2920 '

        )

    elif call.data == 'gr1':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('ТОП-101Б 1️⃣', callback_data='top1')
        btn2 = types.InlineKeyboardButton('ТОП-102И 2️⃣', callback_data='top2')
        btn3 = types.InlineKeyboardButton('💖 ТОП-103Б 💖', callback_data='top3')
        btn4 = types.InlineKeyboardButton('ТОП-104Б4️⃣', callback_data='top4')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите группу',
            reply_markup = markup
        )
    elif call.data == 'top3':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('эта неделя', 'https://isu.uust.ru/schedule_2024/')
        btn2 = types.InlineKeyboardButton('следущая неделя', 'https://isu.uust.ru/schedule_2024/')

        markup.row(btn1, btn2)
        btn100 = types.InlineKeyboardButton('🔙 Вернуться в главное меню 🔙', callback_data='back_main')
        markup.row(btn100)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Выберите неделю',
            reply_markup = markup
        )
    elif call.data == 'top1':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'

        )
    elif call.data == 'top2':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'

        )
    elif call.data == 'top4':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'

        )

    elif call.data == 'gr2':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'

        )
    elif call.data == 'gr3':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'

        )
    elif call.data == 'gr4':
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Расписание на сегодня:\n\n9:00 - Математика (ауд. 101)\n11:00 - Физика (ауд. 205)\n14:00 - Программирование (ауд. 310)'

        )

    elif call.data == 'back_main':
        # Возврат к главному меню
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('👩‍💻 ИСУ Личный кабинет/ISU Personal account 👩‍💻', url='http://isu.uest.ru/')
        btn2 = types.InlineKeyboardButton('📅 Расписание/Schedule 📅', callback_data='schedule')
        btn3 = types.InlineKeyboardButton('🅿️ Парковка/Parking place 🅿️', callback_data='parking')
        btn4 = types.InlineKeyboardButton('🗺️ Карта университета/University map 🗺️', callback_data='map')
        btn5 = types.InlineKeyboardButton('🪩 Предстоящие события/Upcomming events 🪩', callback_data='events')
        btn6 = types.InlineKeyboardButton('🍱 Где покушать/Where can go to eat 🍱',callback_data='eat')
        btn7 = types.InlineKeyboardButton('🔎 Быстрый поисковик Yandex 🔍',
                                          'https://dzen.ru/?clid=2233626&yredirect=true')
        btn8 = types.InlineKeyboardButton('🍽️ Доставка еды 🍽️', callback_data='food')
        btn9 = types.InlineKeyboardButton('🚗 Такси 🚗', callback_data='tax')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn4)
        markup.row(btn6)
        markup.row(btn5)
        markup.row(btn3)
        markup.row(btn7)
        markup.row(btn8)
        markup.row(btn9)

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text='Главное меню:',
            reply_markup=markup
        )

bot.polling(none_stop=True)
