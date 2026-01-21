import telebot
import logging
import random

TOKEN = '7652443729:AAH2F1Exu5jfU6HOG0mip7bVHOtTe-EL5kI'

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

bot = telebot.TeleBot(TOKEN)

THE_number = 0

def is_correct_guess(guess, number):
    if guess == number:
        return True
    elif guess != number:
        return False

def validate_guess(user_number, message):
    try:
        guess = int(user_number)
        if 1 <= guess <= 100:
            return guess
        else:
            bot.send_message(message.chat.id, "введіть число від 1 до 100!!!")
            return None
    except ValueError:
        bot.send_message(message.chat.id, "введіть число від 1 до 100!!!")
        return None

@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name

    logging.info(f'commands "start"| user_name -> {user_name}, chat_id -> {chat_id}')

    global THE_number
    THE_number = random.randint(1, 100)

    bot.send_message(chat_id, f'Hello {user_name}')
    bot.send_message(chat_id, 'Спробуй вгадати число від 1 до 100!')

@bot.message_handler(content_types=['text'])
def check_answer(message):
    global THE_number

    user_input = message.text
    chat_id = message.chat.id
    user_name = message.from_user.first_name

    logging.info(f'text {user_input} | user_name -> {user_name}, chat_id -> {chat_id}')

    guess = validate_guess(user_input, message)

    if guess is None:
        return

    if is_correct_guess(guess, THE_number):
        bot.send_message(chat_id, 'pravilno')
        THE_number = random.randint(1, 100)
        bot.send_message(chat_id, 'Я загадал новое число. Играем дальше!')
    else:
        bot.send_message(chat_id, 'ne pravilno')

if __name__ == '__main__':
    bot.polling(none_stop=True)