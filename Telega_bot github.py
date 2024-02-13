import telebot 
from datetime import datetime, time
from telebot import types

token = "your bot token"
bot = telebot.TeleBot(token)

# print(f'{message.from_user.first_name} написав: "{message.text}" о {now}')

lesson01 = time(8, 0)
lesson0 = time(8, 24)
lesson1 = time(9, 0)
lesson2 = time(9, 40)
lesson3 = time(10, 30)
lesson4 = time(11, 10)
lesson5 = time(12, 0)
lesson6 = time(12, 40)
lesson7 = time(13, 20)

@bot.message_handler(commands=['info'])
def get_user_text(message):
    print(f'{message.from_user.first_name} написав: "{message.text}" о {datetime.now().strftime("%H:%M")}')
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['start'])
def start(message):
    print(f'{message.from_user.first_name} написав: "{message.text}", "{message.from_user.username}" о {datetime.now().strftime("%H:%M")}')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("📚який урок?")

    markup.add(btn1)
    bot.send_message(message.chat.id, text='Привіт. Я - бот, який допоможе тобі дізнатись, який зараз урок. Натисни на кнопку ‘Який урок?’ або напишіть команду /help, щоб побачити всі команди цього бота.', reply_markup=markup)

@bot.message_handler(commands=['rozklad'])
def rozklad(message):
    print(f'{message.from_user.first_name} написав: "{message.text}", "{message.from_user.username}" о {datetime.now().strftime("%H:%M")}')
    bot.send_message(message.chat.id,'''    
1) Мистецтво
2) Фізика
3) Всесвітня історія
4) Біологія
5) Біологія
6) Зарубіжна література
7) Зарубіжна література
                     
1) Українська мова
2) Українська мова
3) Математика
4) Математика
5) Фізична культура
6) Географія
7) Інформатика
                    
1) Історія України/Географ
2) Історія України
3) Німецька мова
4) Німецька мова
5) Фізика
6) Фізика
7) Фізична культура
                    
1) Українська літерат
2) Українська літерат
3) Математика
4) Математика
5) Англійська мова
6) Англійська мова
7) Трудове навчання
                   
1) Основи здоров'я
2) Хімія
3) Хімія
4) Інформатика
5) Фізична культура
6) Основи правознавства
''')

@bot.message_handler(commands=['rk'])
def rk(message):

    print(f'{message.from_user.first_name} написав: "{message.text}", "{message.from_user.username}" о {datetime.now().strftime("%H:%M")}')

    now = datetime.now()
    day_now = now.weekday()

    l1 = "8:30-9:00"
    l2 = "9:10-9:40"
    l3 = "10:00-10:30"
    l4 = "10:40-11:10"
    l5 = "11:30-12:00"
    l6 = "12:10-12:40"
    l7 = "12:50-13:20"

    ximia     = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    fizra     = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    geometria = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    algebra   = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    biologia  = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    osnzd     = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    ykrlit    = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    zaryba    = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    vses_ist  = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    ist_ua    = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    geografia = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    nim_mova  = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    angl      = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    fizika    = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    myzlo     = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    ykr_mova  = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'
    pravo     = 'https://meet.google.com/aaa-aaaa-aaa?authuser=1'

    if day_now == 0:
        bot.send_message(message.chat.id,f'''   
1) <a href =\"{myzlo}\">Мистецтво</a> {l1}
2) <a href =\"{fizika}\">Фізика</a> {l2}
3) <a href =\"{vses_ist}\">Всесвітня історія</a> {l3}
4) <a href =\"{biologia}\">Біологія</a> {l4}
5) <a href =\"{biologia}\">Біологія</a> {l5}
6) <a href =\"{zaryba}\">Зарубіжна література</a> {l6}
7) <a href =\"{zaryba}\">Зарубіжна література</a> {l7}''', parse_mode='HTML')
    elif day_now == 1:
        bot.send_message(message.chat.id,f'''              
1) <a href =\"{ykr_mova}\">Українська мова</a> {l1}
2) <a href =\"{ykr_mova}\">Українська мова</a> {l2}
3) <a href =\"{algebra}\">Алгебра</a> {l3}
4) <a href =\"{algebra}\">Алгебра</a> {l4}
5) <a href =\"{fizra}\">Фізична культура</a> {l5}
6) <a href =\"{geografia}\">Географія</a> {l6}
7) Інформатика {l7}''', parse_mode='HTML')
        
    elif day_now == 2:
        bot.send_message(message.chat.id,f"""
1) <a href =\"{ist_ua}\">Історія України</a> / <a href =\"{geografia}\">Географія</a> {l1}
2) <a href =\"{ist_ua}\">Історія України</a> {l2}
3) <a href =\"{nim_mova}\">Німецька мова</a> {l3}
4) <a href =\"{nim_mova}\">Німецька мова</a> {l4}
5) <a href=\"{fizika}\">Фізика</a> {l5}
6) <a href=\"{fizika}\">Фізика</a> {l6}
7) <a href =\"{fizra}\">Фізична культура</a> {l7}""", parse_mode='HTML')

    elif day_now == 3:
        bot.send_message(message.chat.id,f'''                  
1) <a href =\"{ykrlit}\">Українська літерат</a> {l1}
2) <a href =\"{ykrlit}\">Українська літерат</a> {l2}
3) <a href =\"{geometria}\">Геометрія</a> {l3}
4) <a href =\"{geometria}\">Геометрія</a> {l4}
5) <a href =\"{angl}\">Англійська мова</a> {l5}
6) <a href =\"{angl}\">Англійська мова</a> {l6}
7) Трудове навчання {l7}''', parse_mode='HTML')

    elif day_now == 4:
        bot.send_message(message.chat.id,f'''     
1) <a href =\"{osnzd}\">Основи здоров'я</a> {l1}
2) <a href =\"{ximia}\">Хімія'я</a> {l2}
3) <a href =\"{ximia}\">Хімія'я</a> {l3}
4) Інформатика {l4}
5) <a href =\"{fizra}\">Фізична культура</a> {l5}
6) <a href =\"{pravo}\">Основи правознавства</a> {l6}''', parse_mode='HTML')


