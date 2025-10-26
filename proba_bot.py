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
