from database import get_welcome, get_warn_limit, is_locked, warns
from telebot.types import Message

def register(bot):
    @bot.message_handler(content_types=['new_chat_members'])
    def welcome(message: Message):
        for new_member in message.new_chat_members:
            bot.send_message(message.chat.id, get_welcome().format(name=new_member.first_name))

    @bot.message_handler(func=lambda m: True)
    def moderation(message: Message):
        text = message.text or ""
        chat_warns = warns.setdefault(message.chat.id, {})
        user_id = message.from_user.id

        # Anti-link
        if is_locked("link") and ("http://" in text or "https://" in text):
            bot.delete_message(message.chat.id, message.message_id)
            chat_warns[user_id] = chat_warns.get(user_id, 0) + 1
            bot.send_message(message.chat.id, f"{message.from_user.first_name} warned! ({chat_warns[user_id]}/{get_warn_limit()})")
            if chat_warns[user_id] >= get_warn_limit():
                bot.kick_chat_member(message.chat.id, user_id)
                bot.send_message(message.chat.id, f"{message.from_user.first_name} auto-kicked for exceeding warn limit")
                chat_warns[user_id] = 0