# ДОМАШНЕ ЗАВДАНЯ
@bot.message_handler(commands=['domahka'])
def dz (message):

    print(f'{message.from_user.first_name} написав: "{message.text}", "{message.from_user.username}" о {datetime.now().strftime("%H:%M")}')

    patnisa = types.InlineKeyboardMarkup(row_width=2)
    ponedilok = types.InlineKeyboardMarkup(row_width=2)
    vivtorok = types.InlineKeyboardMarkup(row_width=2)
    sereda = types.InlineKeyboardMarkup(row_width=2)
    chetver = types.InlineKeyboardMarkup(row_width=2)

    # Посилання на книги
    algebra_book =      types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1FnTZNXMSmxjwj7KK7ebRkSsw01Llo25x/view?usp=drive_link')
    angl_book =         types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1k_pSGftny033pxxY-6RAIooIlOHKeFhM/view?usp=drive_link')
    biologia_book =     types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1p_oq7Tf4vzhpCs_pVDaok7yW5TojBneR/view?usp=drive_link')
    vses_ist_book =     types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1IE8TMiGA7nfH7ZhZbPoHwJ1R96wDWKWf/view?usp=drive_link')
    geografia_book =    types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1q2intaWYXCOBIYgaHQMQcQX3xdOjZHxf/view?usp=drive_link')
    geometria_book =    types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1RpHire51uKnAyq-iuxPZaAzqWN_0QnC8/view?usp=drive_link')
    zaryba_book =       types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1ET-rwrdledyRk09evyCP6L40U5jXUADg/view?usp=drive_link')
    informatika_book =  types.InlineKeyboardButton('Книга', url='https://drive.google.com/drive/folders/1dFPP6_Up5yz__DQp2jdZ6oB8OS5ng8_8?usp=sharing')
    ist_ua_book =       types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1V8pGRO5sl37eQdIzRC-NKvVtl7KqdxHR/view?usp=drive_link')
    myzlo_book =        types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1N61BAYl61NdiEODur4LbmKbo549aNJod/view?usp=drive_link')
    nim_mova_book =     types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1I2gx3wqQLOHP_QmTaHINWrNDpuZCzeNz/view?usp=drive_link')
    osnzd_book =        types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1pM58Ak0TCes3z9cRIU2WHuO4tFnC_Yev/view?usp=drive_link')
    pravo_book =        types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1yZMQt8So_Rtvpk7SMAwAUaTbbziNrCcs/view?usp=drive_link')
    trydove_book =      types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1gPt2QQhukGhQmRQ9_9BwEMChDbfz0cOZ/view?usp=drive_link')
    ykr_lit_book =      types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1dIZUULntz-tOsOe7AwMq_N4H1S3ZI_uB/view?usp=drive_link')
    ykr_mova_book =     types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1a842pw5PVGAycqmSIFQGOitm1kXfpFH7/view?usp=drive_link')
    fizra_book =        types.InlineKeyboardButton('Немає', url='https://drive.google.com/drive/folders/1si0b1nROYKhQKp5Ime-WVnylc1xQXYiB?usp=drive_link')
    fizika_book =       types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1pLiiAbBJIudJhRK3ae1Xyl06h5nqwdiI/view?usp=drive_link')
    ximia_book =        types.InlineKeyboardButton('Книга', url='https://drive.google.com/file/d/1gTwU7K3uM0lADqyVicuq81bjEPQeoFzW/view?usp=drive_link')

    # Посилання на домашнє завдання 
    informatika_dz =    types.InlineKeyboardButton('Інформатика', url='https://classroom.google.com/u/1/w/NjIwMTk0ODU1ODYz/t/all')
    ximia_dz =          types.InlineKeyboardButton('Хімія', url='https://classroom.google.com/u/1/w/NjIwMzkwNTY4NDYy/t/all')
    fizra_dz =          types.InlineKeyboardButton('Фізична культура', url='https://classroom.google.com/u/1/w/NTQ1MzMyNTM5MDcz/t/all')
    geometria_dz =      types.InlineKeyboardButton('Геометрія', url='https://classroom.google.com/')
    algebra_dz =        types.InlineKeyboardButton('Алгебра', url='https://classroom.google.com/u/1/w/NjIwNDAzMjQyODMy/t/all')
    biologia_dz =       types.InlineKeyboardButton('Біологія', url='https://classroom.google.com/u/1/w/NjE5NjkwNjkyNDky/t/all')
    osnzd_dz =          types.InlineKeyboardButton('Основи здоровя', url='https://classroom.google.com/u/1/w/NjMzNDMyODY4MjE0/t/all')
    zaryba_dz =         types.InlineKeyboardButton('Зарубіжна література', url='https://classroom.google.com/u/1/w/NjIwMDQyOTM4NjM1/t/all')
    vses_ist_dz =       types.InlineKeyboardButton('Всесвітня історія', url='https://classroom.google.com/u/1/w/NjE5MTQwNTA0MjE4/t/all')
    ist_ua_dz =         types.InlineKeyboardButton('Історія України', url='https://classroom.google.com/u/1/w/NjE5MTQxNjQ3MTc1/t/all')
    geografia_dz =      types.InlineKeyboardButton('Географія', url='https://classroom.google.com/u/1/w/NjE5MTUyNzIyMzE5/t/all')
    nim_mova_dz =       types.InlineKeyboardButton('Німецька мова', url='https://classroom.google.com/u/1/w/NjIwMjk0MzU4MDU5/t/all')
    angl_dz =           types.InlineKeyboardButton('Англійська мова', url='https://classroom.google.com/u/1/w/NjIwNzk4MTM1NjM4/t/all')
    fizika_dz =         types.InlineKeyboardButton('Фізика', url='https://classroom.google.com/u/1/w/NjIwMDE3MDgyMDQz/t/all')
    myzlo_dz =          types.InlineKeyboardButton('Музичне мистецтво', url='https://classroom.google.com/u/1/w/NjIwODUxNzc4MzQ1/t/all')
    ykr_lit_dz =        types.InlineKeyboardButton('Українська література', url='https://classroom.google.com/u/1/w/NjE5MTQ2NDcxMzUz/t/all')
    ykr_mova_dz =       types.InlineKeyboardButton('Українська мова', url='https://classroom.google.com/u/1/w/NjE5MTM4MTM0Njgz/t/all')
    trydove_dz =        types.InlineKeyboardButton('Трудове', url='https://classroom.google.com/u/1/w/NjE3OTcwMzUzMjkx/t/all')
    pravo_dz =          types.InlineKeyboardButton('Правознавство', url='https://classroom.google.com/u/1/w/NjE5MTQyMzYxOTc2/t/all')

    patnisa.add(osnzd_dz, osnzd_book, ximia_dz, ximia_book, informatika_dz, informatika_book, fizra_dz, fizra_book, pravo_dz, pravo_book)
    ponedilok.add(myzlo_dz, myzlo_book, fizika_dz, fizika_book, vses_ist_dz, vses_ist_book, biologia_dz, biologia_book, zaryba_dz, zaryba_book)
    vivtorok.add(ykr_mova_dz, ykr_mova_book, algebra_dz, algebra_book, fizra_dz, fizra_book, geografia_dz, geografia_book, informatika_dz, informatika_book)
    sereda.add(ist_ua_dz, ist_ua_book, geografia_dz, geografia_book, nim_mova_dz, nim_mova_book, fizika_dz, fizika_book, fizra_dz, fizika_book)
    chetver.add(ykr_lit_dz, ykr_lit_book, geometria_dz, geometria_book, angl_dz, angl_book, trydove_dz, trydove_book)

    now = datetime.now()
    day_now = now.weekday()

    if day_now in (4,5,6):
        bot.send_message(message.chat.id, 'Домашнє завдання на понеділок', reply_markup=ponedilok)
    elif day_now == 0:
        bot.send_message(message.chat.id, 'Домашнє завдання на вівторок', reply_markup=vivtorok)    
    elif day_now == 1:
        bot.send_message(message.chat.id, 'Домашнє завдання на середу', reply_markup=sereda) 
    elif day_now == 2:
        bot.send_message(message.chat.id, 'Домашнє завдання на четвер', reply_markup=chetver)
    elif day_now == 3:
        bot.send_message(message.chat.id, 'Домашнє завдання на п\'ятницю', reply_markup=patnisa)


