@bot.message_handler(commands=['start'])

def start_message(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name

    logging.info(f'commands "start"| user_name -> {user_name}, chat_id -> {chat_id}')

    bot.send_message(chat_id, f'Hello {user_name}')