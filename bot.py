import config
import telebot
import sqlite3
import db
from telebot import types
import sys


bot = telebot.TeleBot(config.Token)
@bot.message_handler(commands=['start'])
def first(message):
    keyboard = types.ReplyKeyboardMarkup(True,False)
    keyboard.row('/openday','/course')
    keyboard.row('/specialties','/guide')
    keyboard.row('/contacts','/studorganizations')
    keyboard.row('/map','/calculator')
    send = bot.send_message(message.chat.id, 'Выберите команду!',reply_markup=keyboard)
    bot.register_next_step_handler(send,second)
def SpecialtielsComand(message):
    if message.text == 'Бакалавриат':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,
                                'Номер/Направление/Описание/Экзамены/Кол-во бюджетных мест/Кол-во'
                                ' контррактных мест/Цена\n\n'+ db.res_bak,
                                reply_markup=keyboard)
        bot.register_next_step_handler(send,first)
    elif message.text == 'Специалитет':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,'Номер/Направление/Описание/Экзамены'
                                                '/Кол-во бюджетных мест/Кол-во контррактных мест/'
                                                'Цена\n\n'+ db.result_spec, reply_markup=keyboard)
        bot.register_next_step_handler(send,first)
    else:
        error(message)
def ContactsComand(message):
    if message.text == 'Меню':
        first(message)
    else:
        error(message)
def StudOrgComand(message):
    if message.text == 'Молодежный клуб РГО':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,
        'ВОО "Русское географическое общество" совместно с Федеральным государственным бюджетным образовательным учреждением высшего образования "Московский государственный университет геодезии и картографии" в рамках организации деятельности и популяризации таких направлений как география, картография и смежные науки создали Молодёжный клуб РГО на базе МИИГАиК.Подробнее на сайте: https://mk.rgo.ru/https://sun9-36.userapi.com/impf/c636029/v636029908/3c94b/mwB2aB76rjA.jpg?size=1280x905&quality=96&proxy=1&sign=a3aab35ffcfe401006b8586f4a2915bf&type=album', reply_markup=keyboard)
        bot.register_next_step_handler(send,first)
    elif message.text == 'Спортивные секции':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,
        'Целью "Студенческого спортивного клуба МИИГАиК" является сплочение студентов по спортивным интересам как внутри вуза так и за его пределами, проведение спортивно-массовых мероприятий, формирование сборных команд университета, создание условий для повышения спортивного мастерства студентов, популяризация спорта и здорового образа жизни! В рамках работы кафедры физического воспитания работает ряд секций: Подробную информацию можно узнать в группе: https://vk.com/miigaik_sport', reply_markup=keyboard)
        bot.register_next_step_handler(send,first)
    elif message.text == 'МИИГАиК МЕДИА':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Меню')
        bot.send_message(message.chat.id,'Вконтакте\nhttps://vk.com/miigaikmedia')
        send = bot.send_message(message.chat.id,'Инстаграм\nhttps://www.instagram.com/miigaik/', reply_markup = keyboard)
        bot.register_next_step_handler(send,first)
    elif message.text == 'ПРОФКОМ СТУДЕНТОВ':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,'Наш сайт\nhttps://mgugik.ru/', reply_markup=keyboard)
        bot.register_next_step_handler(send,first)
    elif message.text == 'Меню':
        first(message)
    else:
        error(message)
def MapComand(message):
    if message.text == 'Меню':
        first(message)
    else:
        error(message)
def CourseComand(message):
    if message.text == 'Подготовка к ЕГЭ':
        bot.send_message(message.chat.id, 'Получить более подробную информацию, а также записаться на курсы,можно перейдя по ссылке: http://www.miigaik.ru/applicants/courses/college/')
        first(message)
    elif message.text == 'Архитектурно-художественная школа':
        bot.send_message(message.chat.id, 'Архитектурно-художественная школа МИИГАиК\n Архитектурно-художественная школа (АХШ) - это подготовительные курсы, направленные на подготовку к сдаче вступительных экзаменов и к дальнейшему обучению на кафедре «Архитектуры и ландшафта» в МИИГАиК. Обучение в АХШ происходит по трём направлениям:\n  1.Черчение\n 2.Рисунок светотеневой (натюрморт)\n 3.Рисунок линейно-конструктивный (композиция)\n Срок обучения в школе – от 1 до 3 лет.\n Занятия проводятся 3 раза в неделю ведущими преподавателями кафедры архитектуры и ландшафта, кафедры архитектурного проектирования.\n')
        first(message)
    elif message.text == 'Меню':
       first(message)
    else:
        error(message)
