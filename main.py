import os
from dotenv import load_dotenv
import telebot
import weather

# .env dosyasındaki TOKEN'ı yükleyin
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

# Telegram bot komutu /hava için işlev
@bot.message_handler(commands=['hava'])
def send_weather(message):
    # Kullanıcının kim olduğunu öğrenin
    user_name = message.from_user.username

    response = weather.get_weather()

    # Kullanıcının kim olduğunu yanıtınıza ekleyin
    bot.send_message(message.chat.id, f"Selam, @{user_name}\n{response}")

# Botu başlatın
bot.polling()
