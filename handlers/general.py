from database import get_rules, get_custom_response

def register(bot):
    @bot.message_handler(commands=['start','help'], chat_types=['private','group','supergroup'])
    def start_help(message):
        text = """
Advanced Rose Bot Commands:
/kick <user_id> - Kick user
/ban <user_id> - Ban user
/mute <user_id> - Mute user
/unmute <user_id> - Unmute user
/lock <feature> - Lock feature
/unlock <feature> - Unlock feature
/rules - Show group rules
Custom commands defined in settings.json
        """
        bot.send_message(message.chat.id, text)

    @bot.message_handler(commands=['rules'], chat_types=['private','group','supergroup'])
    def rules(message):
        bot.send_message(message.chat.id, get_rules())

    @bot.message_handler(func=lambda m: True, chat_types=['private','group','supergroup'])
    def auto_response(message):
        text = message.text or ""
        if text.startswith("/"):
            cmd = text[1:].lower()
            resp = get_custom_response(cmd)
            if resp:
                bot.send_message(message.chat.id, resp)
