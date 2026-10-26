import telebot
import time

BOT_TOKEN = "8431872317:AAFAxjNKjEXLAcZV2_ePV2JrWXE4QrtH9xQ"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 Topwork Market Bot Active!\n\n✅ Bot is Online\n/help - Help")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Topwork Market - Bot Ready!")

@bot.message_handler(func=lambda m: True)
def all_msg(message):
    bot.reply_to(message, f"আপনি বলেছেন: {message.text}\n\nBot কাজ করছে ✅")

print("Bot Started...")
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