@bot.message_handler(commands=['all_books'])
def all_books(message):
    print(f'{message.from_user.first_name} написав: "{message.text}", "{message.from_user.username}" о {datetime.now().strftime("%H:%M")}')
    bot.send_message(message.chat.id, f"<a href=\"https://drive.google.com/drive/folders/1si0b1nROYKhQKp5Ime-WVnylc1xQXYiB?usp=drive_link\">👉Всі книги👈</a>", parse_mode="HTML")


@bot.message_handler(regexp=r"який урок")
def func(message):

    print(f'{message.from_user.first_name} написав: "{message.text}", "{message.from_user.username}" о {datetime.now().strftime("%H:%M")}')

    now = datetime.now()
    day_now = now.weekday()
    time_now = now.time()

    osnzd = types.InlineKeyboardMarkup()
    ximia = types.InlineKeyboardMarkup()
    fizra = types.InlineKeyboardMarkup()
    geometria = types.InlineKeyboardMarkup()
    algebra = types.InlineKeyboardMarkup()
    biologia = types.InlineKeyboardMarkup()
    ykrlit = types.InlineKeyboardMarkup()
    zaryba = types.InlineKeyboardMarkup()
    vses_ist = types.InlineKeyboardMarkup()
    ist_ua = types.InlineKeyboardMarkup()
    geografia = types.InlineKeyboardMarkup()
    nim_mova = types.InlineKeyboardMarkup()
    angl = types.InlineKeyboardMarkup()
    fizika = types.InlineKeyboardMarkup()
    myzlo = types.InlineKeyboardMarkup()
    ykr_mova = types.InlineKeyboardMarkup()
    pravo = types.InlineKeyboardMarkup()

    trydove = types.InlineKeyboardMarkup()

    informatika = types.InlineKeyboardMarkup(row_width=2)

    match = types.InlineKeyboardMarkup(row_width=2)

    cereda = types.InlineKeyboardMarkup(row_width=2)

    # Посилання на google meet або щось інше
    ximia.add(types.InlineKeyboardButton('Урок',     url='https://meet.google.com/fxh-qhcn-vkv?authuser=1'))
    fizra.add(types.InlineKeyboardButton('Урок',     url='https://meet.google.com/trm-bykt-kqd?authuser=1'))
    geometria.add(types.InlineKeyboardButton('Урок', url='https://meet.google.com/umh-cihs-czh?authuser=1'))
    algebra.add(types.InlineKeyboardButton('Урок',   url='https://meet.google.com/xbx-fyzh-vxj?authuser=1'))
    biologia.add(types.InlineKeyboardButton('Урок',  url='https://meet.google.com/aym-zvnh-its?authuser=1'))
    osnzd.add(types.InlineKeyboardButton('Урок',     url='https://meet.google.com/ums-zrja-xag?authuser=1'))
    ykrlit.add(types.InlineKeyboardButton('Урок',    url='https://meet.google.com/sbh-fkxx-mjo?authuser=1'))
    zaryba.add(types.InlineKeyboardButton('Урок',    url='https://meet.google.com/ybx-zzjd-wmg?authuser=1'))
    vses_ist.add(types.InlineKeyboardButton('Урок',  url='https://meet.google.com/zhs-mdvc-obq?authuser=1'))
    ist_ua.add(types.InlineKeyboardButton('Урок',    url='https://meet.google.com/fgd-kqkc-xpr?authuser=1'))
    geografia.add(types.InlineKeyboardButton('Урок', url='https://meet.google.com/sbg-chnp-eku?authuser=1'))
    nim_mova.add(types.InlineKeyboardButton('Урок',  url='https://meet.google.com/ojy-mbxu-efo?authuser=1'))
    angl.add(types.InlineKeyboardButton('Урок',      url='https://meet.google.com/ocd-sfmu-bqw?authuser=1'))
    fizika.add(types.InlineKeyboardButton('Урок',    url='https://meet.google.com/dhb-xxhe-xdf?authuser=1'))
    myzlo.add(types.InlineKeyboardButton('Урок',     url='https://meet.google.com/cvg-mshj-kdn?authuser=1'))
    ykr_mova.add(types.InlineKeyboardButton('Урок',  url='https://meet.google.com/eoy-iojm-vea?authuser=1'))
    pravo.add(types.InlineKeyboardButton('Урок',     url='https://meet.google.com/ugg-kgmv-tzu?authuser=1'))

    trydove_xlopci = (types.InlineKeyboardButton('Трудове хлопців', url='https://meet.google.com/xti-nogy-qqp?authuser=1&hs=179'))
    trydove_divchata = (types.InlineKeyboardButton('Трудове дівчат', url='https://meet.google.com/tfa-resw-frd'))
    trydove.add(trydove_xlopci, trydove_divchata)

    informatika1 = types.InlineKeyboardButton('1 Група', url='https://meet.google.com/kax-afva-vjy?authuser=1&hs=179')
    informatika2 = types.InlineKeyboardButton('2 Група', url='https://meet.google.com/rwo-fnow-iwt?authuser=1')
    informatika.add(informatika1, informatika2)

    geometria1 = types.InlineKeyboardButton('Геометрія', url='https://meet.google.com/umh-cihs-czh?authuser=1&hs=179')
    algebra1 = types.InlineKeyboardButton('Алгебра', url='https://meet.google.com/xbx-fyzh-vxj?authuser=1&hs=179')
    match.add(algebra1, geometria1)

    ist_ua1 = types.InlineKeyboardButton('Історія України', url='https://meet.google.com/fgd-kqkc-xpr?authuser=1&hs=179')
    geografia1 = types.InlineKeyboardButton('Географія', url='https://meet.google.com/sbg-chnp-eku?authuser=1&hs=179')
    cereda.add(ist_ua1, geografia1)
   
   

    # yrok_dz = [посилання на classroom цього урока, назва урока, посилання на книгу]
    inf_books =      ['https://drive.google.com/file/d/1jrsW9nHN2lL7CYKJ-inNU2PwkX22Hvff/view?usp=drive_link', 'https://drive.google.com/file/d/10Ss8jfXnmRoIB_bAw6CjSg_FXFZDbcGl/view?usp=sharing']
    informatika_dz = ['https://classroom.google.com', 'Інформатика', '1 група',
                      'https://classroom.google.com', '2 група']
    ximia_dz =       ['https://classroom.google.com/u/1/w/NjIwMzkwNTY4NDYy/t/all?hl=ua', 'Хімія', 'https://drive.google.com/file/d/1gTwU7K3uM0lADqyVicuq81bjEPQeoFzW/view?usp=sharing']
    fizra_dz =       ['https://classroom.google.com/u/1/w/NTQ1MzMyNTM5MDcz/t/all?hl=ua', 'Фізична культура']
    geometria_dz =   ['https://classroom.google.com/u/1/w/NjIwNDAxNjM1Mzgy/t/all?hl=ua', 'Геометрія', 'https://drive.google.com/file/d/1RpHire51uKnAyq-iuxPZaAzqWN_0QnC8/view?usp=sharing'] 
    algebra_dz =     ['https://classroom.google.com/u/1/w/NjIwNDAzMjQyODMy/t/all?hl=ua', 'Алгебра', 'https://drive.google.com/file/d/1FnTZNXMSmxjwj7KK7ebRkSsw01Llo25x/view?usp=drive_link']
    biologia_dz =    ['https://classroom.google.com/u/1/w/NjE5NjkwNjkyNDky/t/all?hl=ua', 'Біологія', 'https://drive.google.com/file/d/1p_oq7Tf4vzhpCs_pVDaok7yW5TojBneR/view?usp=drive_link']
    osnzd_dz =       ['https://classroom.google.com/u/1/w/NjMzNDMyODY4MjE0/t/all?hl=ua', "Основи здоров'я", 'https://drive.google.com/file/d/1pM58Ak0TCes3z9cRIU2WHuO4tFnC_Yev/view?usp=drive_link']
    zaryba_dz =      ['https://classroom.google.com/u/1/w/NjIwMDQyOTM4NjM1/t/all?hl=ua', 'Зарубіжна література', 'https://drive.google.com/file/d/1ET-rwrdledyRk09evyCP6L40U5jXUADg/view?usp=drive_link']
    vses_ist_dz =    ['https://classroom.google.com/u/1/w/NjE5MTQwNTA0MjE4/t/all?hl=ua', 'Всесвітня історія', 'https://drive.google.com/file/d/1IE8TMiGA7nfH7ZhZbPoHwJ1R96wDWKWf/view?usp=drive_link']
    ist_ua_dz =      ['https://classroom.google.com/u/1/w/NjE5MTQxNjQ3MTc1/t/all?hl=ua', 'Історія України', 'https://drive.google.com/file/d/1V8pGRO5sl37eQdIzRC-NKvVtl7KqdxHR/view?usp=drive_link']
    geografia_dz =   ['https://classroom.google.com/u/1/w/NjE5MTUyNzIyMzE5/t/all?hl=ua', 'Географія', 'https://drive.google.com/file/d/1q2intaWYXCOBIYgaHQMQcQX3xdOjZHxf/view?usp=drive_link']
    nim_mova_dz =    ['https://classroom.google.com/u/1/w/NjIwMjk0MzU4MDU5/t/all?hl=ua', 'Німеціка мова', 'https://drive.google.com/file/d/1I2gx3wqQLOHP_QmTaHINWrNDpuZCzeNz/view?usp=drive_link']
    angl_dz =        ['https://classroom.google.com/u/1/w/NjIwNzk4MTM1NjM4/t/all?hl=ua', 'Англійська мова', 'https://drive.google.com/file/d/1k_pSGftny033pxxY-6RAIooIlOHKeFhM/view?usp=drive_link']
    fizika_dz =      ['https://classroom.google.com/u/1/w/NjIwMDE3MDgyMDQz/t/all?hl=ua', 'Фізика', 'https://drive.google.com/file/d/1pLiiAbBJIudJhRK3ae1Xyl06h5nqwdiI/view?usp=drive_link']
    myzlo_dz =       ['https://classroom.google.com/u/1/w/NjIwODUxNzc4MzQ1/t/all?hl=ua', 'Музичне местецтво', 'https://drive.google.com/file/d/1N61BAYl61NdiEODur4LbmKbo549aNJod/view?usp=sharing']
    ykr_lit_dz =     ['https://classroom.google.com/u/1/w/NjE5MTQ2NDcxMzUz/t/all?hl=ua', 'Українська літератутра', 'https://drive.google.com/file/d/1dIZUULntz-tOsOe7AwMq_N4H1S3ZI_uB/view?usp=drive_link']
    ykr_mova_dz =    ['https://classroom.google.com/u/1/w/NjE5MTM4MTM0Njgz/t/all?hl=ua', 'Українська мова', 'https://drive.google.com/file/d/1a842pw5PVGAycqmSIFQGOitm1kXfpFH7/view?usp=drive_link']
    trydove_dz =     ['https://classroom.google.com/u/1/w/NjE3OTcwMzUzMjkx/t/all?hl=ua', 'Трудове навчання', 'https://drive.google.com/file/d/1gPt2QQhukGhQmRQ9_9BwEMChDbfz0cOZ/view?usp=drive_link']
    pravo_dz =       ['https://classroom.google.com/u/1/w/NjE5MTQyMzYxOTc2/t/all?hl=ua', 'Правознавство', 'https://drive.google.com/file/d/1yZMQt8So_Rtvpk7SMAwAUaTbbziNrCcs/view?usp=drive_link']
    
    
    l1 = "8:30-9:00"
    l2 = "9:10-9:40"
    l3 = "10:00-10:30"
    l4 = "10:40-11:10"
    l5 = "11:30-12:00"
    l6 = "12:10-12:40"
    l7 = "12:50-13:20"
        
    if lesson01 <= time_now < lesson0:
        bot.send_message(message.chat.id, f"<a href=\"{ist_ua_dz[0]}\">{ist_ua_dz[1]}</a> 8:20-8:25", reply_markup = ist_ua, parse_mode="HTML")

    # <a href={[0]}>{[1]}</a>
   # Понеділок
    elif day_now == 0:
        if lesson0 <= time_now < lesson1:
            bot.send_message(message.chat.id, f"1) <a href=\"{myzlo_dz[0]}\">{myzlo_dz[1]}</a> {l1} <a href=\"{myzlo_dz[2]}\">Книга</a>", reply_markup = myzlo, parse_mode="HTML")
        elif lesson1 <= time_now < lesson2:
            bot.send_message(message.chat.id, f"2) <a href=\"{fizika_dz[0]}\">{fizika_dz[1]}</a> {l2} <a href=\"{fizika_dz[2]}\">Книга</a>", reply_markup = fizika, parse_mode="HTML")
        elif lesson2 <= time_now < lesson3:
            bot.send_message(message.chat.id, f"3) <a href=\"{vses_ist_dz[0]}\">{vses_ist_dz[1]}</a> {l3} <a href=\"{vses_ist_dz[2]}\">Книга</a>", reply_markup = vses_ist, parse_mode="HTML")
        elif lesson3 <= time_now < lesson4:
            bot.send_message(message.chat.id, f"4) <a href=\"{biologia_dz[0]}\">{biologia_dz[1]}</a> {l4} <a href=\"{biologia_dz[2]}\">Книга</a>", reply_markup=biologia, parse_mode="HTML")
        elif lesson4 <= time_now < lesson5:
            bot.send_message(message.chat.id, f"5) <a href=\"{biologia_dz[0]}\">{biologia_dz[1]}</a> {l5} <a href=\"{biologia_dz[2]}\">Книга</a>", reply_markup = biologia, parse_mode="HTML")
        elif lesson5 <= time_now < lesson6:
            bot.send_message(message.chat.id, f"6) <a href=\"{zaryba_dz[0]}\">{zaryba_dz[1]}</a> {l6} <a href=\"{zaryba_dz[2]}\">Книга</a>", reply_markup = zaryba, parse_mode="HTML")
        elif lesson6 <= time_now < lesson7:
            bot.send_message(message.chat.id, f"7) <a href=\"{zaryba_dz[0]}\">{zaryba_dz[1]}</a> {l7} <a href=\"{zaryba_dz[2]}\">Книга</a>", reply_markup = zaryba, parse_mode="HTML")
        else:
            bot.send_message(message.chat.id, 'Уроки закінчились.')
