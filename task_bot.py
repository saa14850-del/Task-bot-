import os
import telebot

API_TOKEN = os.getenv("BOT_TOKEN")  # GitHub Secrets থেকে নেওয়া হবে
bot = telebot.TeleBot(API_TOKEN)

tasks = {}

# Start কমান্ড
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "👋 Assalamu Alaikum!\nআমি তোমার Task Manager Bot.\n\n"
        "📝 কমান্ডসমূহ:\n"
        "/add <টাস্ক> → নতুন টাস্ক যোগ করো\n"
        "/list → সব টাস্ক দেখো\n"
        "/done <নাম্বার> → টাস্ক সম্পন্ন করো"
    )

# টাস্ক যোগ করা
@bot.message_handler(commands=['add'])
def add_task(message):
    chat_id = message.chat.id
    task_text = message.text.replace("/add", "").strip()
    if not task_text:
        bot.reply_to(message, "⚠️ টাস্ক লিখো, যেমনঃ `/add বাজার করতে হবে`")
        return
    if chat_id not in tasks:
        tasks[chat_id] = []
    tasks[chat_id].append(task_text)
    bot.reply_to(message, f"✅ টাস্ক যোগ করা হলো:\n{task_text}")

# সব টাস্ক দেখানো
@bot.message_handler(commands=['list'])
def list_tasks(message):
    chat_id = message.chat.id
    if chat_id not in tasks or len(tasks[chat_id]) == 0:
        bot.reply_to(message, "📭 কোনো টাস্ক নেই।")
    else:
        task_list = ""
        for i, task in enumerate(tasks[chat_id], 1):
            task_list += f"{i}. {task}\n"
        bot.reply_to(message, f"📌 তোমার টাস্ক লিস্ট:\n\n{task_list}")

# টাস্ক Done করা
@bot.message_handler(commands=['done'])
def done_task(message):
    chat_id = message.chat.id
    try:
        task_number = int(message.text.replace("/done", "").strip()) - 1
        if 0 <= task_number < len(tasks[chat_id]):
            done_task = tasks[chat_id].pop(task_number)
            bot.reply_to(message, f"🎉 সম্পন্ন হয়েছে:\n{done_task}")
        else:
            bot.reply_to(message, "⚠️ টাস্ক নাম্বার সঠিক নয়।")
    except:
        bot.reply_to(message, "❌ উদাহরণ: `/done 1`")

print("🤖 Bot is running...")
bot.polling()
