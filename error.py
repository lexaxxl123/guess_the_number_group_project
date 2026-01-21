#tyt ya bery na random chislo 5 , prosto kak primer
SECRET_NUMBER = '5'


def check_answer(message):
    user_input = message.text
    chat_id = message.chat.id
    user_name = message.from_user.first_name

    logging.info(f'text {user_input} | user_name -> {user_name}, chat_id -> {chat_id}')

    if user_input == SECRET_NUMBER:
        bot.send_message(chat_id, 'pravilno')
    else:
        bot.send_message(chat_id, 'ne pravilno')