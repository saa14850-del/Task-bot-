import telebot
from config import BOT_TOKEN
from handlers import admin, group, general

bot = telebot.TeleBot(BOT_TOKEN)

admin.register(bot)
group.register(bot)
general.register(bot)

bot.infinity_polling()
