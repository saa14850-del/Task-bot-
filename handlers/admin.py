from config import ADMINS
from database import settings, save_settings

def register(bot):
    def is_admin(user_id):
        return user_id in ADMINS

    @bot.message_handler(commands=['kick'], chat_types=['group','supergroup'])
    def kick_user(message):
        if not is_admin(message.from_user.id):
            return
        try:
            user_id = int(message.text.split()[1])
            bot.kick_chat_member(message.chat.id, user_id)
            bot.send_message(message.chat.id, f"User {user_id} kicked!")
        except:
            bot.send_message(message.chat.id, "Usage: /kick <user_id>")

    @bot.message_handler(commands=['ban'], chat_types=['group','supergroup'])
    def ban_user(message):
        if not is_admin(message.from_user.id):
            return
        try:
            user_id = int(message.text.split()[1])
            bot.kick_chat_member(message.chat.id, user_id)
            bot.send_message(message.chat.id, f"User {user_id} banned!")
        except:
            bot.send_message(message.chat.id, "Usage: /ban <user_id>")

    @bot.message_handler(commands=['mute'], chat_types=['group','supergroup'])
    def mute_user(message):
        if not is_admin(message.from_user.id):
            return
        try:
            user_id = int(message.text.split()[1])
            bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
            bot.send_message(message.chat.id, f"User {user_id} muted")
        except:
            bot.send_message(message.chat.id, "Usage: /mute <user_id>")

    @bot.message_handler(commands=['unmute'], chat_types=['group','supergroup'])
    def unmute_user(message):
        if not is_admin(message.from_user.id):
            return
        try:
            user_id = int(message.text.split()[1])
            bot.restrict_chat_member(message.chat.id, user_id,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True)
            bot.send_message(message.chat.id, f"User {user_id} unmuted")
        except:
            bot.send_message(message.chat.id, "Usage: /unmute <user_id>")

    @bot.message_handler(commands=['lock'], chat_types=['group','supergroup'])
    def lock_feature(message):
        if not is_admin(message.from_user.id):
            return
        try:
            feature = message.text.split()[1]
            settings["locks"][feature] = "on"
            save_settings()
            bot.send_message(message.chat.id, f"{feature} locked!")
        except:
            bot.send_message(message.chat.id, "Usage: /lock <feature>")

    @bot.message_handler(commands=['unlock'], chat_types=['group','supergroup'])
    def unlock_feature(message):
        if not is_admin(message.from_user.id):
            return
        try:
            feature = message.text.split()[1]
            settings["locks"][feature] = "off"
            save_settings()
            bot.send_message(message.chat.id, f"{feature} unlocked!")
        except:
            bot.send_message(message.chat.id, "Usage: /unlock <feature>")