# Вівторок
    elif day_now == 1:
        if lesson0 <= time_now < lesson1:
            bot.send_message(message.chat.id, f"1) <a href=\"{ykr_mova_dz[0]}\">{ykr_mova_dz[1]}</a> {l1} <a href=\"{ykr_mova_dz[2]}\">Книга</a>", reply_markup = ykr_mova, parse_mode="HTML")
        elif lesson1 <= time_now < lesson2:
            bot.send_message(message.chat.id, f"2) <a href=\"{ykr_mova_dz[0]}\">{ykr_mova_dz[1]}</a> {l2} <a href=\"{ykr_mova_dz[2]}\">Книга</a>", reply_markup = ykr_mova, parse_mode="HTML")
        elif lesson2 <= time_now < lesson3:
            bot.send_message(message.chat.id, f"3) <a href=\"{algebra_dz[0]}\">{algebra_dz[1]}</a> {l3} <a href=\"{algebra_dz[2]}\">Книга</a>", reply_markup = algebra, parse_mode="HTML")
        elif lesson3 <= time_now < lesson4:
            bot.send_message(message.chat.id, f"4) <a href=\"{algebra_dz[0]}\">{algebra_dz[1]}</a> {l4} <a href=\"{algebra_dz[2]}\">Книга</a>", reply_markup = algebra, parse_mode="HTML")
        elif lesson4 <= time_now < lesson5:
            bot.send_message(message.chat.id, f"5) <a href=\"{fizra_dz[0]}\">{fizra_dz[1]}</a> {l5}", reply_markup=fizra, parse_mode="HTML")
        elif lesson5 <= time_now < lesson6:
            bot.send_message(message.chat.id, f"6) <a href=\"{geografia_dz[0]}\">{geografia_dz[1]}</a> {l6} <a href=\"{geografia_dz[2]}\">Книга</a>", reply_markup = geografia, parse_mode="HTML")
        elif lesson6 <= time_now < lesson7:
            bot.send_message(message.chat.id, f"7) {informatika_dz[1]} <a href=\"{informatika_dz[0]}\">{informatika_dz[2]}</a> / <a href=\"{informatika_dz[3]}\">{informatika_dz[4]}</a> {l7} \n <a href=\"{inf_books[0]}\">Книга 1 гр.</a> / <a href=\"{inf_books[1]}\">Книга 2 гр.</a>", reply_markup = informatika, parse_mode="HTML")       
        else:
            bot.send_message(message.chat.id, 'Уроки закінчились.')
