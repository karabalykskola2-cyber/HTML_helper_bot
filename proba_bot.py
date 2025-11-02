import telebot
import os
# Вставь сюда свой токен
TOKEN=os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 
        "Привет! Я помощник по работе с HTML.\n"
        "Напиши, что нужно сделать, например: изменить цвет текста."
    )

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    words = text.split()

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


