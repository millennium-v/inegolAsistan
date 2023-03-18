import os
from dotenv import load_dotenv
import telebot
import weather
import upcoming_events
import pharmacy
from pharmacy import get_pharmacies


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


# Telegram bot komutu /etkinlik için işlev
@bot.message_handler(commands=['etkinlik'])
def send_events(message):
    # Kullanıcının kim olduğunu öğrenin
    user_name = message.from_user.username

    events = upcoming_events.get_events()

    # Kullanıcının kim olduğunu yanıtınıza ekleyin
    bot.send_message(message.chat.id, f"Selam, @{user_name}\n{events}")

# Telegram bot komutu /eczane için işlev
@bot.message_handler(commands=['eczane'])
def send_pharmacies(message):

    # Kullanıcının kim olduğunu öğrenin
    user_name = message.from_user.username

    pharmacies = get_pharmacies()

    output_message = "Nöbetçi Eczaneler:\n\n"

    for pharmacy in pharmacies:
        output_message += f"{pharmacy['name']}\n{pharmacy['phone']}\n{pharmacy['address']}\n{pharmacy['date_range']} \n\n"

   # Kullanıcının kim olduğunu yanıtınıza ekleyin
    bot.send_message(chat_id=message.chat.id, text=output_message)


# Botu başlatın
bot.polling()