# Середа

    elif day_now == 2:
        if lesson0 <= time_now < lesson1:
            bot.send_message(message.chat.id, f"1) <a href=\"{ist_ua_dz[0]}\">{ist_ua_dz[1]}</a> / <a href=\"{geografia_dz[0]}\">{geografia_dz[1]}</a> {l1} \n <a href=\"{ist_ua_dz[2]}\">Книга історії</a> / <a href=\"{geografia_dz[2]}\">Книга географії</a>", reply_markup = cereda, parse_mode="HTML")
        elif lesson1 <= time_now < lesson2:
            bot.send_message(message.chat.id, f"2) <a href=\"{ist_ua_dz[0]}\">{ist_ua_dz[1]}</a> {l2} <a href=\"{ist_ua_dz[2]}\">Книга</a>", reply_markup = ist_ua, parse_mode="HTML")
        elif lesson2 <= time_now < lesson3:
            bot.send_message(message.chat.id, f"3) <a href=\"{nim_mova_dz[0]}\">{nim_mova_dz[1]}</a> {l3} <a href=\"{nim_mova_dz[2]}\">Книга</a>", reply_markup=nim_mova, parse_mode="HTML")
        elif lesson3 <= time_now < lesson4:
            bot.send_message(message.chat.id, f"4) <a href=\"{nim_mova_dz[0]}\">{nim_mova_dz[1]}</a> {l4} <a href=\"{nim_mova_dz[2]}\">Книга</a>", reply_markup = nim_mova, parse_mode="HTML")
        elif lesson4 <= time_now < lesson5:
            bot.send_message(message.chat.id, f"5) <a href=\"{fizika_dz[0]}\">{fizika_dz[1]}</a> {l5} <a href=\"{fizika_dz[2]}\">Книга</a>", reply_markup=fizika, parse_mode="HTML")
        elif lesson5 <= time_now < lesson6:
            bot.send_message(message.chat.id, f"6) <a href=\"{fizika_dz[0]}\">{fizika_dz[1]}</a> {l6} <a href=\"{fizika_dz[2]}\">Книга</a>", reply_markup = fizika, parse_mode="HTML")
        elif lesson6 <= time_now < lesson7:
            bot.send_message(message.chat.id, f"7) <a href=\"{fizra_dz[0]}\">{fizra_dz[1]}</a> {l7}", reply_markup = fizra, parse_mode="HTML")
        else:
            bot.send_message(message.chat.id, 'Уроки закінчились.')
