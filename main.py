import telebot
from telebot import types

token = '6854567724:AAGYsCVqhkKm5oAbDz9DbAxgTeGgy-xHJvo'

bot = telebot.TeleBot(token)

user_scores = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_scores[chat_id] = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Клик!")
    markup.add(button)
    bot.send_message(chat_id, "Добро пожаловать! Нажимай на кнопку, чтобы получить очки.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_click(message):
    chat_id = message.chat.id
    if message.text == "Клик!":
        user_scores[chat_id] += 1
        bot.send_message(chat_id, f"Вы получили 1 очко! Ваши очки: {user_scores[chat_id]}")
    else:
        bot.send.message(chat_id, "Нажмите на кнопку 'Клик!' чтобы получить очки.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
