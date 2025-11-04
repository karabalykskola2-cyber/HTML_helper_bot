import telebot
import os #модуль для работы с ОС, для работы с переменными окружения 
#это один из самых безопасных
#способов хранить секретные данные(токены)

# Вставь сюда свой токен
#TOKEN = "123456789:ABCdefGhIJKlmNoPQRstuVWxyZ"
TOKEN=os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)#связь с серверами телеграм

@bot.message_handler(commands=['start'])#указывает что делать после старта
def start(message):
    bot.send_message(message.chat.id, 
        "Привет! Я помощник по работе с HTML.\n"
        "Напиши, что нужно сделать, например: изменить цвет текста."
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    words = text.split()
# проверка по условию соответствующего тега
    if "цвет" in words or "color" in words:
        bot.send_message(message.chat.id, 
            "Используй тег <color>. Например:\n<color>Красный мак</color>"
        )
    elif "заголовок" in words:
        bot.send_message(message.chat.id, 
            "Используй тег <title>. Например:\n<title>Yandex</title>"
        )
    elif "жирный" in words:
        bot.send_message(message.chat.id, 
            "Используй тег <в> чтобы выделить текст жирным начертанием. Например:\n<в>Кино</в>"
        )
    elif "курсив" in words:
        bot.send_message(message.chat.id, 
            "Используй тег <i> чтобы выделить текст курсивом. Например:\n <i>Курсив</i>"
        )
    elif "подчеркивание" in words:
        bot.send_message(message.chat.id, 
            "Используй тег <u> чтобы выделить текст курсивом. Например:\n <u>Подчеркнутый текст</u>"
        )
    elif "таблица" in words:
        bot.send_message(message.chat.id, 
            "Используй тег <table> чтобы выделить текст курсивом. Например:\n <table><tr><td></td>Строка и два столбца<td>Строка и два столбца</td> </tr></table>"
        )


        
    elif "шрифт" in words or "font" in words:
        bot.send_message(message.chat.id, 
            "Используй тег <font>. Например:\n<font>Пример текста</font>"
        )
    else:
        bot.send_message(message.chat.id, 
            "Не понял, какой тег тебе нужен. Попробуй уточнить задание."
        )

# Запуск бота
bot.polling(none_stop=True)

#<html> этот тег сообщает браузерам и поисковым системам, что это страница HTML
#<title> определяет заголовок страницы, который отображается в верхней части браузера
#<body> между этими тегами отображается всё содержимое страницы
#<center> с помощью этих тегов текст выравнивается по центру
#<b> текст написанный между этими тегами, выделяется жирным начертанием
#<i> меняет шрифт на курсив
#<u> подчеркивает текст
#<s> перечеркивает текст
#<h1>...<h6> теги заголовков
#<br> перемещает текст на следующую строку
#<img>  тег который показывает изображение
#<a> тег для создания ссылок
#<table> тег создания таблицы
#<tr> создает новую строку
#<td>  создает новый столбец

# Запуск бота
bot.polling(none_stop=True)