# Четвер
    elif day_now == 3:
        if lesson0 <= time_now < lesson1:
            bot.send_message(message.chat.id, f"1) <a href=\"{ykr_lit_dz[0]}\">{ykr_lit_dz[1]}</a> {l1} <a href=\"{ykr_lit_dz[2]}\">Книга</a>", reply_markup = ykrlit, parse_mode="HTML")
        elif lesson1 <= time_now < lesson2:
            bot.send_message(message.chat.id, f"2) <a href=\"{ykr_lit_dz[0]}\">{ykr_lit_dz[1]}</a> {l2} <a href=\"{ykr_lit_dz[2]}\">Книга</a>", reply_markup = ykrlit, parse_mode="HTML")
        elif lesson2 <= time_now < lesson3:
            bot.send_message(message.chat.id, f"3) <a href=\"{geometria_dz[0]}\">{geometria_dz[1]}</a> {l3} <a href=\"{geometria_dz[2]}\">Книга</a>", reply_markup=geometria, parse_mode="HTML")
        elif lesson3 <= time_now < lesson4:
            bot.send_message(message.chat.id, f"4) <a href=\"{geometria_dz[0]}\">{geometria_dz[1]}</a> {l4} <a href=\"{geometria_dz[2]}\">Книга</a>", reply_markup = geometria, parse_mode="HTML")
        elif lesson4 <= time_now < lesson5:
            bot.send_message(message.chat.id, f"5) <a href=\"{angl_dz[0]}\">{angl_dz[1]}</a> {l5} <a href=\"{angl_dz[2]}\">Книга</a>", reply_markup= angl, parse_mode="HTML")
        elif lesson5 <= time_now < lesson6:
            bot.send_message(message.chat.id, f"6) <a href=\"{angl_dz[0]}\">{angl_dz[1]}</a> {l6} <a href=\"{angl_dz[2]}\">Книга</a>", reply_markup = angl, parse_mode="HTML")
        elif lesson6 <= time_now < lesson7:
            bot.send_message(message.chat.id, f"7) Трудове {l7}", reply_markup = trydove, parse_mode="HTML")
        else:
            bot.send_message(message.chat.id, 'Уроки закінчились.')