@bot.message_handler(commands = ['url'])
@bot.message_handler(commands=['guide'])
def GuideComand(message):
    if message.text == 'Список документов':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        markup = types.InlineKeyboardMarkup()
        btn_my_priyom= types.InlineKeyboardButton(text='Заявление о приеме', url='http://www.miigaik.ru/pk/%D0%A4%D0%BE%D1%80%D0%BC%D0%B0%20%D0%B7%D0%B0%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BE%20%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D0%B5%202020.doc')
        btn_my_zachis= types.InlineKeyboardButton(text='Заявление о согласии на зачисление', url='http://www.miigaik.ru/pk/%D0%A4%D0%BE%D1%80%D0%BC%D0%B0%20%D1%81%D0%BE%D0%B3%D0%BB%D0%B0%D1%81%D0%B8%D1%8F%20%D0%BD%D0%B0%20%D0%B7%D0%B0%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%202020.doc')
        markup.add(btn_my_priyom)
        markup.add(btn_my_zachis)
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id, 'Поступающие в университет подают в приемную комиссию следующие документ\n1. заявление на имя ректора (заполняется на месте)\n 2. 2 фотографии размером 3х4 см <b>(после зачисления)</b> для личного дела\n 3. копию документа, удостоверяющего личность и гражданство; \n 4. <b>согласие</b> на обработку персональных данных;\n 5. согласие на зачисление по направлению.\n 6. информацию о результатах единых государственных экзаменов\n 7. документы, дающие право на льготы, установленные законодательством Российской Федерации\n 8. документ (копия/оригинал), удостоверяющий образование соответствующего уровня\n', reply_markup = markup)
        bot.register_next_step_handler(send,first)
    elif message.text == 'Меню':
        first(message)
    else:
        error(message)
def CalcComand(message):
    if float(message.text) < 216.0:
        bot.send_message(message.chat.id, 'К сожалению, твоих баллов не'
                                          ' хватает для поступления на бюджет. '
                                          'Но есть возможность поступить на комерческое обучение.'
                                          'Для ознакомления со специальностями перейди в раздел \n/specialties')
        first(message)
    if float(message.text) >= 216.0 and float(message.text) < 224:
        bot.send_message(message.chat.id, 'Направление подготовки «Информационные системы и технологии» Уровень образования: бакалавриат Форма обучения: очная. Срок обучения: 4 года Проходной балл: 216')
        first(message)
    if float(message.text) >= 216.0 and float(message.text) < 224:
        bot.send_message(message.chat.id, 'Направление подготовки «Информационные системы и технологии» Уровень образования: бакалавриат Форма обучения: очная. Срок обучения: 4 года Проходной балл: 216')  
        first(message)
    if float(message.text) >= 224 and float(message.text) < 230:
        bot.send_message(message.chat.id, 'Направление подготовки «Информационные системы и технологии» Уровень образования: бакалавриат Форма обучения: очная. Срок обучения: 4 года Проходной балл: 216 \n\nНаправление подготовки "Прикладная информатика"Уровень образования: бакалавриат Форма обучения: очная. Срок обучения: 4 года Проходной балл: 224')
        first(message)
    if float(message.text) >= 230:
        bot.send_message(message.chat.id, 'Направление подготовки «Информационные системы и технологии» Уровень образования: бакалавриат Форма обучения: очная. Срок обучения: 4 года Проходной балл: 216 \n\nНаправление подготовки "Прикладная информатика"Уровень образования: бакалавриат Форма обучения: очная. Срок обучения: 4 года Проходной балл: 224\n\n230: Направление подготовки "Информационная безопасность" Уровень образования: бакалавриат Форма обучения: очная. Срок обучения: 4 года Проходной балл: 230 ')
        first(message)
    if message.text == 'Меню':
        first(message)
