import telebot
import os

# GitHub Secrets থেকে Bot Token নেবে
API_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "আসসালামু আলাইকুম! ✅ তোমার Task Manager Bot GitHub Actions থেকে চলছে 🚀")

# /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Available commands:\n/start - Welcome\n/help - Help\n/echo <text> - Echo back")

# /echo command
@bot.message_handler(commands=['echo'])
def echo_message(message):
    text = message.text.replace("/echo", "").strip()
    if text:
        bot.reply_to(message, f"তুমি লিখেছো: {text}")
    else:
        bot.reply_to(message, "⚠️ কিছু লিখে দাও /echo এর পরে।")

# fallback
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"তুমি লিখেছো: {message.text}")

if __name__ == "__main__":
    bot.remove_webhook()  # webhook conflict avoid করবে
    bot.polling(non_stop=True)