# П'ятниця
    elif day_now == 4:
        if lesson0 <= time_now < lesson1:
            bot.send_message(message.chat.id, f"1) <a href=\"{osnzd_dz[0]}\">{osnzd_dz[1]}</a> {l1} <a href=\"{osnzd_dz[2]}\">Книга</a>", reply_markup = osnzd, parse_mode="HTML")
        elif lesson1 <= time_now < lesson2:
            bot.send_message(message.chat.id, f"2) <a href=\"{ximia_dz[0]}\">{ximia_dz[1]}</a> {l2} <a href=\"{ximia_dz[2]}\">Книга</a>", reply_markup = ximia, parse_mode="HTML")
        elif lesson2 <= time_now < lesson3:
            bot.send_message(message.chat.id, f"3) <a href=\"{ximia_dz[0]}\">{ximia_dz[1]}</a> {l3} <a href=\"{ximia_dz[2]}\">Книга</a>", reply_markup = ximia, parse_mode="HTML")
        elif lesson3 <= time_now < lesson4:
            bot.send_message(message.chat.id, f"4) {informatika_dz[1]} <a href=\"{informatika_dz[0]}\">{informatika_dz[2]}</a> / <a href=\"{informatika_dz[3]}\">{informatika_dz[4]}</a> {l4} \n <a href=\"{inf_books[0]}\">Книга 1 гр.</a> / <a href=\"{inf_books[1]}\">Книга 2 гр.</a>", reply_markup = informatika, parse_mode="HTML")       
        elif lesson4 <= time_now < lesson5:
            bot.send_message(message.chat.id, f"5) <a href=\"{fizra_dz[0]}\">{fizra_dz[1]}</a> {l5}", reply_markup= fizra, parse_mode="HTML")
        elif lesson5 <= time_now < lesson6:
            bot.send_message(message.chat.id, f"6) <a href=\"{pravo_dz[0]}\">{pravo_dz[1]}</a> {l6} <a href=\"{pravo_dz[2]}\">Книга</a>", reply_markup = pravo, parse_mode="HTML")
        else:
            bot.send_message(message.chat.id, 'Уроки закінчились.')
    else:
        bot.send_message(message.chat.id, 'Вихідний')


@bot.message_handler(func=lambda message: True)
def set_reminder_time(message):
    print(f'{message.from_user.first_name} написав: "{message.text}", "{message.from_user.username}" о {datetime.now().strftime("%H:%M")}')
    

bot.infinity_polling()