def second(message):
    if message.text =='/openday':
        bot.send_message(message.chat.id,'Приглашаем всех желающих (абитуриентов, школьников и их родителей) на День открытых дверей МИИГАиК.\n Экскурсия по университету, презентации направлений подготовки, ответы на вопросы по процессу обучения в вузе - все будет представлено на дне открытых дверей в Москве.\nБлижайший День открытых дверей в МИИГАиК состоится 2021 года по адресу:\nМосква, Гороховский пер., 4. Проезд: ст. метро Курская, выход к Гоголь-центру. \nНачало в 10:00\n Актуальную и подробную информацию Вы можете узнать на сайте: \nhttp://www.miigaik.ru/\n и в группе Вконтакте\nhttps://vk.com/miigaik')
        first(message)
    elif message.text == '/course':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Архитектурно-художественная школа')
        keyboard.add('Подготовка к ЕГЭ')
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,'Что вам необходимо?', reply_markup=keyboard)
        bot.register_next_step_handler(send,CourseComand)
    elif message.text == '/specialties':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.row('Бакалавриат','Специалитет')
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,'Выберите уровень квалификации:', reply_markup=keyboard)
        bot.register_next_step_handler(send,SpecialtielsComand)
    elif message.text == '/guide':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Список документов')
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,'Чтобы поступить в МИИГАиК необходимо:\n\n Шаг 1: До 25.07 подать заявление в МИИГАиК одним из способов:\n1) В приемную коммисию, по адресу Москва, Гороховский пер., 4\n График работы: по будням с 8.00 до 22.00, по субботам с 8.00 до 18.00\n2) На почту pk@miigaik.ru\n\n Шаг 2: Следи за информацией на сайте:\n http://www.miigaik.ru/Abitur/competition/enrolled/\n\n Шаг 3: Принеси оригинал документов\n\nШаг 4: Вы студент МИИГАиК!', reply_markup=keyboard)
        bot.register_next_step_handler(send,GuideComand)
    elif message.text == '/contacts':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,'Контактная информация\n\nТелефон приемной комиссии:\n 8 (499) 267-15-45 (Москва)\nEmail: portal@miigaik.ru\n Режим работы: по будням с 8.00 до 22.00, по субботам с 8.00 до 18.00\n Проезд: ст. метро "Курская", выход к Гоголь-центру', reply_markup=keyboard)
        bot.register_next_step_handler(send,ContactsComand)
    elif message.text == '/studorganizations':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.row('Молодежный клуб РГО','Спортивные секции')
        keyboard.row('МИИГАиК МЕДИА','ПРОФКОМ СТУДЕНТОВ')
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,'Перейдя по кнопке интересующей вас секции, можно узнать о ней подробнее', reply_markup=keyboard)
        bot.register_next_step_handler(send,StudOrgComand)
    elif message.text == '/map':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,'Карта МИИГАиК\nhttp://map.miigaik.ru/', reply_markup=keyboard)
        bot.register_next_step_handler(send,MapComand)
    elif message.text == '/calculator':
        keyboard = types.ReplyKeyboardMarkup(True,False)
        keyboard.add('Меню')
        send = bot.send_message(message.chat.id,'В данном разделе можно узнать на какие направления подготовки на факультете геоинформатики и информационной безопасности вы проходите.Введите суммарное количестов баллов по математике, русскому языку и информатике/физике:', reply_markup=keyboard)
        bot.register_next_step_handler(send,CalcComand)
    else:
        error(message)
def error(message):
    keyboard = types.ReplyKeyboardMarkup(True,False)
    keyboard.row('/openday','/course')
    keyboard.row('/specialties','/guide')
    keyboard.row('/contacts','/studorganizations')
    keyboard.row('/map','/calculator')
    send = bot.send_message(message.chat.id, 'Выберите команду из предложенного списка',reply_markup=keyboard)
    bot.register_next_step_handler(send,second)
@bot.message_handler(commands=['/specialties'])
def spec(message):
    keyboard = types.ReplyKeyboardMarkup(True,False)
    keyboard.row('Бакалавриат','Специалитет')
    keyboard.add('Меню')
    send = bot.send_message(message.chat.id,'Выберите уровень квалификации:', reply_markup=keyboard)
    bot.register_next_step_handler(send,SpecialtielsComand)
bot.polling(none_stop=True)
